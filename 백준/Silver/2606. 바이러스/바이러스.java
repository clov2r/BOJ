import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int count = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 컴퓨터의 수 입력
        int n = sc.nextInt();
        // 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 입력
        int m = sc.nextInt();

        // 그래프 초기화
        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // 방문 배열 초기화
        visited = new boolean[n + 1];

        // 그래프 입력
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }

        // 1번 컴퓨터에서 시작하여 DFS 실행
        dfs(1);

        // 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
        System.out.println(count - 1);
    }

    public static void dfs(int x) {
        // 현재 노드를 방문 처리
        visited[x] = true;
        count++;

        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graph[x].size(); i++) {
            int y = graph[x].get(i);
            if (!visited[y]) dfs(y);
        }
    }
}
