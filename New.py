def	decode (filename,outname):
	infile = open(filename,'rb')
	outfile = open(outname,'a')
	size = 500
	sizew = 1
	n = 0 
	infile.read(size)
	lenE = infile.read(sizew)
	while n != lenE :
		infile.read(size)
		m = infile.read(sizew)
		print ( m )
		n = n + 1 
		m = raw_input()
filename = raw_input('enter your filename:')
outname = raw_input('enter your outfile name:')
decode(filename,outname)
