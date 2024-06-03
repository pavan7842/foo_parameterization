import unittest
from foo.sphere import calculate_volume

class TestSphereVolume(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.1587902047863905)
        self.assertAlmostEqual(calculate_volume(0), 0)
        self.assertAlmostEqual(calculate_volume(2.5), 64.44984694978735)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

if __name__ == '__main__':
    unittest.main()
