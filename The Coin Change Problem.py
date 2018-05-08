# Question: https://www.hackerrank.com/challenges/coin-change/problem

n,m = map(int, raw_input().split())
coins = list(map(int, raw_input().split()))

sol = [[0 for x in range(n+1)] for y in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        sol[i][j]+=sol[i-1][j]
        if j%coins[i-1]==0:
            sol[i][j]+=1
        k=1
        while j-k*coins[i-1]>0:
            sol[i][j]+=sol[i-1][j-k*coins[i-1]]
            k+=1

print sol[m][n]
