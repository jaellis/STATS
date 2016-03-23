import glob, re, csv
import math
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model	
from collections import defaultdict as dd
import pdb

def calc_rapm(units,eff,poss,alpha):
	'''
	Calculate RAPM (regularized adjusted +/-) for a single or multiple seasons

	Code source: http://nbviewer.jupyter.org/gist/EvanZ/48bf713ce9eb14f28d58
	'''

	u = DictVectorizer(sparse=False)
	u_mat = u.fit_transform(units)
	# print(u_mat) # a giant list of lists where each array contains five +1's, five -1's, and a whole mess of 0's
	# print(eff[:25]) # just showing the first 25 stints
	# print(poss[:100]) # just showing the first 100 stints

	players = u.get_feature_names()
	
	results = {}
	# loop over some alphas for comparison
	# for a in range(1,101,10)+range(101,1001,100):
	print "...fitting model\n\n"
	alphas = range(1,100,10)+range(101,3001,200) if alpha is None else [alpha]
	# alphas = range(101,3001,200)
	clf = linear_model.RidgeCV(alphas=alphas,cv=5)
	print "...determining best alpha value\n\n"
	clf.fit(u_mat,eff,sample_weight=poss)
	print "*-*-*-*-*-*\nmodel-chosen alpha: %d \n*-*-*-*-*-*\n\n" % clf.alpha_
	results['chosen alpha'] = clf.alpha_

	# for a in alphas:
	for a in [clf.alpha_]:
		# this is where an optimal alpha value is found to regularize the data
		clf = linear_model.RidgeCV(alphas=([a]),cv=5)
		# clf = linear_model.RidgeCV(alphas=(np.array([0.01,0.1,1.0,10,100,500,1000,2000,5000,10000])),cv=5)
		clf.fit(u_mat,eff,sample_weight=poss)
		print(clf.alpha_)

		ratings = []
		for player in players:
			ratings.append((player,clf.coef_[players.index(player)]))
		ratings.sort(key=lambda tup: tup[1],reverse=True) # sort by rating in descending order

		# print ratings
		for idx, rating in enumerate(ratings):
			if idx <= 10:
				print(idx+1, "{}".format(rating[0]), "{0:.2f}".format(rating[1]))

		results[a]=ratings
	# return ratings
	return results




def weight_prior(prior_rapm,curr_units,off_def):
	'''Create a weighted prior for previous season(s)
	'''

	def log_rapm(x, off_def):

		if x < -1 or x > 1:
			y = off_def + (x/abs(x)) * math.log(abs(x))
		else:
			y = off_def

		return y


	plyr_prior = {}

	for p in prior_rapm:
		plyr_prior[p[0]] = p[1]

	for curr_unit in curr_units:

		for curr_plyr in curr_unit:

			if curr_plyr in plyr_prior:
				
				curr_unit[curr_plyr] = log_rapm(plyr_prior[curr_plyr],off_def)

			else:
				curr_unit[curr_plyr] = off_def/.6

	return curr_units





def load_data(seasonStart,seasonFinish,off_def_split_in=0):
	'''
	Get data out for all listed seasons
	'''

	off_def_split = bool(off_def_split_in)

	units = []
	off_units = []
	def_units = []
	eff = []
	poss = []
	seasons = range(seasonStart,seasonFinish)

	for fnm in glob.glob('../RAPM_data/RAPM*.CSV'):

		if int(re.search(r'\d+',fnm).group()) in seasons:

			with open(fnm,'r') as a:
				csvr = csv.reader(a)
				names = csvr.next()
				effIndex = names.index('Eff')
				possIndex = names.index('Poss')
				for line in csvr:
					off_indices = [i for i, x in enumerate(line) if x == "1" and i<len(line)-4]
					def_indices = [i for i, x in enumerate(line) if x == "-1" and i<len(line)-4]
					
					offense = {}
					defense = {}
					for h in range(len(off_indices)):
						offense[names[off_indices[h]]] = 1
						defense[names[def_indices[h]]] = -1

					stint = offense.copy()
					stint.update(defense)

					if line[names.index('Poss')]>2:
						units.append(stint)
						off_units.append(offense)
						def_units.append(defense)

						eff.append(float(line[names.index('Eff')]))
						poss.append(math.pow(float(line[names.index('Poss')]),2))

			print "{0} season: {1}, {2}, {3}".format(int(re.search(r'\d+',fnm).group()),len(units),len(eff),len(poss))

	if off_def_split:
		return off_units,def_units,eff,poss		
	else:
		return units,eff,poss




def ditch_losers(units,possessions,percentile):
	'''
	Group players that played fewer than min_poss possessions

	Input:
			units		 units list of dicts
			possessions	 possession list, AKA weights
			percentile 	 the percentile level at which to group players into Reference Players
	'''

	plyr_tot_poss = dd(int)

	print "...summing players' team possessions\n\n"
	for ind,u in enumerate(units):
		for p in u:
			# pdb.set_trace()
			plyr_tot_poss[p]+=possessions[ind]


	plyr_poss_list = []
	
	for p in plyr_tot_poss:
		plyr_poss_list.append(plyr_tot_poss[p])

	poss_percentile = np.percentile(np.array(plyr_poss_list),percentile)

	print "...bunching Reference Players\n\n"

	for unit in units:

		plyrs_to_bunch = []
		# Determine players below minimum possessions
		for plyr in unit:
			if plyr_tot_poss[plyr] < poss_percentile:
				plyrs_to_bunch.append(plyr)
		
		# Replace those players with name "Reference Player"
		for replace in plyrs_to_bunch:			
			unit["Reference Player"]=unit[replace]
			del(unit[replace])

	return units



def two_year_rapm(season):
	'''Get RAPM for the current season and previous, combined
	'''
	pass


def get_weighted_rapm(startSeason,endSeason):#curr_season,load_previous = True): #,single_seasons = False):
	'''
	Create prior with previous seasons

	INPUT:
			curr_season:	Season will not be calculated
			load_previous
	'''

	[prior_off_units,prior_def_units,prior_eff,prior_poss] = load_data(startSeason,endSeason - 1,True)

	[curr_off_units,curr_def_units,curr_eff,curr_poss] = load_data(endSeason - 1,endSeason,True)

	curr_off_units = ditch_losers(curr_off_units,curr_poss,10)
	curr_def_units = ditch_losers(curr_def_units,curr_poss,10)
	# pdb.set_trace()
	prior_off_units = ditch_losers(prior_off_units,prior_poss,10)
	prior_def_units = ditch_losers(prior_def_units,prior_poss,10)	

	prior_off_rapm = calc_rapm(prior_off_units,prior_eff,prior_poss,None)
	prior_def_rapm = calc_rapm(prior_def_units,prior_eff,prior_poss,None)

	chosen_off_alpha = prior_off_rapm['chosen alpha']
	chosen_def_alpha = prior_def_rapm['chosen alpha']

	prior_off = weight_prior(prior_off_rapm[chosen_off_alpha],curr_off_units,1)
	prior_def = weight_prior(prior_def_rapm[chosen_def_alpha],curr_def_units,-1)

	weighted_off_rapm = calc_rapm(prior_off,curr_eff,curr_poss,2101)
	weighted_def_rapm = calc_rapm(prior_def,curr_eff,curr_poss,2101)

	# print "finished calculating prior for seasons {0} to {1}" % seasonStart, seasonFinish

	return weighted_off_rapm,weighted_def_rapm