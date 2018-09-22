def rand1(n):
    x = 53402397
    rand_seq = []
    for i in range(n):
        x = 65539 *x + 125654
        if x < 0:
            x += 2147483647
            x += 1
        rand_seq.append(x)
    return rand_seq

def rand2(n):
    x = 1
    A = 48271
    M = 2147483647
    Q = M/A
    R = M%A
    rand_seq = []
    for i in range(n):
        x = A* (x%Q) - R*(x%Q)
        if x < 0:
            x = x + M
        rand_seq.append(x)
    return rand_seq

def rand3(n):
    x = 1
    next = 0
    A = rand2(55)
    rand_seq = []
    for i in range(n):
        j = (next + 31 ) % 55
        x = A[j] - A[next]
        if x < 0:
            x = x + 2147483647
            x = x + 1
        A[next] = x
        next = (next + 1) % 55
        rand_seq.append(x)
    return rand_seq

print rand1(5)
print rand2(5)
print rand3(5)

NUMBER = 10
z,o,p,q,r,s,t,u,v,w = 0,0,0,0,0,0,0,0,0,0

for i in rand3(NUMBER):
    # print i,2**63-1 ,"----------"
    n = float(i)/(2**63-1)
    if n >= 0.0 and n<=0.1:
        z +=1
    elif n > 0.1 and n<=0.2:
        o +=1
    elif n > 0.2 and n<=0.3:
        p +=1
    elif n > 0.3 and n<=0.4:
        q +=1
    elif n > 0.4 and n<=0.5:
        r +=1
    elif n > 0.5 and n<=0.6:
        s +=1
    elif n > 0.6 and n<=0.7:
        t+=1
    elif n > 0.7 and n<=0.8:
        u+=1
    elif n > 0.8 and n<=0.9:
        v+=1
    elif n > 0.9 and n<=1.0:
        w+=1

print "0-1:",z/NUMBER,"%"
print "1-2:",o/NUMBER,"%"
print "2-3:",p/NUMBER,"%"
print "3-4:",q/NUMBER,"%"
print "4-5:",r/NUMBER,"%"
print "5-6:",s/NUMBER,"%"
print "6-7:",t/NUMBER,"%"
print "7-8:",u/NUMBER,"%"
print "8-9:",v/NUMBER,"%"
print "9-10:",w/NUMBER,"%"


# print rand2(5)
# print rand3(5)
