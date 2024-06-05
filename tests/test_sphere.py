import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from foo.sphere import calculate_volume_of_sphere

class TestSphereVolume(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(calculate_volume_of_sphere(1), 4.1887902047863905)
        self.assertAlmostEqual(calculate_volume_of_sphere(0), 0)
        self.assertAlmostEqual(calculate_volume_of_sphere(2.5), 65.44984694978736)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_sphere(-1)

if __name__ == '__main__':
    unittest.main()