def is_prime(number):
    """Determine whether a number is a prime number."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Example
number_to_test = 29
if is_prime(number_to_test):
    print(f"{number_to_test} is a prime number.")
else:
    print(f"{number_to_test} is not a prime number.")