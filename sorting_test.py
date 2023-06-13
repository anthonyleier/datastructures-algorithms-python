import random
from sorting import bubblesort, insertionsort, selectionsort, mergesort, quicksort


random_sample = random.sample(range(1, 100), 10)
already_sorted = [20, 141, 146, 431, 483, 700, 712, 722, 809, 943]
inversed = [966, 961, 848, 717, 679, 673, 455, 207, 136, 29]
repeated = [5, 5, 5, 717, 5, 673, 5, 5, 5, 29]


if __name__ == "__main__":
    array = inversed
    quicksort(array)
    print(array)
