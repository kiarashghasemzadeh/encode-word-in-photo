def encode(infilename,outfilename,word):
	infile = open(infilename,'rb')
	out = open (outfilename, 'wb')
	n = 0 
	size = 500
	e = len(word)
	#buffer =infile.read(size)
	#outfile.write(buffer)
	#outfile.write(str(e))
	while len(buffer) != 0:
		buffer = infile.read(size)
		outfile.write(buffer)
		#if n < e :
			#oufile.write(word[n])
		#n = n + 1
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
		print ( m , outfile)
		n = n + 1 
infilename = raw_input('enter your filename:')
outfilename = raw_input('enter your outfile name:')
word = raw_input('enter your word:')
encode(infilename,outfilename,word)

