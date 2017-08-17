import unittest


def overtime(hours):
    """Calculate the amount of overtime payable per day.
    
    Args:
        hours (list): seven-element array of hours logged (ints) 
    
    Returns:
        list: seven-element array of overtime to be charged
    """
    pass


class TestOvertime(unittest.TestCase):

    def test_overtime(self):
        self.assertEqual(overtime([8, 8, 8, 8, 8, 0, 0]), [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(overtime([8, 8, 8, 8, 0, 8, 0]), [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(overtime([8, 8, 8, 8, 8, 8, 0]), [0, 0, 0, 0, 0, 8, 0])
        self.assertEqual(overtime([6, 6, 6, 6, 6, 12, 0]), [0, 0, 0, 0, 0, 2, 0])
        self.assertEqual(overtime([12, 8, 4, 8, 8, 2, 0]), [2, 0, 0, 0, 0, 0, 0])
        self.assertEqual(overtime([16, 16, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(overtime([6, 6, 6, 6, 6, 6, 6]), [0, 0, 0, 0, 0, 0, 2])
        self.assertEqual(overtime([8, 8, 8, 8, 8, 0, 0]), [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(overtime([10, 10, 10, 8, 7, 0, 0]), [2, 2, 1, 0, 0, 0, 0])
        self.assertEqual(overtime([0, 10, 10, 8, 7, 10, 0]), [0, 2, 2, 0, 0, 1, 0])

if __name__ == "__main__":
    unittest.main()
