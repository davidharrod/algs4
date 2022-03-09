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


def shell_sort(array):
    """Use 3x + 1 as sequence."""
    N = len(array)
    h = 1
    while(h < N/3):
        h = 3*h+1  # Calculate h according to 3x + 1 sequence.
    while h >= 1:
        p, q = 0, 0
        while p < N-h:
            q = p+h
            while q >= h:
                if is_less(array[q], array[q-h]):
                    exchange(array, q, q-h)
                    q -= h
                else:
                    break
            p += 1
        h = int(h/3)
    return array


if __name__ == '__main__':
    array = [231112, 3, 21, 423, 534, 56, 5, 7,
             65, 7, 5678, 67, 987, 97809, 780, 890, 2]
    print(shell_sort(array))
