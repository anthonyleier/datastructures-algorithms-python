class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]

    def generate_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.generate_hash(key)
        self.data[index].append([key, value])

    def search(self, key):
        index = self.generate_hash(key)
        info = self.data[index]
        for item in info:
            if key == item[0]:
                return item[1]
        return None

    def remove(self, key):
        index = self.generate_hash(key)
        info = self.data[index]
        for item in info:
            if key == item[0]:
                info.remove(item)
                return
        raise KeyError('Chave não encontrada')

    def __str__(self):
        text = ""
        for index, info in enumerate(self.data):
            for item in info:
                text += f"({index}, {item[0]}, {item[1]})"
        return text


if __name__ == "__main__":
    hashtable = HashTable(10)
    hashtable.add('Coordenador', 'Laura')
    hashtable.add('Gerente', 'João')
    hashtable.add('Desenvolvedor', 'Carlos')
    hashtable.add('Estagiário', 'Mariana')
    hashtable.add('Desenvolvedor', 'Pedro')
    hashtable.add('Gerente', 'Lucas')
    hashtable.add('Analista', 'Ana')
    hashtable.add('Gerente', 'Mariana')
    hashtable.add('Estagiário', 'Pedro')
    hashtable.add('Analista', 'Laura')
    print(hashtable)

    print(hashtable.search('Gerente'))
    print(hashtable.search('Estagiário'))

    hashtable.remove('Gerente')
    hashtable.remove('Desenvolvedor')
    print(hashtable)
