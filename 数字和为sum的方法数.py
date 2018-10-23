
def count(sum, arr):
    if sum == 0:
        return 1
    if sum <0 or len(arr)==0:
        return 0

    start = 0
    sum1 = 0
    sum2 = 0
    sum1 += count(sum,arr[start+1:])
    sum2 += count(sum-arr[start],arr[start+1:])
    return sum1+sum2

sum = int(raw_input().split(' ')[1])
arr = map(int,raw_input().split(' '))
print count(sum, arr)

