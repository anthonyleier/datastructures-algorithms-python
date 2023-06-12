class Fila:
    def __init__(self):
        self.dados = []

    def adicionar(self, elemento):
        self.dados.append(elemento)
        print(self)

    def remover(self):
        if not self.esta_vazia():
            self.dados.pop(0)
        print(self)

    def tamanho(self):
        return len(self.dados)

    def esta_vazia(self):
        return self.tamanho() == 0

    def __str__(self):
        return str(self.dados)


if __name__ == "__main__":
    fila = Fila()
    fila.adicionar('Anthony')
    fila.adicionar('Luiz')
    fila.adicionar('Wendel')
    fila.adicionar('Marília')
    fila.adicionar('Júlio')
    fila.adicionar('Ronei')
    fila.adicionar('Boico')

    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
    fila.remover()
