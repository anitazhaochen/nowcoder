import sys

#s = sys.stdin.readlines()

s= [[1,1,100],[2,3,100],[4,5,110]]

s2 = [ 0 for _ in range(1000) ]
for s1 in s:
    #s1 = s1.split(' ')
    for i in range(int(s1[0]),int(s1[1])+1):
        #s2[i] = s1[2].strip('\n')
        s2[i] = s1[2]

flag = s2[1]
r = [1, 1,s2[2]]
res = []
i = 1

while i < 1000:
    if s2[i] == flag:
        i += 1
        r[1] = r[1] + 1
    else:
        if r[2] != 0:
            r[1] = r[1] - 1
            res.append(str(r))
        flag = s2[i]
        r = [i, i+1, flag]
        i = i + 1

print ','.join(res)
