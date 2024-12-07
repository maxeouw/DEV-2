from TP7 import Fraction

def main():
    # Fractionss
    f1 = Fraction(3, 4)
    f2 = Fraction(5, 8)
    f3 = Fraction(7, 4)  # (Improper fraction)
    f4 = Fraction(1, 3)  # (Unit fraction)

    print("=== Fractions Created ===")
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f3 = {f3} (improper)")
    print(f"f4 = {f4} (unit)")

    # Improper fractions
    print("\n=== Improper fraction ===")
    print(f"f3 as a mixed number: {f3.as_mixed_number()}")

    # Operations
    print("\n=== Arithmetic operations ===")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 ** 2 = {f1 ** 2}")
    print(f"f1 ** -1 (inverse) = {f1 ** -1}")

    # Properties
    print("\n=== Properties ===")
    print(f"Is f1 equal to zero ? {f1.is_zero()}")
    print(f"Is f1 an integer ? {f1.is_integer()}")
    print(f"Is f1 proper ? {f1.is_proper()}")
    print(f"Is f4 a unit fraction ? {f4.is_unit()}")

    # Comparison
    f5 = Fraction(3, 4)  # Eqtals to f1
    print("\n=== Comparaison ===")
    print(f"f1 == f5 ? {f1 == f5}")
    print(f"f1 == f2 ? {f1 == f2}")

    # Checking for adjacent fractions
    print("\n=== Adjacent Fractions ===")
    f6 = Fraction(1, 2)  # 1/2
    f7 = Fraction(1, 3)  # 1/3
    print(f"Is f6 adjacent to f7 ? {f6.is_adjacent_to(f7)}")
    print(f"Is f6 adjacent to f1 ? {f6.is_adjacent_to(f1)}")

if __name__ == "__main__":
    main()
