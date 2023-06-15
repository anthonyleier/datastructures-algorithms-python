class Queue:
    def __init__(self):
        self.data = []

    def add(self, elemento):
        self.data.append(elemento)

    def remove(self):
        if not self.is_empty():
            return self.data.pop(0)

    def length(self):
        return len(self.data)

    def is_empty(self):
        return self.length() == 0

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    queue = Queue()
    queue.add('Anthony')
    queue.add('Luiz')
    queue.add('Wendel')
    queue.add('Marília')
    queue.add('Júlio')
    queue.add('Ronei')
    queue.add('Boico')
    print(queue)

    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    print(queue)

    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    print(queue)
