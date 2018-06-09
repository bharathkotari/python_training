def func():
	print("func() in one.py")
print("*****in one.py*******")
print("name is ",__name__)
if __name__=="__main__":
	print("one.py is being run directly")
else:
	print("one.py is imported into another module")
	