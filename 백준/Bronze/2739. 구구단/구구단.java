import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt(); // testcase
        for(int i=1; i<10; i++){
            System.out.printf("%d * %d = %d\n",T,i,T*i);
        }
    }
}