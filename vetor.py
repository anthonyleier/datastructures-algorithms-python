from array import array

numeros = array('i', [10, 15, 20, 25, 30, 35])

for numero in numeros:
    print(numero)

numeros.append(5)
print(numeros)

numeros.remove(20)
print(numeros)

try:
    numeros.append('teste')
except TypeError:
    print("Não é possível adicionar outros tipos de dados no array")
