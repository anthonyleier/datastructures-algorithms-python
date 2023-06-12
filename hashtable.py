class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [[] for _ in range(tamanho)]

    def montar_hash(self, chave):
        return hash(chave) % self.tamanho

    def adicionar(self, chave, valor):
        indice = self.montar_hash(chave)
        self.dados[indice].append([chave, valor])

    def procurar(self, chave):
        indice = self.montar_hash(chave)
        dado = self.dados[indice]
        for item in dado:
            if chave == item[0]:
                return item[1]
        return None

    def remover(self, chave):
        indice = self.montar_hash(chave)
        dado = self.dados[indice]
        for item in dado:
            if chave == item[0]:
                dado.remove(item)
                return
        raise KeyError('Chave não encontrada')

    def __str__(self):
        texto = ""
        for indice, dado in enumerate(self.dados):
            for item in dado:
                texto += f"({indice}, {item[0]}, {item[1]})"
        return texto


if __name__ == "__main__":
    hashtable = HashTable(10)
    hashtable.adicionar('Coordenador', 'Laura')
    hashtable.adicionar('Gerente', 'João')
    hashtable.adicionar('Desenvolvedor', 'Carlos')
    hashtable.adicionar('Estagiário', 'Mariana')
    hashtable.adicionar('Desenvolvedor', 'Pedro')
    hashtable.adicionar('Gerente', 'Lucas')
    hashtable.adicionar('Analista', 'Ana')
    hashtable.adicionar('Gerente', 'Mariana')
    hashtable.adicionar('Estagiário', 'Pedro')
    hashtable.adicionar('Analista', 'Laura')
    print(hashtable)

    print(hashtable.procurar('Gerente'))
    print(hashtable.procurar('Estagiário'))

    hashtable.remover('Gerente')
    hashtable.remover('Desenvolvedor')
    print(hashtable)
