# Question: https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem

n = int(raw_input())
cust = []
for i in range(n):
    cust.append(list(map(int,raw_input().split())))
cust.sort()

time=cust[0][0]
wait_time=0
heap=[[] for x in range(n)]
heap_size=0
ctr=0

def siftup(index):
    while  index!=0 and heap[index][1]<heap[(index-1)/2][1]:
        heap[index], heap[(index-1)/2] = heap[(index-1)/2], heap[index]
        index=int((index-1)/2)

def addtoheap(order, heap_size):
    heap[heap_size]=order
    heap_size+=1
    siftup(heap_size-1)
    return heap_size

def minheapify(index):
    l=index*2+1
    r=index*2+2
    if l<heap_size and heap[l][1]<heap[index][1]:
        small=l
    else:
        small=index
    if r<heap_size and heap[r][1]<heap[small][1]:
        small=r
    if small!=index:
        heap[index], heap[small] = heap[small], heap[index]
        minheapify(small)

def extractmin(heap_size):
    minimum=heap[0]
    heap[0]=heap[heap_size-1]
    heap_size-=1
    minheapify(0)
    return minimum, heap_size

for i in range(n):
    # print "after", i, "th:", time, wait_time, ctr, heap, heap_size
    while(ctr<n and cust[ctr][0]<=time):
        heap_size = addtoheap(cust[ctr], heap_size)
        ctr+=1
    # print heap,heap_size
    if heap_size==0:
        heap_size = addtoheap(cust[ctr], heap_size)
        time=cust[ctr][0]
        ctr+=1
    min_order, heap_size = extractmin(heap_size)
    time+=min_order[1]
    wait_time+=time-min_order[0]

print int(wait_time/n)
