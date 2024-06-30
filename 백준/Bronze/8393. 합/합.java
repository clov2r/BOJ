import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt(); // testcase
        int res=0;
        for(int i=1; i<T+1; i++){
            res+=i;
        }
        System.out.println(res);
    }
}
