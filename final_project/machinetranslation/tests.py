import unittest
import translator

class TestTranslationMethods(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench(None), '')
        self.assertEqual(translator.englishToFrench("Hello"), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish(None), '')
        self.assertEqual(translator.frenchToEnglish("Bonjour"), 'Hello')

 if __name__ == '__main__':
    unittest.main()
