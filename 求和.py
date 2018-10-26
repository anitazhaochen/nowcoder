def help(n, m, start=1, result=[]):
    if m == 0:
        print " ".join(map(str,result))
    for i in range(start, n+1):
        result.append(i)
        help(n, m-i,i+1,result)
        result.pop()

n,m = map(int,raw_input().split(' '))
help(n,m)

