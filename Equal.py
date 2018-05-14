# Question: https://www.hackerrank.com/challenges/equal/problem

t = int(raw_input())
subs = [5,2,1]

for i in range(t):
    n = int(raw_input())
    dist = list(map(int, raw_input().split()))
    low = min(dist)
    for j in range(n):
        dist[j]-=low
    ops=0
    for j in range(n):
        for k in range(3):
            ops+=int(dist[j]/subs[k])
            dist[j]%=subs[k]
    print ops
