class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = new Map()
        for(let char of nums){
            map.set(char,(map.get(char) || 0 )+1)
        }
        const sorted = Array.from(map.entries()).sort((a,b)=>b[1]-a[1])
        let result=[]
        for(let i = 0; i<k;i++){
            result.push(sorted[i][0])
        }
        return result
    }
}
