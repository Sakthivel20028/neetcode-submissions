class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k){
        let sortedNums = nums.sort((a,b) => b - a)
        let len = sortedNums.length
        let output = sortedNums[k-1]
        return output
    }
}
