import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    //방향 없는 그래프가 주어졌을 때,
    // 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
    // 첫째 줄에 노드의 개수와 간선의 개수 N, M이 주어짐
    // 둘째 줄부터 간선의 양끝점 U, V가 주어짐

    public static boolean[] visited;
    public static ArrayList<Integer>[] graph;

    // DFS 함수 정의
    public static void dfs(int x) {
        // 현재 노드를 방문 처리
        visited[x] = true;

        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graph[x].size(); i++) {
            int y = graph[x].get(i);
            if (!visited[y]) dfs(y);
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        int N = sc.nextInt();
        int M = sc.nextInt();

        // 그래프와 방문 배열 초기화
        graph = new ArrayList[N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        // 간선 정보 입력 받기
        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        // 연결 요소의 개수 세기
        int connectedComponents = 0;
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                dfs(i);
                connectedComponents++;
            }
        }

        // 결과 출력
        System.out.println(connectedComponents);

        sc.close();
    }

}