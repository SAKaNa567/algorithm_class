from random import randint
import random
def quicksort(alist, start, end):
	if start < end:
		pIndex = partition(alist, start, end)
		quicksort(alist, start, pIndex-1)
		quicksort(alist, pIndex+1, end)
	return alist

def partition(alist, start, end):
	pivot = randint(start, end)
        alist[pivot],alist[end] = alist[end],alist[pivot]
	pIndex = start

	for i in range(start, end):
		if alist[i] <= alist[end]:
                        alist[pIndex],alist[i] = alist[i],alist[pIndex]
			pIndex += 1
        alist[end],alist[pIndex] = alist[pIndex],alist[end]
	return pIndex


def quicksort_determine(alist, start, end):
	if start < end:
		pIndex = partition_determine(alist, start, end)
		quicksort_determine(alist, start, pIndex-1)
		quicksort_determine(alist, pIndex+1, end)
	return alist

def partition_determine(alist, start, end):
	pivot = 0
        alist[pivot],alist[end] = alist[end],alist[pivot]
	pIndex = start
	for i in range(start, end):
		if alist[i] <= alist[end]:
                        alist[pIndex],alist[i] = alist[i],alist[pIndex]
			pIndex += 1
        alist[end],alist[pIndex] = alist[pIndex],alist[end]
	return pIndex

def make_sequence(ROOPNUMBER):
    sequence = []
    for i in range(ROOPNUMBER):
        sequence.append(random.random())
    return sequence

if __name__ == '__main__':
        N = [100,1000,10000,100000,1000000]

        import time
        for i in N:
            list =make_sequence(i)
            start = time.time()
            quicksort(list, 0, len(list)-1)
            end = time.time()
            print "Randomize",end-start

        for i in N:
            list2 = make_sequence(i)
            start = time.time()
            quicksort_determine(list2,0,len(list2)-1)
            end = time.time()
            print "Determine",end - start
