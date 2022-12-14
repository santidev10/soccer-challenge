import unittest
import challenge

class TestChallengy(unittest.TestCase):
    def test_main(self):
        result = challenge.main()
        expected = {'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0}
        self.assertEqual(result, expected)