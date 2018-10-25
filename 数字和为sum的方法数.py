
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

#sum = int(raw_input().split(' ')[1])
#arr = map(int,raw_input().split(' '))
#print count(sum, arr)

def res(nums, sum):
    dp = [ [0]*(sum+1) for _ in range(len(nums)+1)]
    for i in range(0,len(nums)+1):
        dp[i][0] = 1


	count = 1
    for j in nums:
        for i in range(1,sum+1):
            if i >= j:
                dp[count][i] = dp[count - 1][i - j] + dp[count - 1][i]
            else:
                dp[count][i] = dp[count-1][i]
        count += 1
    print dp
    print dp[-1][-1]


res([5,5,10,2,3],15)
