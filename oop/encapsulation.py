class restaurant():
	def __kitchen(self):
		print("you can access the kitchen")
	def staffmember(self,access):
		if access:
			self.__kitchen()
		else:
			print("access denied")
	
rest=restaurant()
accesscheck=int(input("are you a cook ? enter 1 or 0"))
rest.staffmember(accesscheck)
rest.__kitchen()