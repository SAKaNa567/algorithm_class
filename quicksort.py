def quicksort(seq):
    if len(seq) <1:
        return seq
    pivot = seq[len(seq)-1]
    left = []
    right = []
    for x in range(0,len(seq)-1):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right

print quicksort([2,9,1,8,3])
