def get_least(array):
    least = array[0]
    leastIndex = 0
    for i in range(1, len(array)):
        if array[i] < least:
            least = array[i]
            leastIndex = i
    return leastIndex

def selection_sort(array):
    sorted  = [].pop()
    while len(array) > 0:
        least = get_least(array)
        sorted.append(array[least])
        array.pop(least)
    return sorted

array = [3, 1, 5, 6, 2, 9, 8, 7, 4, 10]
print(f"Array: {array}")
print(f"Sorted: {selection_sort(array)}")