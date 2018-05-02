# Question: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

n = int(raw_input())
score = list(map(int, raw_input().split()))
m = int(raw_input())
alice = list(map(int, raw_input().split()))

def search(s):
    l,r = 0,n-1
    d=1
    while(l<=r):
        mid=(l+r)/2
        if s==score[mid]:
            return d,mid,mid
        elif s>score[mid]:
            r=mid-1
            d=-1
        else:
            l=mid+1
            d=1
    return d,l,r

rank = [1]
for i in range(1,n):
    if score[i]==score[i-1]:
        rank.append(rank[i-1])
    else:
        rank.append(rank[i-1]+1)

for i in range(m):
    d,l,r = search(alice[i])
    if l==r:
        print rank[l]
    else:
        if d==-1:
            print rank[l]
        else:
            print rank[r]+1
