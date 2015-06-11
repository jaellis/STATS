 import random as r

qbs = ['Drew Brees',
'Andrew Luck',
'Eli Manning',
'Peyton Manning',
'Philip Rivers',
'Aaron Rodgers',
'Ben Roethlisberger',
'Matt Ryan',
'Matthew Stafford',
'Russell Wilson']

BigPlays = [52,
73,
52,
66,
57,
59,
55,
60,
53,
54]


Location = {'name':'QBs','children': [
 {'name':'Drew Brees', 
	'children': [
	{'name':'Less than -20','children':[],'size':6},
		{'name':'-20 to - 39','children':[],'size':20},
		{'name':'-40 to +40','children':[],'size':16},
		{'name':'+39 to +20','children':[],'size':10}]
,'size':52
},
{'name':'Andrew Luck',
	'children':	[
	{'name':'Less than -20','children':[],'size':8},
		{'name':'-20 to - 39','children':[],'size':29},
		{'name':'-40 to +40','children':[],'size':16},
		{'name':'+39 to +20','children':[],'size':20}]
	,'size':73
},
{'name':'Eli Manning',
	'children': [
	{'name':'Less than -20','children':[],'size':4},
		{'name':'-20 to - 39','children':[],'size':24},
		{'name':'-40 to +40','children':[],'size':14},
		{'name':'+39 to +20','children':[],'size':10}]
	,'size':52
},
{'name':'Peyton Manning',
	'children': [
	{'name':'Less than -20','children':[],'size':7},
		{'name':'-20 to - 39','children':[],'size':23},
		{'name':'-40 to +40','children':[],'size':18},
		{'name':'+39 to +20','children':[],'size':18}]
	,'size':66
},
{'name':'Philip Rivers',
	'children': [
	{'name':'Less than -20','children':[],'size':3},
		{'name':'-20 to - 39','children':[],'size':21},
		{'name':'-40 to +40','children':[],'size':18},
		{'name':'+39 to +20','children':[],'size':15}]
	,'size':57
},
{'name':'Aaron Rodgers',
	'children': [
	{'name':'Less than -20','children':[],'size':5},
		{'name':'-20 to - 39','children':[],'size':22},
		{'name':'-40 to +40','children':[],'size':22},
		{'name':'+39 to +20','children':[],'size':10}]
	,'size':59
} ,
{'name':'Ben Roethlisberger',
	'children': [
	{'name':'Less than -20','children':[],'size':8},
		{'name':'-20 to - 39','children':[],'size':19},
		{'name':'-40 to +40','children':[],'size':16},
		{'name':'+39 to +20','children':[],'size':12}]
	,'size':55
} ,
{'name':'Matt Ryan',
	'children': [
	{'name':'Less than -20','children':[],'size':8},
		{'name':'-20 to - 39','children':[],'size':26},
		{'name':'-40 to +40','children':[],'size':13},
		{'name':'+39 to +20','children':[],'size':13}]
	,'size':60
} ,
{'name':'Matthew Stafford',
	'children': [
	{'name':'Less than -20','children':[],'size':7},
		{'name':'-20 to - 39','children':[],'size':21},
		{'name':'-40 to +40','children':[],'size':19},
		{'name':'+39 to +20','children':[],'size':6}]
	,'size':53
} ,
{'name':'Russell Wilson',
	'children': [
	{'name':'Less than -20','children':[],'size':5},
		{'name':'-20 to - 39','children':[],'size':20},
		{'name':'-40 to +40','children':[],'size':18},
		{'name':'+39 to +20','children':[],'size':11}]
	,'size':54
} 
]} 


qbs = ['Drew Brees',
'Andrew Luck',
'Eli Manning',
'Peyton Manning',
'Philip Rivers',
'Aaron Rodgers',
'Ben Roethlisberger',
'Matt Ryan',
'Matthew Stafford',
'Russell Wilson']

LocBreakouts = [{'name':'Less than -20',
'children':[[{'name':'J.Graham','size':2},
{'name':'M.Colston','size':1},
{'name':'T.Cadet','size':1},
{'name':'N.Toon','size':1},
{'name':'K.Stills','size':1}],
[{'name':'C.Fleener','size':2},
{'name':'D.Moncrief','size':2},
{'name':'J.Doyle','size':1},
{'name':'H.Nicks','size':1},
{'name':'D.Allen','size':1},
{'name':'R.Wayne','size':1}],
[{'name':'O.Beckham Jr.','size':2},
{'name':'C.Washington','size':1},
{'name':'R.Randle','size':1}],
[{'name':'D.Thomas','size':3},
{'name':'C.Anderson','size':2},
{'name':'W.Welker','size':1},
{'name':'E.Sanders','size':1}],
[{'name':'M.Floyd','size':1},
{'name':'E.Royal','size':1},
{'name':'A.Gates','size':1}],
[{'name':'R.Cobb','size':2},
{'name':'A.Quarless','size':1},
{'name':'J.Nelson','size':1},
{'name':'J.Starks','size':1}],
[{'name':'L.Bell','size':3},
{'name':'M.Bryant','size':2},
{'name':'H.Miller','size':1},
{'name':'A.Brown','size':1},
{'name':'L.Moore','size':1}],
[{'name':'J.Jones','size':7},
{'name':'R.White','size':1}],
[{'name':'J.Bell','size':3},
{'name':'G.Tate','size':2},
{'name':'C.Fuller','size':1},
{'name':'C.Johnson','size':1}],
[{'name':'D.Baldwin','size':3},
{'name':'Z.Miller','size':1},
{'name':'J.Kearse','size':1}]]},
{'name':'-20 to - 39','children':
[[{'name':'M.Colston','size':8},
{'name':'K.Stills','size':3},
{'name':'J.Graham','size':2},
{'name':'B.Cooks','size':2},
{'name':'P.Thomas','size':2},
{'name':'J.Morgan','size':1},
{'name':'J.Hill','size':1},
{'name':'N.Toon','size':1}],
[{'name':'T.Hilton','size':9},
{'name':'C.Fleener','size':5},
{'name':'R.Wayne','size':4},
{'name':'T.Richardson','size':3},
{'name':'D.Herron','size':2},
{'name':'A.Bradshaw','size':2},
{'name':'D.Allen','size':2},
{'name':'D.Moncrief','size':2}],
[{'name':'O.Beckham Jr.','size':7},
{'name':'R.Randle','size':5},
{'name':'P.Parker','size':4},
{'name':'L.Donnell','size':3},
{'name':'V.Cruz','size':3},
{'name':'P.Hillis','size':1},
{'name':'D.Fells','size':1}],
[{'name':'E.Sanders','size':12},
{'name':'D.Thomas','size':7},
{'name':'J.Thomas','size':2},
{'name':'W.Welker','size':1},
{'name':'C.Anderson','size':1}],
[{'name':'M.Floyd','size':5},
{'name':'E.Royal','size':4},
{'name':'A.Gates','size':3},
{'name':'K.Allen','size':3},
{'name':'B.Oliver','size':2},
{'name':'L.Green','size':2},
{'name':'D.Brown','size':2}],
[{'name':'R.Cobb','size':9},
{'name':'J.Nelson','size':8},
{'name':'R.Rodgers','size':2},
{'name':'D.Adams','size':2},
{'name':'E.Lacy','size':1}],
[{'name':'A.Brown','size':6},
{'name':'L.Bell','size':4},
{'name':'M.Bryant','size':4},
{'name':'H.Miller','size':4},
{'name':'M.Wheaton','size':1}],
[{'name':'J.Jones','size':10},
{'name':'R.White','size':8},
{'name':'D.Hester','size':5},
{'name':'A.Smith','size':1},
{'name':'H.Douglas','size':1},
{'name':'D.Freeman','size':1}],
[{'name':'G.Tate','size':9},
{'name':'C.Johnson','size':7},
{'name':'J.Ross','size':2},
{'name':'T.Riddick','size':1},
{'name':'R.Bush','size':1},
{'name':'C.Fuller','size':1}],
[{'name':'D.Baldwin','size':6},
{'name':'J.Kearse','size':4},
{'name':'L.Willson','size':3},
{'name':'M.Lynch','size':2},
{'name':'Z.Miller','size':1},
{'name':'P.Harvin','size':1},
{'name':'T.Moeaki','size':1},
{'name':'R.Turbin','size':1},
{'name':'P.Richardson','size':1}]]
},
{'name':'-40 to +40','children': [
[{'name':'K.Stills','size':5},
{'name':'M.Colston','size':5},
{'name':'R.Meachem','size':2},
{'name':'T.Cadet','size':2},
{'name':'J.Graham','size':1},
{'name':'B.Cooks','size':1}],
[{'name':'T.Hilton','size':5},
{'name':'R.Wayne','size':3},
{'name':'C.Fleener','size':3},
{'name':'H.Nicks','size':2},
{'name':'D.Moncrief','size':1},
{'name':'D.Herron','size':1},
{'name':'D.Allen','size':1}],
[{'name':'O.Beckham Jr.','size':5},
{'name':'R.Randle','size':4},
{'name':'V.Cruz','size':2},
{'name':'L.Donnell','size':1},
{'name':'D.Fells','size':1},
{'name':'R.Jennings','size':1}],
[{'name':'E.Sanders','size':8},
{'name':'D.Thomas','size':7},
{'name':'J.Thomas','size':2},
{'name':'C.Anderson','size':1}],
[{'name':'E.Royal','size':7},
{'name':'M.Floyd','size':5},
{'name':'A.Gates','size':4},
{'name':'K.Allen','size':1},
{'name':'R.Brown','size':1}],
[{'name':'R.Cobb','size':10},
{'name':'J.Nelson','size':8},
{'name':'E.Lacy','size':2},
{'name':'A.Quarless','size':1},
{'name':'D.Adams','size':1}],
[{'name':'A.Brown','size':7},
{'name':'M.Wheaton','size':4},
{'name':'H.Miller','size':2},
{'name':'L.Moore','size':2},
{'name':'L.Bell','size':1}],
[{'name':'J.Jones','size':6},
{'name':'A.Smith','size':2},
{'name':'H.Douglas','size':2},
{'name':'R.White','size':2},
{'name':'D.Hester','size':1}],
[{'name':'C.Johnson','size':6},
{'name':'G.Tate','size':5},
{'name':'T.Riddick','size':2},
{'name':'J.Ross','size':2},
{'name':'C.Fuller','size':1},
{'name':'R.Broyles','size':1},
{'name':'J.Fauria','size':1},
{'name':'E.Ebron','size':1}],
[{'name':'C.Helfet','size':4},
{'name':'D.Baldwin','size':4},
{'name':'M.Lynch','size':3},
{'name':'R.Turbin','size':2},
{'name':'P.Richardson','size':2},
{'name':'K.Norwood','size':1},
{'name':'T.Moeaki','size':1},
{'name':'R.Lockette','size':1}]]
},
{
	'name':'+39 to +20','children': [
[{'name':'M.Colston','size':3},
{'name':'J.Graham','size':3},
{'name':'K.Stills','size':1},
{'name':'N.Toon','size':1},
{'name':'J.Hill','size':1},
{'name':'B.Cooks','size':1}],
[{'name':'T.Hilton','size':7},
{'name':'C.Fleener','size':5},
{'name':'R.Wayne','size':2},
{'name':'D.Moncrief','size':2},
{'name':'D.Allen','size':2},
{'name':'H.Nicks','size':1},
{'name':'D.Herron','size':1}],
[{'name':'O.Beckham Jr.','size':2},
{'name':'V.Cruz','size':2},
{'name':'R.Randle','size':2},
{'name':'R.Jennings','size':1},
{'name':'D.Fells','size':1},
{'name':'L.Donnell','size':1},
{'name':'A.Williams','size':1}],
[{'name':'D.Thomas','size':8},
{'name':'J.Thomas','size':3},
{'name':'E.Sanders','size':3},
{'name':'W.Welker','size':3},
{'name':'J.Tamme','size':1}],
[{'name':'A.Gates','size':4},
{'name':'L.Green','size':3},
{'name':'K.Allen','size':2},
{'name':'E.Royal','size':2},
{'name':'M.Floyd','size':2},
{'name':'D.Inman','size':1},
{'name':'B.Oliver','size':1}],
[{'name':'R.Cobb','size':3},
{'name':'J.Nelson','size':2},
{'name':'D.Adams','size':2},
{'name':'R.Rodgers','size':1},
{'name':'A.Quarless','size':1},
{'name':'E.Lacy','size':1}],
[{'name':'A.Brown','size':5},
{'name':'M.Bryant','size':2},
{'name':'L.Bell','size':2},
{'name':'M.Spaeth','size':1},
{'name':'H.Miller','size':1},
{'name':'L.Moore','size':1}],
[{'name':'J.Jones','size':8},
{'name':'R.White','size':3},
{'name':'L.Toilolo','size':1},
{'name':'D.Hester','size':1}],
[{'name':'C.Johnson','size':2},
{'name':'R.Bush','size':2},
{'name':'J.Fauria','size':1},
{'name':'G.Tate','size':1}],
[{'name':'L.Willson','size':4},
{'name':'D.Baldwin','size':2},
{'name':'R.Lockette','size':2},
{'name':'J.Kearse','size':2},
{'name':'C.Helfet','size':1}]
]
}
]


LocBreakoutNames = []
for kk in LocBreakouts:
	LocBreakoutNames.append(kk['name'])

ZeroInd = 0
for ii in Location['children']:
	qbLoc = qbs.index(ii['name'])
	ind = 0
	for kk in ii['children']:
		LocInd = LocBreakoutNames.index(ii['children'][ind]['name'])
		kk['name'] = kk['name'] + "_"+str(round(10000*r.random()))
		kk['children'] = LocBreakouts[LocInd]['children'][qbLoc]
		Location['children'][qbLoc]['children'][ind] = kk
		ind += 1
		for d in kk['children']:
			d['name'] = d['name'] + "_"+str(round(10000*r.random()))

smallTest = {'name':'QBs','children':[]}
trim_to = 3
for ii in range(trim_to):
	smallTest['children'].append(Location['children'][qbs[ii]])

with open('ice_qb_location_target.json','w') as w:
    json.dump(Location,w)

with open('ice_qb_location_target_smalTest.json','w') as w:
    json.dump(smallTest,w)    