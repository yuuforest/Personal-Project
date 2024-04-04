package 자료구조;

import java.util.HashMap;

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

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        return Math.min(nums.length / 2, map.size());
    }
}