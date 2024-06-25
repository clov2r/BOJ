import java.util.Scanner;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        // N개의 정수 입력 받음
        // N개의 정수 리스트가 생성됨
        int N = in.nextInt();
        int[] arr = new int[N];

        // N개의 정수 리스트 arr에 N개만큼 값을 집어 넣음
        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }


        // 배열은 반드시 정렬되어야 이분탐색 가능
        Arrays.sort(arr);

        // 배열 안에 M이 있는지 없는지 확인함
        int M = in.nextInt();

        // 여러 번의 이분 탐색 결과를 하나의 문자열로 만들어 출력하기 위함
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < M; i++) {

            // 찾고자 하는 값이 있을 경우 1, 없을 경우 0을 출력해야한다.
            if(binarySearch(arr, in.nextInt()) >= 0) {
                sb.append(1).append('\n');
            }
            else {
                sb.append(0).append('\n');
            }
        }
        System.out.println(sb);
    }
    // 이진 탐색 알고리즘 구현

    public static int binarySearch(int[] arr, int key) {

        int lo = 0;					// 탐색 범위의 왼쪽 끝 인덱스
        int hi = arr.length - 1;	// 탐색 범위의 오른쪽 끝 인덱스

        // lo가 hi보다 커지기 전까지 반복한다.
        while(lo <= hi) {

            int mid = (lo + hi) / 2;	// 중간위치를 구한다.

            // key값이 arr[mid] 값보다 작을 경우 : key는 arr[mid]의 왼쪽에 있어야 함
            if(key < arr[mid]) {
                // 탐색 범위를 왼쪽 절반으로 줄이기 위해 hi를 mid-1로 설정
                hi = mid - 1;
            }
            
            // key값이 arr[mid] 값보다 클 경우 : key는 arr[mid]의 오른쪽에 있어야 함
            else if(key > arr[mid]) {
                // 탐색 범위를 오쪽 절반으로 줄이기 위해 lo를 mid+1로 설정
                lo = mid + 1;
            }
            
            // key값과 중간 위치의 값이 같을 경우
            else {
                return mid;
            }
        }

        // 찾고자 하는 값이 존재하지 않을 경우
        return -1;

    }
}