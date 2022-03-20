import numpy as np

def prod_list(l):
    return np.prod(np.array(l))

if __name__ == '__main__':
    print(prod_list([1, 2, 3, 4, 5]))