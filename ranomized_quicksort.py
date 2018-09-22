import random
Sminus  =[]
Splus = []
def quicksort(S):
    if len(S) is 0: return
    ai = S[random.randint(0,len(S)-1)]
    for a in S:
        if a < ai:
            Sminus.append(a)
        if a > ai: 
            Splus.append(a)
    quicksort(Sminus)
    print ai
    quicksort(Splus)

  def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = p[]
        for x in range(1, len(seq)):
            if seq[x] <= pivot:
                left.append(seq[x])
            else:
                right.append(seq[x])
        left = quicksort(left)
        right = quicksort(right)
        foo = [pivot]
        return left + foo + right  
    




S = [9,2,3,1,4,0,5,7,8,6,3]
print quicksort(S)
