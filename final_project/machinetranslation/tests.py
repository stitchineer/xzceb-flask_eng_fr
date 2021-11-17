import unittest
import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
