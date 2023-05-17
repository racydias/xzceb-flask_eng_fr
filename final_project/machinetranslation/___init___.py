import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
        self.assertEqual(englishToFrench('How are you?'), 'Comment allez-vous?')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
        self.assertEqual(frenchToEnglish('Comment allez-vous?'), 'How are you?')

if __name__ == '__main__':
    unittest.main()