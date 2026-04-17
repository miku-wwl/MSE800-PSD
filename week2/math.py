import math

def basic_arithmetic(a, b) -> None:
    print("Basic Arithmetic Operations:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} % {b} = {a % b}")
    print()

def basic_power(x, y) -> None:
    print("Basic Power Operations:")
    print(f"{x} ** {y} = {x ** y}")
    print(f"pow({x}, {y}) = {pow(x, y)}")
    print()

def basic_log(x, base) -> None:
    print("Basic Logarithm Operations:")
    print(f"log({x}, {base}) = {math.log(x, base)}")
    print()

def basic_factorial(n) -> None:
    print("Factorial Function:")
    try:
        result = math.factorial(n)
        print(f"factorial({n}) = {result}")
    except (ValueError, TypeError) as e:
        print(f"factorial({n}) -> Error: {e}")
    print()
    
def basic_complex_operations() -> None:
    print("Complex Number Operations:")
    c1 = 3 + 4j
    c2 = 1 + 2j
    
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    
    print(f"c1 + c2 = {c1 + c2}")
    print(f"c1 - c2 = {c1 - c2}")
    print(f"c1 * c2 = {c1 * c2}")
    print(f"c1 / c2 = {c1 / c2}")
    print()

def main() -> None:
    basic_arithmetic(10, 5)
    basic_power(2, 3)
    basic_log(100, 10)
    basic_factorial(5)
    basic_complex_operations()

if __name__ == "__main__":
    main()