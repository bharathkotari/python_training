#files

#writing to a file
'''
myfile1=open("zebracaution.txt","w")
myfile1.write("don't mess with the killer zebra \n it's kind of mad")
myfile1.close()

#reading from a file
myfile2=open("zebracaution.txt","r+")
print(myfile2.read(100))
myfile2.close()
#anotherway
with open("zebracaution.txt",'r+') as f:
	f.write("  hello")
	print(f.read(100))  # no need to close the file here'''
	
#reading and writingchunk data

#reading from a image file

mychunk=1000
myimg='h.jpg'
dummyfile=open('chunkfile.txt','wb+')
with open(myimg,'rb') as fileloop:
	while(True):
		filelines=fileloop.read(mychunk)
		dummyfile.write(filelines)
		if not filelines:break
dummyfile.close()
#for wiriting to a file	
readdummy=open("chunkfile.txt",'rb')

with open('six.jpg','wb') as tempfile:
	for f in readdummy:
		tempfile.write(f)
readdummy.close()