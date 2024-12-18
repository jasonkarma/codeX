try:
    num = int(input("Enter a positive number: "))
    if num > 100:
        raise ValueError("Numbers higher than 100 are not allowed!")
    print(f"You entered: {num}")
    if num < 0:
        raise ValueError("Negative numbers are not allowed!")
    print(f"You entered: {num}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Program execution complete.")
