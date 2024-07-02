import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String T=sc.next(); // 대소문자로 이루어진 단어 입력
        String T2=T.toUpperCase(); // 대소문자 구분 X라서 대문자로 올려버림

        // 문자열을 한 글자씩 순회하면서 등장 횟수를 계산
        Map<Character, Integer> charCountMap= new HashMap<>();
        for (char c:T2.toCharArray()){
            if(charCountMap.containsKey(c)){
                charCountMap.put(c, charCountMap.get(c)+1);
            }
            else {
                charCountMap.put(c, 1);
            }
        }

        // 가장 많이 등장한 문자 찾기
        char maxChar = ' ';
        int maxCount = 0;
        boolean isTie = false;

        for (Map.Entry<Character, Integer> entry : charCountMap.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxChar = entry.getKey();
                maxCount = entry.getValue();
                isTie = false; // 새 최대값이 발견되면 타이 상태 초기화
            } else if (entry.getValue() == maxCount) {
                isTie = true; // 같은 최대값이 발견되면 타이 상태로 설정
            }
        }

        // 결과 출력
        if (isTie) {
            System.out.println("?");
        } else {
            System.out.println(maxChar);
        }
    }
}
