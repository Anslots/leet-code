var twoSum = function(nums, target) {   
  for (var i = 0; i < nums.length; i++) {
    for (var j =i + 1; j < nums.length; j++) {
      // console.log(nums[i] + nums[j] === target);
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

const nums = [2,7,11,15]
const target = 9
console.log(twoSum(nums, target))
