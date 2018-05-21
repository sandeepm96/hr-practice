# Question: https://www.hackerrank.com/challenges/merging-communities/problem

n,q = map(int, raw_input().split())
p = [x for x in range(n+1)]
size = [1 for x in range(n+1)]

def find_set(x):
    if x!=p[x]:
        p[x]=find_set(p[x])
    return p[x]

def merge_sets(x, y):
    px=find_set(x)
    py=find_set(y)
    if px==py:
        return
    else:
        if size[px]>size[py]:
            p[py]=px
            size[px]+=size[py]
        else:
            p[px]=py
            size[py]+=size[px]

for i in range(q):
    query = list(raw_input().split())
    if len(query)==2:
        parent = find_set(int(query[1]))
        print size[parent]
    else:
        merge_sets(int(query[1]),int(query[2]))
