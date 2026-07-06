class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    isHappy(n) {
        let set = new Set()
        const getSquare = (num) => {
            let sum = 0
            while (num > 0 ){
                let rem = num % 10
                sum = sum + Math.pow(rem,2)
                num = Math.floor(num/10)
            }
            return sum
        }
        while(n !== 1){
            if(!set.has(n)){
                set.add(n)
                n = getSquare(n)
            }
            else{
                return false
            }
        }
        return true
    }
}
