import json
import re

WizPlayers = [
'Wall, John',
'Beal, Bradley',
'Pierce, Paul',
'Sessions, Ramon',
'Miller, Andre',
'Butler, Rasual',
'Temple, Garrett',
'Porter, Otto',
'Hilario, Nene',
'Gooden, Drew',
'Humphries, Kris',
'Webster, Martell',
'Bynum, Will',
'Gortat, Marcin',
'Seraphin, Kevin',
'Blair, DeJuan',
'Murry, Toure',
'Rice Jr., Glen',
]

for ii in WizPlayers:
	WizPlayers[WizPlayers.index(ii)] = ii.split(',')[1]+' '+ii.split(',')[0]

stats = {'Drives':[567,	225,	159,	109,	107,	53,	40,	36,	30,	29,	27,	17,	16,	11,	6,	2,	1,	1],
'Drives Per 36':[7.2,	3.8,	3,	7.2,	6.1,	1.3,	2,	0.9,	0.6,	1.2,	0.7,	1.7,	8.6,	0.2,	0.2,	0.4,	2.1,	0.8],
'Points':[329,	136,	109,	75,	75,	47,	10,	28,	27,	16,	13,	9,	8,	6,	4,	0,	2,	0],
'Player PPD': [0.58,	0.6,	0.69,	0.69,	0.7,	0.89,	0.25,	0.78,	0.9,	0.55,	0.48,	0.53,	0.5,	0.55,	0.67,	0,	2,	0],
'Team Points': [678,	254,	193,	117,	113,	61,	37,	43,	37,	26,	29,	9,	16,	8,	9,	4,	2,	0],
'Team PPP':[1.22,	1.13,	1.24,	1.08,	1.11,	1.15,	0.93,	1.19,	1.28,	0.93,	1.07,	0.53,	1.07,	0.73,	1.5,	2,	2,	0],
'FTR':[0.487,	0.262,	0.763,	0.83,	0.186,	0.469,	0.235,	0.25,	0.158,	0.125,	0.188,	1.5,	0,	0.5,	0,	0,	0,	0],
'Shot %': [0.395,	0.542,	0.371,	0.431,	0.551,	0.604,	0.425,	0.667,	0.633,	0.552,	0.593,	0.353,	0.375,	0.364,	0.333,	0.5,	1,	1],
'FG %':[0.491,	0.426,	0.542,	0.383,	0.542,	0.5,	0.176,	0.458,	0.632,	0.438,	0.313,	0,	0.667,	0.5,	1,	0,	1,	0],
'Ast %': [0.148,	0.044,	0.119,	0.119,	0.056,	0.057,	0.125,	0.083,	0.1,	0.103,	0.037,	0,	0.188,	0,	0,	0,	0,	0],
'TO %': [0.06,	0.076,	0.113,	0.092,	0.047,	0.075,	0.1,	0.028,	0.1,	0,	0,	0.118,	0.188,	0.273,	0.333,	0,	0,	0],
'Foul %': [0.139,	0.102,	0.208,	0.257,	0.103,	0.208,	0.125,	0.139,	0.167,	0.069,	0.148,	0.471,	0,	0.091,	0,	0,	0,	0]}


WizStats = {}

for ii in WizPlayers:	
	WizStats[ii] = {}
	for ss in stats:
		if re.search(r'%',ss):
			WizStats[ii][ss] = round(100*stats[ss][WizPlayers.index(ii)],1)
		# else:
		# 	WizStats[ii][ss] = stats[ss][WizPlayers.index(ii)]

with open('WizStats.json','w') as a: 
	json.dump(WizStats,a)

with open('WizStats.csv','w') as a:
	cc = csv.writer(a)
	head = ['Player']
	for ii in stats:
		head.append(ii)
	cc.writerow(head)
	for pp in WizStats:
		line=[pp.split(",")[1]+" "+pp.split(",")[0]]
		for ss in stats:
			line.append(WizStats[pp][ss])
		cc.writerow(line)