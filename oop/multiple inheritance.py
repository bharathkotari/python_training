#Method Resolution Order

class A1():
	#def who_am_i(self):
	#	print("im A1")
	pass
class A2():pass
	#def who_am_i(self):
	#	print("im A2")
		
class A3():
	def who_am_i(self):
		print("im A3")
		
class B(A1,A2):
	#def who_am_i(self):
	#	print("im B")
	pass
	
class C(A3):
	def who_am_i(self):
		print("im c")
		
class D(B,C):
	#def who_am_i(self):
	#	print("im D")
	pass
	
	
d1=D()
d1.who_am_i()


#getter and setter 

class Book():
	def __init__(self,name):
		self.__name=name
	
	#getter method
	@property
	def bookname(self):
		return self.__name
	#setter Method
	@bookname.setter
	def bookname(self,newname):
		self.__name=newname

b1=Book("harry potter")
print(b1.bookname)
b1.bookname="avengers"
print(b1.bookname)
