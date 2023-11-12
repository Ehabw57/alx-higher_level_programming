import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_None(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_multyID(self):
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base15 = Base(15)
        self.assertEqual(base15.id, 15)


if __name__ == "__main__":
    unittest.main()
