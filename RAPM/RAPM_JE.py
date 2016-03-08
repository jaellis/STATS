from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model
import numpy as np

units = []
eff = []
poss = []
with open('/Users/mozilla/Desktop/STATS/RAPM/RAPMMatchupFile2015.CSV','r') as a:
	csvr = csv.reader(a)
	names = csvr.next()
	effIndex = names.index('Eff')
	possIndex = names.index('Poss')
	for line in csvr:
		home_indices = [i for i, x in enumerate(line) if x == "1" and i<len(line)-4]
		away_indices = [i for i, x in enumerate(line) if x == "-1" and i<len(line)-4]
		
		home = {}
		away = {}
		for h in range(len(home_indices)):
			home[names[home_indices[h]]] = 1
			away[names[away_indices[h]]] = -1

		stint = home.copy()
		stint.update(away)

		if line[names.index('Poss')]>2:
			units.append(stint)

			eff.append(float(line[names.index('Eff')]))
			poss.append(float(line[names.index('Poss')]))

print len(units),len(eff),len(poss)


v = DictVectorizer(sparse=False)
list_dicts = []

for unit in units:
    list_dicts.append({name: 1 for name in unit})
# print(list_dicts)

# X = v.fit_transform(list_dicts)
# print(X)

u = DictVectorizer(sparse=False)
u_mat = u.fit_transform(units)
# print(u_mat) # a giant list of lists where each array contains five +1's, five -1's, and a whole mess of 0's
# print(eff[:25]) # just showing the first 25 stints
# print(poss[:100]) # just showing the first 100 stints

players = u.get_feature_names()

# this is where an optimal alpha value is found to regularize the data
clf = linear_model.RidgeCV(alphas=(np.array([0.01,0.1,1.0,10,100,500,1000,2000,5000])),cv=5)
clf.fit(u_mat,eff,sample_weight=poss)
print(clf.alpha_)

ratings = []
for player in players:
    ratings.append((player,clf.coef_[players.index(player)]))
ratings.sort(key=lambda tup: tup[1],reverse=True) # sort by rating in descending order

# print ratings
for idx, rating in enumerate(ratings):
    print(idx+1, "{}".format(rating[0]), "{0:.2f}".format(rating[1]))