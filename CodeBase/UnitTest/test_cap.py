import unittest
import cap

class TestCap(unittest.TestCase):
	def test_single_word(self):
		text = "python"
		result = cap.cap_text(text)
		self.assertEqual(result, "Python")

	def test_multiple_word(self):
		text = "jupyter notebook"
		result = cap.cap_text(text)
		self.assertEqual(result,"Jupyter Notebook")

if __name__ == "__main__":
	unittest.main()