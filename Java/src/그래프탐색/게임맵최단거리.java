package 그래프탐색;

public class 게임맵최단거리 {

    public static void main(String[] args) {

        int[][] m1 = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,1}, {0,0,0,0,1}};
        System.out.println(solution(m1));

        int[][] m2 = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,0}, {0,0,0,0,1}};
        System.out.println(solution(m2));

    }

    public static int solution(int[][] maps) {
        int answer = 0;
        return answer;
    }
    
}
