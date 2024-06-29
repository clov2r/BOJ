import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // A+B 받는건데 그럼 그냥 True를 쓰면 될텐데 왜 hasNextInt를 쓰는 거디
        while (scanner.hasNextInt()) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            System.out.println(A + B);
        }
        scanner.close();
    }
}