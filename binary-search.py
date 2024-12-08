import os

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = (high + low) // 2
        if list[guess] == item:
            return guess
        if list[guess] < item:
            low = guess + 1
        else:
            high = guess - 1
    return None

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = int(input("Type the number to be found: "))
item_position = binary_search(list, item)
os.system('cls')
print(f"List: {list}\nItem to be found: {item}\nItem position: {item_position}")