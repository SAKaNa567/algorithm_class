import random
def quicksort(alist,start,end):
    if start < end:
        pIndex = partition(alist,start,end)
        quicksort(alist,start,pIndex-1)
        quicksort(alist,pIndex+1,end)
    return alist
    
def swap(list,p1,p2):
    tmp  = list[p1]
    list[p1] = list[p2]
    list[p2] = tmp
    return list

def partition(alist,start,end):
    pivot = random.randint(start,end)
    alist = swap(alist,pivot,end)#common1
    pIndex = start
    for i in range(start,end):
        if alist[i] <= alist[end]:#alist[end]ipivot
            alist = swap(alist,pIndex,i)
            pIndex +=1
    alist = swap(alist,end,pIndex)#common2
    return pIndex


alist = [1,3,1,6,1,2,2,8,3]
print quicksort(alist,0,len(alist)-1)
