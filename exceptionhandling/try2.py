# custom exceptions
class Error(Exception):
	pass
class SmallNumber(Error):
	def raiseexception(self):
		print("im inside small number classs")
		
class BigNumber(Error):
	def raiseexception(self):
		print("inside big number class")
	
number = 15
while(1):
	try:
		num=int(input("enter a number\n"))
		if num<number:
			raise SmallNumber
		elif num>number:
			raise BigNumber
		break
	except SmallNumber:
		print("this value is too small")
		k=SmallNumber()
		k.raiseexception()
	except BigNumber:
		print("this value is big")
		k=BigNumber()
		k.raiseexception()
print("guess is 15")