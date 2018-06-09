import one

print("****this is two.py****")
print("name is ",__name__)

if __name__=="__main__":
	print("two.py is being executed directly")
else:
	print("two.py is imported to othermodule")
one.func()