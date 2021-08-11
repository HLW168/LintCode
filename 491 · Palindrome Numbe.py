public class Solution {
    /**
     * @param num: a positive number
     * @return: true if it's a palindrome or false
     */
    public boolean isPalindrome(int num) {
        // write your code here
        String number = String.valueOf(num);
        char[] digit = number.toCharArray();
        if (digit.length == 1) {
            return true;
        }
        int midPoint = digit.length/2;
        //System.out.println(midPoint);
        String original = "";
        String contrast = "";
        if (digit.length%2==0) {
            for (int i = 0; i < midPoint; i++) {
            original += digit[i];
            }
            for (int i = digit.length-1; i >= midPoint; i--) {
            contrast += digit[i];
            }
        } else {
             for (int i = 0; i < midPoint; i++) {
            original += digit[i];
            }
            for (int i = digit.length-1; i > midPoint; i--) {
            contrast += digit[i];
            }
        }
        
        //System.out.println(original);
        //System.out.println(contrast);
    
        return original.equals(contrast);
    }
}
