class Stack:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def is_empty(self):
        return self.length() == 0

    def add(self, elemento):
        self.data.insert(0, elemento)

    def remove(self):
        if not self.is_empty():
            return self.data.pop(0)

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    pilha = Stack()
    pilha.add('Anthony')
    pilha.add('Luiz')
    pilha.add('Wendel')
    pilha.add('Marília')
    pilha.add('Júlio')
    pilha.add('Ronei')
    pilha.add('Boico')

    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
    print("Elemento removido:", pilha.remove())
