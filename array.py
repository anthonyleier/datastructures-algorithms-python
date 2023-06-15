from array import array

numbers = array('i', [10, 15, 20, 25, 30, 35])

for number in numbers:
    print(number)

numbers.append(5)
print(numbers)

numbers.remove(20)
print(numbers)

try:
    numbers.append('teste')
except TypeError:
    print("Não é possível adicionar outros tipos de dados no array")
