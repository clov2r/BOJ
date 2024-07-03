import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        int M=sc.nextInt();

        int gdc=0; // 최대공약수
        for (int i=1; i<=N && i<=M; i++){
            if(N%i==0 && M%i==0){
                gdc=i;
            }
        }
        int lcm=N*M/gdc;
        System.out.println(gdc);
        System.out.println(lcm);
    }
}