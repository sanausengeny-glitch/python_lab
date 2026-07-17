from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    value = input("Enter a number: ")
    try:
        number = float(value)
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Square: {square(number)}")
    print(f"Even: {is_even(number)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number):.2f}")
    print(greet("Student"))


if __name__ == "__main__":
    main()

