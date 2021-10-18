import unittest

from unittest.mock import patch
from app import start


class TestMethods(unittest.TestCase):
    @patch("builtins.input", side_effect=["55", "12N", "LMLMLMLMM", "S"])
    def test_start(self, mock):
        self.plateau = start()
        self.assertEqual(1, len(self.plateau.rovers))


if __name__ == "__main__":
    unittest.main()
