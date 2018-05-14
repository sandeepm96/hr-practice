# Question: https://www.hackerrank.com/challenges/jesse-and-cookies/problem

n,k = map(int, raw_input().split())
s = list(map(int, raw_input().split()))

def min_heapify(i):
    l = 2*i+1
    r = 2*i+2
    if l<n and s[l]<s[i]:
        small=l
    else:
        small=i
    if r<n and s[r]<s[small]:
        small=r
    if small!=i:
        s[small],s[i]=s[i],s[small]
        min_heapify(small)

for i in range((n+1/2)-1,-1,-1):
    min_heapify(i)

ctr=0
while(s[0]<k):
    if n<2:
        print "-1"
        break
    else:
        min1=s[0]
        s[0]=s[n-1]
        n-=1
        min_heapify(0)
        s[0]= min1+s[0]*2
        min_heapify(0)
        ctr+=1
else:
    print ctr
