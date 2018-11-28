


def fanzhuan(a,start,end):
    while start < end:
        tmp = a[start]
        a[start] = a[end]
        a[end] = tmp
        start += 1
        end -= 1


if __name__ == "__main__":
    a = "abcdef"
    a = list(a)
    fanzhuan(a, 0,2)
    fanzhuan(a, 3,5)
    fanzhuan(a, 0,5)
    print str(a)

