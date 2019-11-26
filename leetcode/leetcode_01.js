/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

function sortNumber(a,b){
  return a - b
}



var twoSum = function(nums, target) {
  a = []
  nums.forEach(function (num) {
    a.push(num)
  })
  nums.sort(sortNumber)
  i = 0
  j = nums.length - 1
  while (i<j) {
    if (nums[i] + nums[j] === target){
      tmp_a = a.indexOf(nums[i])
      tmp_b = a.indexOf(nums[j])
      if (tmp_a === tmp_b) {
        a.splice(tmp_a,1)
        tmp_b = a.indexOf(nums[j]) + 1
      }
      if (tmp_a > tmp_b) {
        tmp = tmp_a
        tmp_a = tmp_b
        tmp_b = tmp
      }
      return [tmp_a,tmp_b]
    }
    else if(nums[i]+nums[j] > target) {
      j = j - 1
    }
    else{
      i = i + 1
    }
    }
  return []
  }

var twoSum = function(nums, target) {
  a = {}
  i = 0
  nums.forEach((num) => {
    a[num] = i
    i = i + 1
  })
  result = []
  for (var i = 0; i < nums.length; i++) {
    if (a[target-nums[i]] && i != a[target-nums[i]]){
      result.push(i)
      result.push(a[target-nums[i]])
      break
    } 
  }
  return result
}

console.log(twoSum([7,2,11,15], 9))
console.log(twoSum([7,2,332,1,2,715], 4))
