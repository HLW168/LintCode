public class Solution {
    /**
     * @param A: An integer
     * @return: a float number
     */
    public float maxOfArray(float[] A) {
        // write your code here
        float maxValue = -10000000;
        for (int i = 0; i < A.length; i++ ) {
            //System.out.println(A[i]);
            if (A[i] > maxValue) {
                maxValue = A[i];
                //System.out.println(maxValue);
            }
        }
     
     return maxValue;
        
    }
}
