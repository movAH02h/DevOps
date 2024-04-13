array = [-100, -1, 0, 1, 1, 2, 3, 10, 100]

def bin_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] > x:
            return bin_search(arr, low, mid - 1, x)

        else:
            return bin_search(arr, mid + 1, high, x)

    else:
        return -1