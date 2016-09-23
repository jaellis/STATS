# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cd '~/Desktop/STATS'
#import tensorflow as tf
import pandas as pd
import sqlite3 as sql
import numpy as np
import pandas as pd
import re
from collections import defaultdict as dd
import math

dbfilename = '1570554-bigTable.db'
conn = sql.connect(dbfilename)
data = pd.read_sql_query("SELECT * from biggerTable",conn)
import time


# frame_times = []
# for i in range(1,len(data)):
# 	frame_times.append(data[col_names[0]][i]-data[col_names[0]][i-1])

col_names = data.columns.values.tolist()

# screen_times = {'onsets': [1447818761818.80,1447818761818.80,
# 1447818876884.40,1447818876884.40,1447818922431.20,1447820734115.10,
# 1447820739209.15,1447820913126.01,1447820913126.01,1447820913126.01,
# 1447820975033.70,1447821034364.40,1447821121442.69,1447821316035.40],
# 'offsets':[1447818770808.30,1447818775902.35,1447818885873.90,
# 1447818894863.40,1447818927824.90,1447820737710.90,1447820743703.90,
# 1447820918100.20,1447820921696.00,1447820925112.01,1447820978929.15,
# 1447821041855.65,1447821128454.50,1447821324425.60]}1447818248946.55	1447818251449.47


screen_times = {'onsets': [1447818248946.55,1447818280983.92,1447818280983.92,1447818293665.39
,1447818798087.21,1447818799505.53,1447818847928.69,1447818847928.69
,1447818847928.69,1447818865165.47,1447818881684.74,1447818905929.69
,1447818960109.57]
	
,'offsets':[1447818252867.79,1447818283486.84,1447818285989.76,1447818295167.14
,1447818799088.38,1447818800756.99,1447818849313.64,1447818850314.81
,1447818851265.92,1447818866250.07,1447818883770.51,1447818907881.97,1447818962445.63]
}

players={'screener':['Bogut','Barnes','Carroll','Scola','Curry'
					,'Valanciunas','Valanciunas','Ezeli','Thompson','Green'
					,'Valanciunas','Iguodala','Ezeli','Green']
		 ,'screen recipient':['Curry','Curry','DeRozan','DeRozan','Thompson'
		 			,'DeRozan','Scola','Curry','Curry','Curry','Carroll','Curry'
		 			,'Thompson','Thompson']
		 ,'recipient defender': ['Lowry','Lowry','Thompson','Barnes','Carroll'
		 			,'Thompson','Green','Lowry','Lowry','Lowry','Iguodala','Lowry','Carroll'
		 			,'Carroll']
		}

playerIDs = {'Valanciunas': 599780,
			'Thompson': 	457611,
			'Scola': 		168061,
			'Lowry': 		266394,
			'Bogut': 		229912,
			'Curry': 		338365,
			'DeRozan': 		457594,
			'Carroll': 		262890,
			'Green': 		468895,
			'Barnes':		552336,'Ezeli':417020,'Iguodala':173004
			}

playerTeams = {
			'Home': ['Thompson','Bogut','Curry','Green','Barnes','Ezeli','Iguodala']
			,'Away': ['Valanciunas','Scola','Lowry','DeRozan','Carroll']
}

playerIDTeams = {
			'Home': [457611,229912,338365,468895,552336,417020,173004]
			,'Away': [599780,168061,266394,457594,262890]
}

screendf=pd.DataFrame(screen_times)

screen_frames = {'frame_offsets':[],'frame_onsets':[],'lengths':[]}
# Find first row greater than given UTC 
for t in screendf.columns.values.tolist():
	for s in screendf[t]:
		for ind,i in enumerate(data[col_names[0]]):
			if i > s:
				screen_frames['frame_'+t].append(ind)
				break
for ind,sc in enumerate(screen_frames['frame_onsets']):
	screen_frames['lengths'].append(screen_frames['frame_offsets'][ind] - sc)


# Matchup player names with playerIDs
# Grab any data relating to those players within the onset-to-offset period

playerIDcols = []
for i in col_names:
	if re.search(r'\d+PlayerID',i):
		playerIDcols.append(i)

playerDataCols = []
for i in col_names:
	if re.search(r'Player.\d+',i) and i not in playerIDcols:
		playerDataCols.append(i)


screen_data = dd()


# def get_screen_data(data,players,screen_frames,playerIDs,playerIDcols,playerDataCols):
# iterate over screen frame rows
for ind,onset in enumerate(screen_frames['frame_onsets']):
    for r in range(screen_frames['frame_onsets'][ind],screen_frames['frame_offsets'][ind]):
        # Get feature row
        row = data.iloc[r]
        screener = None
        screenerID_offdef = 'empty'
        screenerID_homeaway = 'empty'
        screen_recipient = None
        screen_recipientID_homeaway = 'empty'
        screen_recipientID_offdef = 'empty'
        recipient_dfndr = None
        recipient_dfndrID_homeaway = 'empty'
        recipient_dfndrID_offdef = 'empty'
        #Check which players match for this row
        for col in playerIDcols:
            if playerIDs[players['screener'][ind]] == row[col]:
#                print 'found screener in row ' + str(r) + '; screener: ' + players['screener'][ind] + ' screener recipient: ' + players['screen recipient'][ind]
                screener = re.search(r'\d+',col).group()				
                offense = 'Home' if players['screener'] in playerTeams['Home'] else 'Away'				                
                screen_data[ind] = {'screener': {}, 'screen recipient': {}, 'recipient defender': {} }
                screen_data[ind]['screener']['home player'] = screenerID_homeaway
                screenerID_homeaway = 'homePlayerA' + screener if playerIDs[players['screener'][ind]] in playerIDTeams['Home'] else 'awayPlayerB' + screener
                screenerID_offdef = 'offPlayerO' + screener
            elif playerIDs[players['screen recipient'][ind]] == row[col]:                
#                print 'found screener recipient in row ' + str(r)
                screen_recipient = re.search(r'\d+',col).group()
                screen_recipientID_homeaway = 'homePlayerA' + screen_recipient if playerIDs[players['screener'][ind]] in playerIDTeams['Home'] else 'awayPlayerB' + screen_recipient
                screen_recipientID_offdef = 'offPlayerO' + screen_recipient
            elif playerIDs[players['recipient defender'][ind]] == row[col]:
                recipient_dfndr = re.search(r'\d+',col).group()
                recipient_dfndrID_homeaway = 'homePlayerA' + recipient_dfndr if playerIDs[players['screener'][ind]] in playerIDTeams['Away'] else 'awayPlayerB' + recipient_dfndr
                recipient_dfndrID_offdef = 'defPlayerD' + recipient_dfndr
        if screener != None:
            for datacol in playerDataCols:
                if screenerID_offdef in datacol or screenerID_homeaway in datacol:
                    new_col = datacol.split(screenerID_offdef)[1] if screenerID_offdef in datacol else datacol.split(screenerID_homeaway)[1]
                    if new_col not in screen_data[ind]['screener']:
                        screen_data[ind]['screener'][new_col] = [row[datacol]]
                    screen_data[ind]['screener'][new_col].append(row[datacol])
                if screen_recipientID_offdef in datacol or screen_recipientID_homeaway in datacol:
                    new_col = datacol.split(screen_recipientID_offdef)[1] if screen_recipientID_offdef in datacol else datacol.split(screen_recipientID_homeaway)[1]
                    if new_col not in screen_data[ind]['screen recipient']:
                        screen_data[ind]['screen recipient'][new_col] = [row[datacol]]
                    screen_data[ind]['screen recipient'][new_col].append(row[datacol])
                if recipient_dfndrID_offdef in datacol or recipient_dfndrID_homeaway in datacol:
                    new_col = datacol.split(recipient_dfndrID_offdef)[1] if recipient_dfndrID_offdef in datacol else datacol.split(recipient_dfndrID_homeaway)[1]
                    if new_col not in screen_data[ind]['recipient defender']:
                        screen_data[ind]['recipient defender'][new_col] = [row[datacol]]
                    screen_data[ind]['recipient defender'][new_col].append(row[datacol])

        screen_data[ind]['IDs'] = {'screener': {'homeaway': screenerID_homeaway,
        										'offdef': screenerID_offdef
        										},
        							'screen recipient': {'homeaway': screen_recipientID_homeaway,
        												'offdef': screen_recipientID_offdef
        												},
        							'recipient defender': {'homeaway': recipient_dfndrID_homeaway,
        												'offdef': recipient_dfndrID_offdef
        													}
        							}


def get_player_data_cols(data):

	playerDataCols = []

	col_names = data.columns.values.tolist()

	for i in col_names:
		if re.search(r'Player.\d+',i) and i not in playerIDcols:
			playerDataCols.append(i)

	return playerDataCols


def moving_window(sample,test,bin_inc,frame_inc):

	'''
	Simplest unit method of measuring difference in player attributes

	INPUT
		sample			sample data (list)
		test			test data (list)
		bin_inc			how often (in frames) to calculate differences/how far to slide bin
		frame_inc 		within the bin, how often (in frames) to calc difference
	'''

	start_ind = -1
	end_ind = len(sample) - 1

	diff_mat = []

	for i in range(0,len(test) - len(sample),bin_inc):

		start_ind += 1
		end_ind += 1
		bin = test[start_ind:end_ind]
		running_diff = 0

		for s in range(start_ind,end_ind,frame_inc):
						
			running_diff += abs(bin[s]-sample[s - start_ind])

		diff_mat.append(running_diff)

	return {'Diff Mat': diff_mat, 'Running Diff': running_diff}



def find_col_match(col_nick,col_list):

	'''
	take a column name (partial) and find the matching column(s) in the list of data columns

	INPUT 
		col_nick 	nickname (shortened name) of column
		col_list 	list of all possible column names excluding those with 'playerID

	OUTPUT
		out 		list of matching column names
	'''

	out = []

	for i in col_list:

		if col_nick in i:

			out.append(i)

	return out



def crawl_player(sample,test,col_list,cons,b_inc,f_inc):

	'''
	Crawl over sample dictionary (a SUB SAMPLE for a single player) and feed columns into <<moving_window()>>

	INPUT
		sample 		sample data (dict) !! SUB-SAMPLE !!
		test 		test data (DataFrame)
		col_list 	list of all possible column names excluding those with 'playerID
		cons 		list of constraining col nicknames
	OUTPUT
		diff 		a dictionary of differences between the sample and test with keys for column in the test data nested under the column abbrev in the sample
	'''

	diff = {}

	for col in sample:

		diff[col] = {}
		
		if col in cons or not cons:

			matches = find_col_match(col,col_list)

			for m in matches:

				start_time = time.clock()

				temp_diff = moving_window(sample[col],test[m],b_inc,f_inc)

				print '<' + m + '> elapsed: ' + str(time.clock() - start_time)

				if m not in diff[col]:
					diff[col][m] = []

				diff[col][m].append(temp_diff['Diff Mat'])

	return diff



def run_all(sample,test,b_inc,f_inc,*args):

	'''
	Go through each screen instance, feed the player to crawl_player()

	INPUT
		sample 		sample data (ALL)
		test 		test data (DataFrame)
		*args 		var args for constraining column names -- pass a list of column nicknames

	OUTPUT
		differences 	
	'''

	constraints = []
	
	for a in args:
		constraints.append(a)

	col_names = get_player_data_cols(test)

	total_out = {}

	for screen_ind in sample:

		total_out[screen_ind] = {}

		print 'running screen #' + str(screen_ind)

		screen_diff = {}

		for player in sample[screen_ind]:			

			print 'player: ' + player
			
			diff = crawl_player(sample[screen_ind][player],test,col_names,constraints,b_inc,f_inc)

			total_out[screen_ind][player] = diff

	return total_out


def normalize(data,output,depth):
	
	'''
	'''

	if type(data) is list:

		print 'Leaf at depth = ' + str(depth)

		scrub_data = np.nan_to_num(np.array(data))
		return (scrub_data - scrub_data.mean()) / scrub_data.std()

	else:

		for key in data:

			print 'Recursive call at depth ' + str(depth) + ' and key ' + str(key)
			depth+=1
			output[key] = normalize(data[key],{},depth)

		return output

def KNN_data_clean(IDs,raw):

	'''
	'''		

	cleaned = {}

	final = {}

	found = {}

	for player_type in IDs:

		cols = raw[player_type].keys()

		for datatype in raw[player_type]:

			cleaned[datatype] = {'screen':[],'other':[] }

			for player_id in IDs[player_type]:

				for rawCol in raw[player_type][datatype]:

					if IDs[player_type][player_id] in rawCol:

						cleaned[datatype]['screen'].append(rawCol)
						found[datatype] = 1

						if IDs[player_type][player_id] in cleaned[datatype]['other']:
							cleaned_data[datatype]['other'].pop(cleaned_data[datatype]['other'].index(IDs[player_type][player_id]))

					elif IDs[player_type][player_id] not in cleaned[datatype]['screen']:

						cleaned[datatype]['other'].append(rawCol)
	
	print 'Found matches in:'
	for i in found:

		print i
		final[i] = cleaned[i]

	return final


def KNN(train,test,exemplar_cols,predict_cols,num_neighbors):

	'''
	'''

	from sklearn.neighbors import KNeighborsRegressor

	knn = KNeighborsRegressor(n_neighbors = num_neighbors)

	knn.fit(train[exemplar_cols],train[predict_cols])

	predictions = knn.predict(test[predict_cols])

	return predictions


def feed_KNN(data,train_percent,column_data):

	'''
	INPUT
		data 				all data
		train_percent 		percentage of data to use as training
		cleaned_data 		dict of which columns are exempar and which are test (output from <KNN_data_clean>)
	'''

	exemplar_cols = {} 
	predict_cols = {}

	knn_results = {}

	train = data[0:int(len(data)*train_percent)]
 	test = data[int(len(data)*train_percent) + 1:]	

	for i in column_data:

		exemplar_cols[i] = []
		predict_cols[i] = []

		for c in column_data[i]:

			exemplar_cols[i].append(column_data[i][c]['screen'])
			predict_cols[i].append(column_data[i][c]['other'])

		knn_results[i] = KNN(train,test,exemplar_cols,predict_cols,10)

	return knn_results



def get_matching_players_by_frame(data):

	'''
	Return a nested dict with <KEY> player_id and <VALUE> dict with 

	Scratching this for now
	'''
	pass


def match_up_players(data):

	'''
	Nest difference to exemplar data under the same player id
	'''

	pass


################################
################################
################################
################################


# class knn_data:

# 	def 

knn_data = np.array([])
screen_knn_data = np.array([])

dataTypes= ['ThetaPos','ThetaVel','AcclMag','ThetaAccl','distToBall']#,'XAccl','YAccl']
dataCols = []
for i in playerDataCols:
	for d in dataTypes:
		if d in i:
			dataCols.append(i)
			break

max_array_length = [len(dataTypes)*5*max(screen_frames['lengths'])] # data types * players * max screen duration

for ind,onset in enumerate(screen_frames['frame_onsets'][0:5]):

	players = []

	for pid in screen_data[ind]['IDs']:

		for pid_sub in screen_data[ind]['IDs'][pid]:

			if screen_data[ind]['IDs'][pid][pid_sub] != 'empty':

				players.append('Player'+screen_data[ind]['IDs'][pid][pid_sub].split('Player')[1])

	### Set constants/initialize variables ###
	actualscreen = np.zeros(max_array_length) # initialize screen data (label = 1)
	ac_cnt = 0
	screen_duration = screen_frames['frame_offsets'][ind] - onset
	startTime = time.time()
	###	###

	for col in dataCols:

		startLoc = screen_duration*ac_cnt

		if re.search(r'Player.\d+',col).group() in players:
			
			actualscreen[startLoc:startLoc+screen_duration] = data[col][onset:screen_frames['frame_offsets'][ind]]
			ac_cnt+=1

	if ind == 0:
		screen_knn_data = [actualscreen]

	else:
		screen_knn_data = np.append(screen_knn_data,[actualscreen],axis=0)

	print "\nWrote actual screen data, screen #%d in %ds" % (ind,time.time() - startTime)

	startTime = time.time()

	for i in range(0,len(data[col]) - screen_duration,15):

		candidate = np.zeros(max_array_length)

		cand_cnt = 0

		startLoc = screen_duration*cand_cnt

		for col in dataCols:

			candidate[startLoc:startLoc+screen_duration] = data[col][i:i+screen_duration]

			cand_cnt+=1

		if ind == 0:
			knn_data = [candidate]

		else:
			knn_data = np.append(knn_data,[candidate],axis=0)

	print "Done with screen #%d in %ds\n" % (ind,time.time() - startTime)

			# if knn_data.size == 0:
					# knn_data = [np.array(list(data[col][i:i+screen_duration]))]

				# try:
				# 	knn_data = np.append(knn_data,[np.array(list(data[col][i:i+screen_duration]))],axis = 0)
				# except:
				# 	pass

				# 	try:
				# 		screen_knn_data = np.append(screen_knn_data,[np.nan_to_num(np.array(list(data[col][screen_frames['frame_onsets'][ind]:screen_frames['frame_offsets'][ind]])))],axis = 0)
				# 	except:
				# 		pass





