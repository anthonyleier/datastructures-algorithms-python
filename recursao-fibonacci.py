def fibonacci(numero):
    if numero == 1 or numero == 2:
        return 1
    return fibonacci(numero-1) + fibonacci(numero-2)


if __name__ == "__main__":
    print(fibonacci(4)) # 3
    print(fibonacci(5)) # 5
    print(fibonacci(6)) # 8
    print(fibonacci(7)) # 13

