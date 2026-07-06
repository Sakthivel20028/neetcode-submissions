class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map()
        for(let i = 0 ; i < nums.length ;i++){
            let currentNum = nums[i]
            let complement = target - currentNum
            if(map.has(complement)){
                return [map.get(complement),i]
            }
            else{
                map.set(currentNum,i)
            }
        }
    }
}
