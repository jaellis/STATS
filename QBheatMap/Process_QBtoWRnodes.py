import csv
#	Convert csv from Oracle SQL to node format for D3.js
data=[]
with open('QBtoWRnode.csv','r') as cc:
	rr=csv.reader(cc)
	for line in rr:
		data.append(line)

head = data[0]

minQBR=100
maxQBR=0
qbTowr = dict()
for ii in data[1:]:
	if ii[0] not in qbTowr:
		qbTowr[ii[0]] = {}
	if ii[1] not in qbTowr[ii[0]]:
		qbTowr[ii[0]][ii[1]] = {}
		for hh in head[2:]:
			qbTowr[ii[0]][ii[1]][hh]=ii[head.index(hh)]
			if hh in 'QB_RATING':
				if float(ii[head.index(hh)]) > maxQBR:
				 	maxQBR = float(ii[head.index(hh)])
				if float(ii[head.index(hh)]) < minQBR:
					minQBR = float(ii[head.index(hh)])

test=[]
for ii in qbTowr:
	for hh in qbTowr[ii]:
		test.append({'qb':ii,'receiver':hh,'QBR':qbTowr[ii][hh]['QB_RATING'],'AirYards':qbTowr[ii][hh]['AVG_AIRYARDS'],'targets':qbTowr[ii][hh]['TARGETS'],'yac':qbTowr[ii][hh]['YDS_AFTER_CATCH']})

with open('QBtoWR.csv','w') as qb:
	cc = csv.writer(qb)
	cc.writerow(['source','target','rating','airyards','comps','yac'])
	for ii in test:
		line = []
		line.append(ii['qb'])
		line.append(ii['receiver'])
		line.append(ii['QBR'])
		line.append(ii['AirYards'])
		line.append(ii['targets'])
		line.append(ii['yac'])
		cc.writerow(line)