package 자료구조;

public class 올바른괄호 {

    public static void main(String[] args) {

        String s1 = "()()";
        System.out.println(solution(s1));

        String s2 = "(())()";
        System.out.println(solution(s2));

        String s3 = ")()(";
        System.out.println(solution(s3));

        String s4 = "(()(";
        System.out.println(solution(s4));

        String s5 = "()()()((())()()()()()";
        System.out.println(solution(s5));

    }

    public static boolean solution(String s) {

        if (s.charAt(s.length()-1) == '(') {
            return false;
        }

        int count = 0;
        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '(') {
                count += 1;
            } else {
                count -= 1;
            }

            if (count < 0) {
                return false;
            }
        }

        if (count > 0) return false;
        return true;
    }
}
