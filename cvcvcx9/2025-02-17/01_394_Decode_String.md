## 처음 시도한 코드
```java
class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        Stack<Integer> mulStack = new Stack<>();
        Stack<String> wordStack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for(char c: s.toCharArray()){
            if(Character.isDigit(c)){
                mulStack.push((int)c-'0');
            }
            else if(c == '['){
                stack.push('[');
                wordStack.push(sb.toString());
                sb = new StringBuilder();
            }
            else if(c == ']'){
                stack.pop();
                int mulVal =  mulStack.pop();
                for(int i=1;i<mulVal;i++){
                    sb.append(sb.toString());
                }
                
                String word = wordStack.pop();
                sb = new StringBuilder(word+sb.toString());
                
            }
            else if(Character.isAlphabetic(c)){
                sb.append(c);
            }
        }
        
        System.out.println(sb.toString());
        return "";
    }
}
```

## 정답코드드
```java
class Solution {
   public String decodeString(String s) {
        Stack<Integer> mulStack = new Stack<>();  // 숫자 저장 스택
        Stack<StringBuilder> wordStack = new Stack<>();  // 문자열 저장 스택
        StringBuilder sb = new StringBuilder();
        int num = 0; // 숫자 저장 변수

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');  // 다자리 숫자 처리
            } else if (c == '[') {
                mulStack.push(num);  // 숫자 스택에 저장
                wordStack.push(sb);  // 현재까지의 문자열 저장
                sb = new StringBuilder();  // 새로운 문자열 시작
                num = 0;  // 숫자 초기화
            } else if (c == ']') {
                int repeatCount = mulStack.pop();  // 반복 횟수 가져오기
                StringBuilder temp = new StringBuilder();
                for (int i = 0; i < repeatCount; i++) {
                    temp.append(sb);
                }
                sb = wordStack.pop().append(temp);  // 이전 문자열과 합치기
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```