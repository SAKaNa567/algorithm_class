#buttom up version
def HeapBottomUp(A,listsize):
    for i in range( listsize/ 2, -1, -1):
        MaxHeapify(A, i, listsize)

def heapsort(random_list):
    list_size = len(random_list) - 1
    HeapBottomUp(random_list,list_size)

    for i in range(list_size , 0, -1):
        # if random_list[0] > random_list[i]:
            random_list[0], random_list[i] = random_list[i] , random_list[0]
            MaxHeapify(random_list, 0, i - 1)
    return random_list

def Left(i):
    return i * 2 + 1

def Right(i):
    return i * 2 + 2

def MaxHeapify(A, i, bottom):
    left = Left(i)
    right = Right(i)

    if left <= bottom and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right <= bottom and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, bottom)

random_list = [3,100,99,0,11,63,12,23,9,75,52]
print "original array: ",random_list
print "sorted array: ",heapsort(random_list)
