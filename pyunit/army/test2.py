import unittest
from soldier import Soldier

class TestEligibility2(unittest.TestCase):
	candidate11=Soldier(23)
	candidate12=Soldier(17)
	candidate13=Soldier(25)
	candidate14=Soldier(18)
	candidate15=Soldier(26)
	candidate16=Soldier(24)
	candidate17=Soldier(19)
	
	def test_one_abc(self):
		self.assertEqual(self.candidate11.checkagelimit(),True)
	def test_two_abc(self):
		self.assertEqual(self.candidate12.checkagelimit(),False)	
	def test_three_abc(self):
		self.assertEqual(self.candidate13.checkagelimit(),True)
	def test_four_abc(self):
		self.assertEqual(self.candidate14.checkagelimit(),False)
	def test_five_abc(self):
		self.assertEqual(self.candidate15.checkagelimit(),False)	
	def test_six_abc(self):
		self.assertEqual(self.candidate16.checkagelimit(),True)
	def test_seven_abc(self):
		self.assertEqual(self.candidate17.checkagelimit(),False)
	
		
if __name__=="__main__":
	unittest.main()