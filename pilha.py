class Pilha:
    def __init__(self):
        self.dados = []

    def tamanho(self):
        return len(self.dados)

    def esta_vazia(self):
        return self.tamanho() == 0

    def adicionar(self, elemento):
        self.dados.insert(0, elemento)
        print(self)

    def remover(self):
        if not self.esta_vazia():
            self.dados.pop(0)
        print(self)

    def __str__(self):
        return str(self.dados)


if __name__ == "__main__":
    pilha = Pilha()
    pilha.adicionar('Anthony')
    pilha.adicionar('Luiz')
    pilha.adicionar('Wendel')
    pilha.adicionar('Marília')
    pilha.adicionar('Júlio')
    pilha.adicionar('Ronei')
    pilha.adicionar('Boico')

    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
