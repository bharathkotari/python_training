class Animal():
	habitat='land'
	def __init__(self,animaltype,limbs,habitat,tail=1):# default constructor
		self.limbs=limbs
		self.animaltype=animaltype
		self.tail=tail
		self.habitat=habitat
	def animaldetails(self,color,hair,breed):
		print("color of the",self.animaltype,"is",color)
		print("hair of this",self.limbs,"limbed animal is",hair)
		print("breed of this",self.tail,"tail animal is",breed)

dog=Animal("dog",4,"water",1)
print(dog.limbs)
print(dog.tail)
print(dog.animaltype)
print(dog.habitat)
dog.animaldetails("brown","long","retriver")