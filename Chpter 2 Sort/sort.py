def is_less(a, b):
    return True if a < b else False


def exchange(array, i, j):
    exchange_val = array[i]
    array[i] = array[j]
    array[j] = exchange_val
    return None


def selection_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if is_less(array[j], array[i]):
                exchange(array, i, j)
                # exchange_val = array[i]
                # array[i] = array[j]
                # array[j] = exchange_val
    return array


def insertion_sort(array):
    p, q = 0, 0
    while p < len(array)-1:
        q = p+1
        while q > 0:
            if is_less(array[q], array[q-1]):
                exchange(array, q, q-1)
                q -= 1
            else:
                break
        p += 1
    return array


if __name__ == '__main__':
    array = [21, 23, 213, 123, 15, 23, 5, 23, 46, 43, 5,
             7, 9, 57, 6, 3, 5, 423, 42, 4, 3141, 34141343124]
    print(selection_sort(array))
