import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 동전의 종류
        int n = sc.nextInt();
        // 만들어야 될 값
        int k = sc.nextInt();

        // 입력한 n을 통해 동전의 종류 배열을 만든다 > 반복문으로
        int[] coin=new int[n];

        for(int i=0; i<n; i++){
            coin[i]=sc.nextInt();
        }

        // 거스름돈의 count 해야함
        int count=0;

        // coin을 큰 값에서 작은 값 순서대로 순회하기 위해 n-1로 초기화함
        for (int i=n-1; i>=0; i--){
            // coin[i]의 값이 남은 금액 k보다 작거나 같을 때 사용할 수 있도록 조건문 생성
            // 남은 금액을 줄이는 역할
            if(coin[i]<=k){ 
                count+=k/coin[i];
                k=k%coin[i];
            }
        }

        // 거스름돈 계수 카운팅

        System.out.println(count);
    }
}
