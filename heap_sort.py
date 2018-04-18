#buttom up version
def heapsort(random_list):
    list_size = len(random_list) - 1
    for i in range((list_size / 2), -1, -1):
        MaxHeapify(random_list, i, list_size)

    for i in range(list_size , 0, -1):
        if random_list[0] > random_list[i]:
            random_list[0], random_list[i] = random_list[i] , random_list[0]
            MaxHeapify(random_list, 0, i - 1)
    return random_list

def Left(i):
    return i * 2 + 1

def Right(i):
    return i * 2 + 2

def MaxHeapify(aList, root, bottom):
    left = Left(root)
    right = Right(root)

    if left <= bottom and aList[left] > aList[root]:
        max_child = left
    else:
        max_child = root

    if right <= bottom and aList[right] > aList[max_child]:
        max_child = right

    if max_child != root:
        aList[root], aList[max_child] = aList[max_child], aList[root]
        MaxHeapify(aList, max_child, bottom)

random_list = [3,99,0,11,23,9,75,52]
print heapsort(random_list)
