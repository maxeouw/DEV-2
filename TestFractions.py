import unittest
from TP7 import Fraction

class TestFraction(unittest.TestCase):
    def test_constructor(self):
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-3, 4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(3, -4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        f = Fraction(-3, -4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str_and_as_mixed_number(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

        f = Fraction(4, 1)
        self.assertEqual(str(f), "4")

        f = Fraction(7, 4)
        self.assertEqual(f.as_mixed_number(), "1 + 3/4")

        f = Fraction(8, 4)
        self.assertEqual(f.as_mixed_number(), "2")

        f = Fraction(3, 4)
        self.assertEqual(f.as_mixed_number(), "3/4")

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result, Fraction(5, 6))

        f1 = Fraction(3, 4)
        f2 = Fraction(-1, 4)
        result = f1 + f2
        self.assertEqual(result, Fraction(1, 2))

    def test_division(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        result = f1 / f2
        self.assertEqual(result, Fraction(3, 2))

        f1 = Fraction(3, 4)
        f2 = Fraction(-1, 4)
        result = f1 / f2
        self.assertEqual(result, Fraction(-3, 1))

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_equality(self):
        self.assertTrue(Fraction(3, 4) == Fraction(6, 8))
        self.assertFalse(Fraction(3, 4) == Fraction(2, 4))
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(-1, 2))

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertTrue(Fraction(0, 5).is_integer())
        self.assertFalse(Fraction(3, 4).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(3, 4).is_proper())
        self.assertFalse(Fraction(5, 4).is_proper())
        self.assertTrue(Fraction(-1, 2).is_proper())

    def test_is_adjacent_to(self):
        self.assertFalse(Fraction(3, 4).is_adjacent_to(Fraction(5, 4)))
        self.assertTrue(Fraction(3, 4).is_adjacent_to(Fraction(2, 4)))
        self.assertTrue(Fraction(3, 4).is_adjacent_to(Fraction(1, 2)))


if __name__ == "__main__":
    unittest.main()
