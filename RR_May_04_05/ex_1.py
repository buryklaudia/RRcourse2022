import unittest
import sys

def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')

class TestConvert(unittest.TestCase):
    def test_example(self):
        self.assertEqual(convert(50, target='c'), 10)
        self.assertEqual(convert(70, target='c'), 21.1111111111111111)
        self.assertEqual(convert(90, target='c'), 32.2222222222222222)
        
    def test_Reaumur_scale(self):
        with self.assertRaises(Exception):
            convert(50, target = 'Reaumur')


if __name__ == '__main__':
    unittest.main()
 