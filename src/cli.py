import sys
from calculator import calculate_sum


def main():
    if len(sys.argv) != 3:
        print("Usage: python cli.py <number1> <number2>")
        sys.exit(1)
    
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        result = calculate_sum(a, b)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Both arguments must be valid numbers")
        sys.exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
