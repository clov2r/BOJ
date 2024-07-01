import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt(); // 입력한 N
        String num=sc.next(); // 입력한 N의 길이만큼 숫자 N개가 나열된 문자열
        String arr[]=num.split(""); // num을 공백없이 자름
        
        int sum=0;
        // 각 문자를 정수로 변환하여 합산하기 위한 반복문 작성
        for(int i=0; i< arr.length; i++){
            sum+=Integer.parseInt(arr[i]);
        }
        
        System.out.println(sum);
        
    }
}