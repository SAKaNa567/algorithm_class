import heapq

queue = [[100,22],
         [12,55],
         [1,0],
         [77,5],
         [99,100],]
def priority_queue():
    queue.sort()#from small to big
    print "original is ", queue
    queue.remove(queue[0])
    return queue

x = priority_queue()
print "changed is " ,x
