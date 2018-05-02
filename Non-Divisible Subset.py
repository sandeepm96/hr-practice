# Question: https://www.hackerrank.com/challenges/non-divisible-subset/problem

n,k = map(int, raw_input().split())
s = list(map(int, raw_input().split()))

count = [0 for x in range(k)]

for i in range(len(s)):
    s[i]= s[i]%k
    count[s[i]]+=1

total = 0

for i in range((k/2)+1):
    if i==0 or i==k-i:
        if count[i]>0:
            total+=1
    else:
        add = count[i] if count[i]>count[k-i] else count[k-i]
        total+=add

print total
