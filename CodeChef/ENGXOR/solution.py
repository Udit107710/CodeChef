from sys import stdin, stdout
from collections import defaultdict

for _ in range(int(stdin.readline())):
	n ,q = map(int ,stdin.readline().split())
	x = list(map( int ,stdin.readline().split()))

	
	mapp = defaultdict(int)
	
	for e in x:
		if(bin(e).count('1') %2 == 0):
			mapp['even'] += 1
		else:
			mapp['odd']  += 1
		
	for o in range(q):
		l = int(stdin.readline())
		
		
		if(bin(l).count('1') % 2 != 0):
			print(mapp['odd'], mapp['even'])
		else:
			print(mapp['even'], mapp['odd'])