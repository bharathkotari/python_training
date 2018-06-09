class Travel():
	def booktcket(self,lst):
		raise NotImplementedError("subclass must implement abstract method")
		
class BusinessTravel(Travel):
	def booktcket(self,lst):
		print("i needto book %d   tickets"%lst[0])
class PleasureTravel(Travel):
	def booktcket(self,lst):
		print("i need to book %d tickets"%lst[0])
		print("i need ti book %d rooms"%lst[1])

bt=BusinessTravel()
bt.booktcket([2])
pt=PleasureTravel()
pt.booktcket([4,2])