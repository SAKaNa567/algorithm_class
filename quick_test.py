def quick(seq):
    if len(seq) < 1:
        return seq
    right = []
    left = []
    pivot = seq[len(seq)-1]
    for i in range(0,len(seq)-1):
        if pivot <= seq[i]:
            right.append(seq[i])
        else:
            left.append(seq[i])
    right = quick(right)
    left = quick(left)
    foo = [pivot]
    return  left + foo + right

print quick([2,3,1])
