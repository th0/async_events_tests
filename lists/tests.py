from django.test import TestCase

class FakeTest(TestCase):
	def test_something_stupid(self):
		self.assertEqual(2*4,19)
# Create your tests here.
