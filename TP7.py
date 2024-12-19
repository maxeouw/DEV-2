from math import gcd


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.
        PRE: None
        POST : The fraction is stored in its reduced form with a positive denominator.
        RAISES : Sets an error if the denominator is zero
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(num, den)
        self.__numerator = num // common_divisor
        self.__denominator = abs(den // common_divisor)
        if den < 0:
            self.__numerator = -self.__numerator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction
        PRE: None
        POST : Returns a string in the form "numerator/denominator" or "numerator" if the denominator is equal to 1.
        """
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction
        PRE: None
        POST : Returns a string in the form "integer + proper_fraction" (or "integer" if the remainder equals zero) if the fraction is improper.
        """
        if self.numerator == 0:
            return "0"  # Special case for zero

        abs_numerator = abs(self.numerator)
        integer_part = abs_numerator // self.denominator
        remainder = abs_numerator % self.denominator

        if remainder == 0:
            return str(self.numerator // self.denominator)  # Whole number

        sign = "-" if self.numerator < 0 else ""
        if integer_part == 0:
            return f"{sign}{remainder}/{self.denominator}"  # Proper fraction
        return f"{sign}{integer_part} + {remainder}/{self.denominator}"  # Mixed number
    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions
        PRE: None
        POST : Returns a fraction representing a sum.
        RAISES : raises an error if the other operand is not a Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("The other operand must be a fraction")
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions
        PRE: None
        POST : Returns a new Fraction representing the difference.
        RAISES : raises an error if the other operand is not a Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("The other operand must be a fraction")
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions
        PRE: None
        POST : Returns a new Fraction representing the product.
        RAISES : raises an error if the other operand is not a Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("The other operand must be a fraction")
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE: None
        POST : Returns a new Fraction representing the division.
        RAISES : Raises a ZeroDivisionError if the other fraction has a numerator of 0.
        """
        if not isinstance(other, Fraction):
            raise TypeError("The other operand must be a fraction")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with a numerator of 0.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions
        PRE: None
        POST : Returns a new Fraction representing the power.
        RAISES: raises an error if the power is not an integer.
        """
        if not isinstance(power, int):
            raise ValueError("The power must be an integer.")
        if power >= 0:
            return Fraction(self.numerator ** power, self.denominator ** power)
        return Fraction(self.denominator ** abs(power), self.numerator ** abs(power))

    def __eq__(self, other):
        """Overloading of the == operator for fractions
        PRE: None
        POST : Returns True if the two fractions are equal.
        RAISES : raises an error if the other operand is not a fraction
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction
        PRE: None
        POST : Returns the decimal value of the fraction.
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0
        PRE: None
        POST : Verifies if the fraction's value is 0 by checking if the numerator is equal to 0.
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)
        PRE: None
        POST : Verifies if the rest of the division is equal to zero.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1
        PRE: None
        POST : Verifies if the absolute value of the numerator is smaller than the denominator.
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form
        PRE: None
        POST : Verifies if the numerator is equal to 1.
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction
        PRE: None
        POST : Checks if  the numerator of the absolute value of the difference is equal to 1 and if its denominator is equal to zero
        RAISES : raises an error if the other operand is not a fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("The other operand must be a Fraction.")
        diff = self - other
        return diff.is_unit()
