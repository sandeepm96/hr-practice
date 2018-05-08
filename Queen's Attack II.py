# Question: https://www.hackerrank.com/challenges/queens-attack-2/problem

n,k = map(int, raw_input().split())
rq,cq = map(int, raw_input().split())

obs=[]

for i in range(k):
    obs.append((map(int, raw_input().split())))

cells = [n-rq,rq-1,n-cq,cq-1,min(n-rq,n-cq),min(n-cq,rq-1),min(rq-1,cq-1),min(n-rq,cq-1)]

for i in range(k):
    if obs[i][1]==cq:
        if obs[i][0]>rq:
            c=obs[i][0]-rq-1
            cells[0]=c if c<cells[0] else cells[0]
        else:
            c=rq-obs[i][0]-1
            cells[1]=c if c<cells[1] else cells[1]
    elif obs[i][0]==rq:
        if obs[i][1]>cq:
            c=obs[i][1]-cq-1
            cells[2]=c if c<cells[2] else cells[2]
        else:
            c=cq-obs[i][1]-1
            cells[3]=c if c<cells[3] else cells[3]
    elif obs[i][0]-rq==obs[i][1]-cq:
        if obs[i][0]>rq:
            c=obs[i][0]-rq-1
            cells[4]=c if c<cells[4] else cells[4]
        else:
            c=rq-obs[i][0]-1
            cells[6]=c if c<cells[6] else cells[6]
    elif obs[i][0]+obs[i][1]==rq+cq:
        if obs[i][0]>rq:
            c=obs[i][0]-rq-1
            cells[7]=c if c<cells[7] else cells[7]
        else:
            c=rq-obs[i][0]-1
            cells[5]=c if c<cells[5] else cells[5]

tot=0
for i in range(8):
    tot+=cells[i]

print tot
