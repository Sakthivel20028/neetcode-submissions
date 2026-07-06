class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let trimmed=s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        let i = 0 ;
        let j = trimmed.length-1
        while(i<j){
            if(trimmed[i] === trimmed[j]){
                i++
                j--
            }
            else{
                return false
            }
        }
        return true
    }
}
