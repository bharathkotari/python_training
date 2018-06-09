
class Person():
	__name=""
	__age=0
	__cls=0
	def __init__(self,name,age,cls):
		self.__name=name
		self.__age=age
		self.__cls=cls
	def print_data(self):
		print(self.__name,"\n")
		print(self.__age,"\n")
		print(self.__cls,"\n")
	
n=input("enter the name\n")
age=int(input("enter age\n"))
cls=int(input("enter class\n"))

s=Person(n,age,cls)
s.print_data()