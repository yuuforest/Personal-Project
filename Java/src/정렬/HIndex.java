package 정렬;

import java.util.Arrays;

public class HIndex {

    public static void main(String[] args) {

        int[] c1 = {3, 0, 6, 1, 5};
        System.out.println(solution(c1));

        int[] c2 = {3, 0, 6, 1, 5, 8};
        System.out.println(solution(c2));
    }

    public static int solution(int[] citations) {

        Arrays.sort(citations);

        int length = citations.length;
        for (int i = 0; i < length; i++) {

            int count = length - i;

            if (count <= citations[i]) {
                return count;
            }
        }

        return 0;
    }
    
}
