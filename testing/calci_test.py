import unittest
from calci import add, sub, name
class testcalci(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_sub(self):
        self.assertNotEqual(sub(5,2),1)
    def test_name(self):
        self.assertEqual(name("monish"),"monishgowda")
if __name__=="__main__":
    unittest.main()