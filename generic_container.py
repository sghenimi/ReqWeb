from math import sqrt
import numpy as np


def first(container):
    return container[0]


if __name__ == "__main__":
    list_01 = ["a", "b", "c"]
    print(list_01)
    print(first(list_01))

    arr_a = np.array([sqrt(i) for i in range(5)])
    print("--"*100)
    for i in arr_a:
        print(i)