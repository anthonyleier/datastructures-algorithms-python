def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    return fibonacci(number-1) + fibonacci(number-2)


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)


if __name__ == "__main__":
    print(fibonacci(4))  # 3
    print(fibonacci(5))  # 5
    print(fibonacci(6))  # 8
    print(fibonacci(7))  # 13

    print(factorial(1))  # 1
    print(factorial(2))  # 2
    print(factorial(3))  # 6
    print(factorial(4))  # 24
    print(factorial(5))  # 120
    print(factorial(6))  # 720
    print(factorial(7))  # 5040
    print(factorial(8))  # 40320
    print(factorial(9))  # 362880
    print(factorial(10))  # 3628800
