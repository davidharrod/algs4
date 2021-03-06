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
    """Use 3x + 1 as sequence. The only difference 
    between shell and insertion is that shell look back at h positions."""
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


def merge_sort(array):
    def merge(array1, array2):
        p, q = 0, 0
        result_array = (len(array1)+len(array2))*[0]
        for _ in range(len(result_array)):
            if p == len(array1):
                result_array[_] = array2[q]
                q += 1
                continue
            if q == len(array2):
                result_array[_] = array1[p]
                p += 1
                continue
            if is_less(array1[p], array2[q]):
                result_array[_] = array1[p]
                p += 1
            else:
                result_array[_] = array2[q]
                q += 1
        return result_array

    if len(array) == 2:
        if not is_less(array[0], array[1]):
            exchange(array, 0, 1)
        return array
    elif len(array) < 2:
        return array

    low = 0
    high = len(array)  # (a,b]
    mid = int((high-low)/2)
    sub_array1 = merge_sort(array[low:mid])  # Sort first merge later.
    sub_array2 = merge_sort(array[mid:high])
    result_array = merge(sub_array1, sub_array2)
    return result_array


def quick_sort(array, low, high):
    def partition(array, low, high):
        partition_val = array[low]
        partition_pos = low
        while high > low:
            while array[high] >= partition_val and high > low:
                high -= 1
            while array[low] <= partition_val and high > low:
                low += 1
            exchange(array, low, high)
        exchange(array, partition_pos, low)
        return low

    # Define return pattern.
    if low >= high:
        return None

    # Define recursion pattern.
    # The position of this value is settled.
    base_val_pos = partition(array, low, high)
    quick_sort(array, low, base_val_pos-1)
    quick_sort(array, base_val_pos+1, high)

    return None


if __name__ == '__main__':
    array = [5, 2, 4, 1, 3, 234, 23, 5, 345,
             34, 5, 2, 34, 23, 4, 23, 423, 4, 23]
    quick_sort(array, 0, len(array)-1)
    print(array)
