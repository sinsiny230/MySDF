def CountMol (inputfile):
	inf = open(inputfile)
	count = 0
	for line in inf:
		if '$$$$' in line :
			count = count +1
	return count


def CutSDF(inputfile,outfile,n):
	inf = open(inputfile)
	outf = open(outfile,'w')
	count = 0
	sdf = ''
	for line in inf :
		sdf = sdf + line
		if '$$$$' in line :
			count = count + 1
			outf.write(sdf)
			sdf = ''
		if count == n :
			break


def GetID(inputfile):
	inf = open(inputfile)
	sdf = ''
	mol = []
	ID = []
	for line in inf :
		sdf = sdf + line
		if '$$$$' in line :
			mid = sdf.split('\n')[0]
			ID.append(mid)
			sdf = ''
			mid = []
	return ID


def RemoveInfo(inputfile,outfile):
	inf = open(inputfile)
	outf = open(outfile,'w')
	sdf = ''
	for line in inf :
		sdf = sdf + line
		if '$$$$' in line :
			sdf = sdf.split('M  END')[0]
			sdf = sdf + 'M END\n' +'$$$$\n'
			outf.write(sdf)
			sdf = ''
