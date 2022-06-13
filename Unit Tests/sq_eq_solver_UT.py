import unittest
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(findRoots(2,2,2),"No Roots")
        self.assertAlmostEqual(findRoots(1,5,1),(-0.208,-4.79))
