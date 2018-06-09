def twofunc():
		print("*******this is two.py******")
		print("name is",__name__)
if __name__=="__main__":
	twofunc()
else:
	print("not in main")