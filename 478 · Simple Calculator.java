public class Calculator {
    /**
     * @param a: An integer
     * @param operator: A character, +, -, *, /.
     * @param b: An integer
     * @return: The result
     */
    public int calculate(int a, char operator, int b) {
        // write your code here
        int res = 0;
        switch(operator) {
            case '+':
                //System.out.println(a+b);
                res =  a+b;
                //System.out.println(res);
                break;
            case '-':
                res = a-b;
                break;
            case '*':
                res = a*b;
                break;
            case '/':
                res = a/b;
                break;
        }
        //System.out.println(res);
        return res;
        
    }
}
