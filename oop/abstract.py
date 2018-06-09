from abc import ABC,abstractmethod

class Restaurant(ABC):
	count=10
	@abstractmethod
	def dininghall(self):
		print("this is in main abstract class Restaurant")
class Fivestar(Restaurant):
	def dininghall(self):
		print("it has 1000peoplecapasity")
	def swmmingpool(self):
		print("it has swimming pool")
class BeachsideResort(Restaurant):
	def dininghall(self):
		print("it has 100peoplecapasity")
	def beachsidecafe(self):
		print("yes it has beachside cafe")
		
fs=Fivestar()
fs.swmmingpool()
fs.dininghall()
br=BeachsideResort()
br.beachsidecafe()

br.count=20
print(br.count)
print(fs.count)
