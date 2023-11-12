import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


def Capture_output(r, flag=0):
    captured = StringIO()
    sys.stdout = captured
    if flag > 0:
        print(r)
    else:
        r.display()
    sys.stdout = sys.__stdout__
    return captured.getvalue()


class Test_Rectagnle_Initilze(unittest.TestCase):
    def test_rectangle_id(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, 12).id, 12)

    def test_multiy_id(self):
        r3 = Rectangle(11, 5)
        r4 = Rectangle(5, 8)
        self.assertEqual(r3.id, r4.id - 1)

    def test_All_args(self):
        self.assertEqual(Rectangle(2, 4, 1, 2, 5).id, 5)


class Test_Rectangle_Width(unittest.TestCase):
    def test_width_getter(self):
        self.assertEqual(Rectangle(4, 7).width, 4)

    def test_width_setter(self):
        r1 = Rectangle(4, 7)
        r1.width = 12
        self.assertEqual(r1.width, 12)

    def test_width_Vaild(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Vaild", 4)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_width_under_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def test_width_setter_TypeError(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).width = ["hello"]


class Test_Rectangle_height(unittest.TestCase):
    def test_height_getter(self):
        self.assertEqual(Rectangle(2, 3).height, 3)

    def test_height_setter(self):
        r1 = Rectangle(33, 22)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_height_vaild(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "vaild")

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, True)

    def test_height_underzero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -1)

    def test_height_setter_TypeError(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 4).height = [12, 23]


class Test_Rectangle_x(unittest.TestCase):
    def test_x_getter(self):
        self.assertEqual(Rectangle(2, 3, 2).x, 2)

    def test_x_setter(self):
        r1 = Rectangle(33, 22)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_x_vaild(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, None)

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, True)

    def test_x_underzero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -1)

    def test_x_setter_TypeError(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 4).x = [12, 23]


class Test_Rectagnle_Area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Rectangle(12, 2).area(), 24)


class Test_Rectanlge_output(unittest.TestCase):
    def test_display(self):
        result = ("#" * 4 + "\n") * 3
        test = Capture_output(Rectangle(4, 3))
        self.assertEqual(result, test)

    def test_rectangle_str(self):
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        test = Capture_output(Rectangle(4, 6, 2, 1, 12), 1)
        self.assertEqual(result, test)

    def test_display_XY(self):
        result = ("\n" * 2) + ((" " * 3 + "#" * 2 + "\n") * 5)
        test = Capture_output(Rectangle(2, 5, 3, 2))
        self.assertEqual(result, test)

    def test_display_xY(self):
        result = ("\n" * 2) + ("#" * 2 + "\n") * 5
        test = Capture_output(Rectangle(2, 5, 0, 2))
        self.assertEqual(result, test)

    def test_display_Xy(self):
        result = (" " * 3 + "#" * 2 + "\n") * 5
        test = Capture_output(Rectangle(2, 5, 3, 0))
        self.assertEqual(result, test)

    def test_update(self):
        r1 = Rectangle(11, 4)
        r1.update(4, 3, 2)
        self.assertEqual(r1.id, 4)

    def test_update_not(self):
        r1 = Rectangle(2, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(2, "vaild")
