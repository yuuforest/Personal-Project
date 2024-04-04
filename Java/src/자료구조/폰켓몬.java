package 자료구조;

// import java.util.HashMap;
import java.util.HashSet;

class Solution {

    public static void main(String[] args) {

        int[] s1 = {3, 1, 2, 3};
        System.out.println(solution(s1));

        int[] s2 = {3,3,3,2,2,4};
        System.out.println(solution(s2));

        int[] s3 = {3,3,3,2,2,2};
        System.out.println(solution(s3));

    }

    public static int solution(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        return Math.min(nums.length / 2, set.size());
    }
}