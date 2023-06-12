def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)


if __name__ == "__main__":
    print(fatorial(1)) # 1
    print(fatorial(2)) # 2
    print(fatorial(3)) # 6
    print(fatorial(4)) # 24
    print(fatorial(5)) # 120
    print(fatorial(6)) # 720
    print(fatorial(7)) # 5040
    print(fatorial(8)) # 40320
    print(fatorial(9)) # 362880
    print(fatorial(10)) # 3628800