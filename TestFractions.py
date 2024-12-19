import unittest
from TP7 import Fraction

class TestFraction(unittest.TestCase):

    def test_initialization(self):
        # Positive numerator and denominator
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(Fraction(3, 4).numerator, 3)
        self.assertEqual(Fraction(3, 4).denominator, 4)
        # Negative numerator
        self.assertEqual(str(Fraction(-3, 4)), "-3/4")
        self.assertEqual(str(Fraction(-2, 3)), "-2/3")
        # Negative denominator
        self.assertEqual(str(Fraction(3, -4)), "-3/4")
        self.assertEqual(str(Fraction(2, -3)), "-2/3")
        # Zero numerator
        self.assertEqual(str(Fraction(0, 5)), "0")
        # Reduction of fractions
        self.assertEqual(str(Fraction(6, 8)), "3/4")
        # Negative numerator and denominator
        self.assertEqual(str(Fraction(-3, -4)), "3/4")
        # Fraction equal to integer
        self.assertEqual(str(Fraction(8, 4)), "2")

    def test_as_mixed_number(self):
        # Proper fraction
        self.assertEqual(Fraction(3, 4).as_mixed_number(), "3/4")
        # Improper fraction
        self.assertEqual(Fraction(7, 4).as_mixed_number(), "1 + 3/4")
        # Whole number
        self.assertEqual(Fraction(8, 4).as_mixed_number(), "2")
        # Negative improper fraction
        self.assertEqual(Fraction(-7, 4).as_mixed_number(), "-1 + 3/4")
        # Negative proper fraction
        self.assertEqual(Fraction(-3, 4).as_mixed_number(), "-3/4")
        # Zero fraction
        self.assertEqual(Fraction(0, 1).as_mixed_number(), "0")

    def test_addition(self):
        # Adding positive fractions
        self.assertEqual(str(Fraction(1, 4) + Fraction(1, 4)), "1/2")
        # Adding negative fractions
        self.assertEqual(str(Fraction(-1, 4) + Fraction(-1, 4)), "-1/2")
        # Adding fractions with different denominators
        self.assertEqual(str(Fraction(1, 3) + Fraction(1, 6)), "1/2")
        # Adding a fraction and zero
        self.assertEqual(str(Fraction(1, 4) + Fraction(0, 1)), "1/4")
        # Adding an integer to a fraction
        self.assertEqual(str(Fraction(1, 4) + Fraction(4, 4)), "5/4")
        # Adding fractions leading to an integer
        self.assertEqual(str(Fraction(1, 2) + Fraction(1, 2)), "1")
        # Adding opposite fractions
        self.assertEqual(str(Fraction(1, 4) + Fraction(-1, 4)), "0")

    def test_subtraction(self):
        # Subtracting positive fractions
        self.assertEqual(str(Fraction(1, 2) - Fraction(1, 4)), "1/4")
        # Subtracting negative fractions
        self.assertEqual(str(Fraction(-1, 2) - Fraction(-1, 4)), "-1/4")
        # Subtracting a larger fraction from a smaller fraction
        self.assertEqual(str(Fraction(1, 4) - Fraction(1, 2)), "-1/4")
        # Subtracting zero
        self.assertEqual(str(Fraction(1, 4) - Fraction(0, 1)), "1/4")
        # Subtracting a fraction from itself
        self.assertEqual(str(Fraction(3, 5) - Fraction(3, 5)), "0")
        # Subtracting fractions with reduction
        self.assertEqual(str(Fraction(3, 4) - Fraction(1, 4)), "1/2")
        # Subtracting fractions with opposite signs
        self.assertEqual(str(Fraction(1, 4) - Fraction(-1, 4)), "1/2")

    def test_multiplication(self):
        # Multiplying positive fractions
        self.assertEqual(str(Fraction(1, 2) * Fraction(2, 3)), "1/3")
        # Multiplying negative fractions
        self.assertEqual(str(Fraction(-1, 2) * Fraction(-2, 3)), "1/3")
        # Multiplying a fraction by zero
        self.assertEqual(str(Fraction(1, 2) * Fraction(0, 1)), "0")
        # Multiplying a positive and a negative fraction
        self.assertEqual(str(Fraction(1, 2) * Fraction(-2, 3)), "-1/3")
        # Multiplying a fraction by 1
        self.assertEqual(str(Fraction(1, 3) * Fraction(1, 1)), "1/3")
        # Multiplying leading to a whole number
        self.assertEqual(str(Fraction(3, 4) * Fraction(4, 3)), "1")
        # Multiplying with reduction
        self.assertEqual(str(Fraction(2, 4) * Fraction(4, 6)), "1/3")

    def test_division(self):
        # Dividing positive fractions
        self.assertEqual(str(Fraction(1, 2) / Fraction(2, 3)), "3/4")
        # Dividing negative fractions
        self.assertEqual(str(Fraction(-1, 2) / Fraction(-2, 3)), "3/4")
        # Dividing a positive by a negative fraction
        self.assertEqual(str(Fraction(1, 2) / Fraction(-2, 3)), "-3/4")
        # Dividing by 1
        self.assertEqual(str(Fraction(1, 2) / Fraction(1, 1)), "1/2")
        # Dividing a fraction by itself
        self.assertEqual(str(Fraction(3, 4) / Fraction(3, 4)), "1")
        # Dividing fractions leading to a reduced form
        self.assertEqual(str(Fraction(6, 8) / Fraction(3, 4)), "1")
        # Attempting to divide by zero
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_power(self):
        # Positive power
        self.assertEqual(str(Fraction(2, 3) ** 2), "4/9")
        # Zero power
        self.assertEqual(str(Fraction(2, 3) ** 0), "1")
        # Negative power
        self.assertEqual(str(Fraction(2, 3) ** -1), "3/2")
        # Power of a negative fraction
        self.assertEqual(str(Fraction(-2, 3) ** 2), "4/9")
        self.assertEqual(str(Fraction(-2, 3) ** 3), "-8/27")
        # Fraction raised to 1
        self.assertEqual(str(Fraction(3, 4) ** 1), "3/4")
        # Power of 0
        self.assertEqual(str(Fraction(0, 1) ** 3), "0")
        # Negative power of a negative fraction
        self.assertEqual(str(Fraction(-2, 3) ** -1), "-3/2")

    def test_properties(self):
        # Zero fraction
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 3).is_zero())
        # Integer fraction
        self.assertTrue(Fraction(6, 3).is_integer())
        self.assertFalse(Fraction(7, 3).is_integer())
        # Proper fraction
        self.assertTrue(Fraction(1, 3).is_proper())
        self.assertFalse(Fraction(4, 3).is_proper())
        # Unit fraction
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        # Adjacent fractions
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 4)))
        self.assertFalse(Fraction(2, 3).is_adjacent_to(Fraction(1, 8)))
        # Integer and adjacent fraction
        self.assertTrue(Fraction(1, 1).is_adjacent_to(Fraction(1, 2)))
        self.assertFalse(Fraction(2, 1).is_adjacent_to(Fraction(1, 3)))

    def test_initialization_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_addition_with_invalid_operand(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + 3  # Addition avec un entier

    def test_subtraction_with_invalid_operand(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) - "1/2"  # Soustraction avec une chaîne

    def test_multiplication_with_invalid_operand(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * None  # Multiplication avec None

    def test_division_with_invalid_operand(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) / [1, 2]  # Division avec une liste

    def test_power_with_non_integer(self):
        with self.assertRaises(ValueError):
            Fraction(1, 2) ** 0.5  # Puissance non entière

    def test_float_conversion(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)
        self.assertEqual(float(Fraction(0, 1)), 0.0)

if __name__ == "__main__":
    unittest.main()
