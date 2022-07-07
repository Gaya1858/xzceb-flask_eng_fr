import unittest

from translator import englishtofrench, frenchtoenglish

   

class TestEnglishToFrench(unittest.TestCase):

    def test1(self):
       #self.assertEqual(frenchtoenglish(None),'')
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')

class FrenchToEnglish(unittest.TestCase):

    def test2(self):
        #self.assertEqual(englishtofrench(None),'')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

if __name__ == '__main__':
    unittest.main()