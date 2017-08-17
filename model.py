import numpy as np
i = 0
while(1):
	path_to_csv = "rightcsv/"+ input() + ".csv"
	data = np.genfromtxt(path_to_csv, dtype=None, delimiter=',', names=True)
	#print(data["time"])
	for j in data["motifs"]:
		if(j.decode("utf-8") == 'A'):
			print(j)
	#i += 1
	beta_closure = 1.0 #A,H,E,G,J,K,L
	beta_nonclosure = 10.0 #B,C,D,F,I,M,N,O,P
	closures = ['A','H','E','G','J','K','L']
	non_closrues = ['B','C','D','F','I','M','N','O','P']
	l = len(data["time"])
	maxx = np.floor(data["time"][l-1]) + 1
	effectvec = np.array([0.0]*16)
	recent = np.array([0.0]*16)
	#print(effectvec)
	
	j = 2
	time = data["time"][0]
	#while(np.floor(time) > j):
	#	j += 1
	print("1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0")
	for i in range(int(l)):
		#print(maxx)
		motif = data["motifs"][i].decode("utf-8")
		time = data["time"][i]
		#print(l)
		if(np.floor(time) >= j):
			while(np.floor(time) >= j):
				for k in range(len(effectvec)):
					if(motif in closures):
						effectvec[k] = -1 * beta_closure * (j - recent[k])
					else:
						effectvec[k] = -1 * beta_nonclosure * (j - recent[k])
				effectvec = np.around(np.exp(effectvec),6)
				lis = ','.join(map(str,effectvec))
				lis = str(j) +','+ lis
				print(lis)
				#print(str(j))
				j += 1
		
		recent[ord(motif) - ord('A')] = time
		#print(time,recent)
	for k in range(len(effectvec)):
		if(motif in closures):
			effectvec[k] = -1 * beta_closure * (j - recent[k])
		else:
			effectvec[k] = -1 * beta_nonclosure * (j - recent[k])
	effectvec = np.around(np.exp(effectvec),6)
	lis = ','.join(map(str,effectvec))
	lis = str(j) +','+ lis
	print(lis)

	break
