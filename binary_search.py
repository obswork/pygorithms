def binary_search(array, value):
    last, first = len(array), 0

    while first < last:
        # int division
        mid = (last - first) // 2
        item = array[mid]

        if item == value:
            return True

        elif item < value:
            last = mid

        else:
            first = mid

    return False


def recursive_binary_search(array, value, first=0, last=None):
    last = last or len(array)

    # will return 0 if e.g. last is out of bounds
    # ..or will it? Test!
    if len(array[first:last]) < 1:
        return False

    mid = (last - first) // 2
    if array[mid] == value:
        return True
    elif array[mid] < value:
        # recursively call fx on left sub-array
        return recursive_binary_search(array, value, first=first, last=mid)
    else:
        # else recursively call fx on right sub-array
        return recursive_binary_search(array, value, first=mid, last=last)
