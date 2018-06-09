import unittest
from soldier import Soldier

class TestEligibility(unittest.TestCase):
	candidate1=Soldier(23)
	candidate2=Soldier(17)
	candidate3=Soldier(25)
	candidate4=Soldier(18)
	
	def test_one(self):
		self.assertEqual(self.candidate1.checkagelimit(),True)
	def test_two(self):
		self.assertEqual(self.candidate2.checkagelimit(),False)	
	def test_three(self):
		self.assertEqual(self.candidate3.checkagelimit(),True)
	def test_four(self):
		self.assertEqual(self.candidate4.checkagelimit(),False)
		
if __name__=="__main__":
	unittest.main()