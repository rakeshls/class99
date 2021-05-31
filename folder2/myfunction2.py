def readfile():
	fname=input("enter file name:")
	file=open(fname,'r')
	f=file.read()
	print(f)
	words=0
	nw=0
	for i in f:
		words=i.split()
		nw=nw+len(words)
	print(nw)
readfile()