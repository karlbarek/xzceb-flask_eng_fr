import unittest

from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        result = english_to_french(english_text)
        self.assertEqual(result, "Bonjour")

    def test_null_english_to_french(self):
        invalid_text = "Invalid Input"
        result = english_to_french("")
        self.assertEqual(result, invalid_text)

    def test_french_to_english(self):
        french_text = "Bonjour"
        result = french_to_english(french_text)
        self.assertEqual(result, "Hello")

    def test_null_french_to_english(self):
        invalid_text = "Invalid Input"
        result = french_to_english("")
        self.assertEqual(result, invalid_text)

if __name__ == '__main__':
    unittest.main()