class Soldier:
	def __init__(self,candidateage):
		self.joiningage=candidateage
	def checkagelimit(self):
		if 18<self.joiningage<25:
			return True
		else:
			return False