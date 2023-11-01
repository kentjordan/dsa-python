import math

# List must be sorted first
data = [i*2 for i in range(0, 10)]


def search(data: list[int], search_item: int):

    l = 0
    r = len(data)

    while l < r:

        mid = math.floor((l + r) / 2)

        if search_item == data[mid]:
            return mid

        if search_item > data[mid]:
            l = mid
            continue

        r = mid


for i, e in enumerate(data):
    searched_index = search(data, e)
    print(f'Item \'{e}\' index at: ', searched_index)
