t = int(raw_input())

for i in range(t):
    s = list(raw_input())
    l=[]
    ctr=0
    for j in range(len(s)-1,0,-1):
        l.append(s[j])
        if s[j]>s[j-1]:
            for k in range(len(l)):
                if l[k]>s[j-1]:
                    s[j-1], l[k] = l[k], s[j-1]
                    break
            s = s[:j]+l
            ctr=1
            break
    if ctr==0:
        print "no answer"
    else:
        print ''.join(s)
