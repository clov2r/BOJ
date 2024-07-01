import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 번째 줄에서 입력받은 n (문자열의 개수)
        int n = Integer.parseInt(br.readLine());
        
        // n개의 문자열을 순차적으로 처리
        for (int i = 0; i < n; i++) {
            // 문자열 입력 받기
            String input = br.readLine();
            // 알파벳의 출현 빈도를 저장할 배열
            int[] result = new int[26];
            
            // 입력 문자열을 한 글자씩 처리
            for (int j = 0; j < input.length(); j++) {
                // 소문자 알파벳인 경우에만 빈도 수 증가
                if (input.charAt(j) >= 'a' && input.charAt(j) <= 'z') {
                    result[input.charAt(j) - 'a']++;
                }
            }

            // 가장 많이 출현한 알파벳의 빈도를 저장할 변수
            int max = 0;
            // 배열을 순회하며 최대 빈도 값 찾기
            for (int r : result) {
                if (r > max) {
                    max = r;
                }
            }

            // 가장 많이 출현한 알파벳이 여러 개인지 확인하기 위한 변수들
            int count = 0;
            int answer = 0;
            for (int j = 0; j < 26; j++) {
                if (max == result[j]) {
                    count++;
                    answer = j;
                }
            }

            // if 조건문을 사용하여 결과 출력
            if (count == 1) {
                System.out.println((char) (answer + 'a'));
            } else {
                System.out.println("?");
            }
        }
    }
}
