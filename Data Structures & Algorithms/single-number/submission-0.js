class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        let map = new Map()
        for(let num of nums){
            map.set(num,(map.get(num) || 0) + 1)
        }
        for(let [num,count] of map){
            if (count === 1){
                return num
            }
        }
    }
}
