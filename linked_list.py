class Node:
    def __init__(self):
        self.value = 0
        self.next = None

    def __str__(self):
        return f"{self.value} | {self.next}"


if __name__ == "__main__":
    one = Node()
    two = Node()
    three = Node()

    one.value = 5
    two.value = 10
    three.value = 15

    one.next = two
    two.next = three
    three.next = None

    # Abordagem oficial
    head = one
    while (head != None):
        print(head.value)
        head = head.next

    # Minha abordagem
    print(one)
