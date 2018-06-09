import unittest
from one import *

class MyTestClassName(unittest.TestCase):
	def test_unittest1(self):
		self.assertEqual(checkfunction1(16,12),True)
		self.assertEqual(checkfunction1(5,12),False)
		self.assertEqual(checkfunction1(7,12),False)
		self.assertEqual(checkfunction1(6,12),False)
		
		
	def test_unittest2(self):
		self.assertEqual(checkfunction2("Everyday"),True)
		self.assertEqual(checkfunction2("ey"),False)
	def test_unittest3(self):
		self.assertEqual(checkfunction3("aaEveryday"),True)


		
		
if __name__=="__main__":
	unittest.main()