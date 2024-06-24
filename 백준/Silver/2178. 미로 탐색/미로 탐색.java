import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int N, M; // 미로의 크기
    static int[][] maze; // 미로 배열
    static boolean[][] visited; // 방문 여부 배열
    static int[][] distance; // 최단 거리 배열
    static int[] dx = {-1, 1, 0, 0}; // 상하좌우 이동을 위한 배열
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); // 행 수 입력
        M = sc.nextInt(); // 열 수 입력
        maze = new int[N][M]; // 미로 배열 초기화
        visited = new boolean[N][M]; // 방문 여부 배열 초기화
        distance = new int[N][M]; // 최단 거리 배열 초기화

        // 미로 정보 입력
        for (int i = 0; i < N; i++) {
            String line = sc.next();
            for (int j = 0; j < M; j++) {
                maze[i][j] = line.charAt(j) - '0'; // 문자열을 정수로 변환하여 저장
            }
        }

        // BFS를 사용하여 최단 경로 찾기
        bfs(0, 0);

        // 도착점의 최단 거리 출력
        System.out.println(distance[N - 1][M - 1]);
    }

    public static void bfs(int startX, int startY) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{startX, startY}); // 시작점을 큐에 추가
        visited[startX][startY] = true; // 시작점 방문 처리
        distance[startX][startY] = 1; // 시작점의 거리를 1로 설정

        while (!q.isEmpty()) {
            int[] current = q.poll(); // 큐에서 현재 위치를 꺼냄
            int x = current[0];
            int y = current[1];

            // 네 방향으로 이동
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 이동할 위치가 미로 범위 내에 있고 이동 가능하며 방문하지 않은 경우
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (maze[nx][ny] == 1 && !visited[nx][ny]) {
                        q.offer(new int[]{nx, ny}); // 큐에 다음 위치 추가
                        visited[nx][ny] = true; // 방문 처리
                        distance[nx][ny] = distance[x][y] + 1; // 현재 위치까지의 거리에 1을 더하여 저장
                    }
                }
            }
        }
    }
}