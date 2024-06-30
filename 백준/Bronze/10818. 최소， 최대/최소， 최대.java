import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt(); // 배열의 크기 입력 받음
        sc.nextLine(); // 버퍼 채우기 (왜 채워야 하지?)

        // 배열의 원소를 한 줄로 입력 받아 배열로 저장
        String num=sc.nextLine();
        String[] stringNumbers=num.split(" ");
        int[] numbers=new int[T];

        // 문자열 배열을 정수 배열로 변환
        for(int i=0; i<T; i++){
            numbers[i]=Integer.parseInt(stringNumbers[i]);
        }

        // 배열에 있는 요소 최대값 최소값 구하기
        int min= Arrays.stream(numbers).min().getAsInt();
        int max= Arrays.stream(numbers).max().getAsInt();

        System.out.printf("%d %d",min, max);
    }
}
