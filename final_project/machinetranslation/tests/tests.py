import unittest
import translator

class TestTranslationMethods(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(translator.english_to_french(None), '')
        self.assertEqual(translator.english_to_french("Hello"), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(translator.french_to_english(None), '')
        self.assertEqual(translator.french_to_english("Bonjour"), 'Hello')

if __name__ == '__main__':
    unittest.main()
