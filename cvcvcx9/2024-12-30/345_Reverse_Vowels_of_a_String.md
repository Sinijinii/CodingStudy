```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 시간초과 실패
        # vowel_list = set(['a','e','i','o','u','A','E','I','O','U'])
        # vowel_index = []
        # vowel_stack = []
        # result = []
        # for index,v in enumerate(s):
        #     if v in vowel_list:
        #         vowel_index.append(index)
        #         vowel_stack.append(v)
        
        # for i in range(len(s)):
        #     if i in vowel_index:
        #         tmp = vowel_stack.pop()
        #         result.append(tmp)
        #     else:
        #         result.append(s[i])
        # return "".join(result)
        
        # 모음 리스트
        vowels = set('aeiouAEIOU')
        # 모음 저장
        vowel_stack = [ch for ch in s if ch in vowels]
        
        # 결과 문자열 생성
        result = []
        for ch in s:
            if ch in vowels:
                # 역순으로 모음을 가져와 대체
                result.append(vowel_stack.pop())
            else:
                # 모음이 아니면 그대로 추가
                result.append(ch)
        
        # 리스트를 문자열로 변환 후 반환
        return ''.join(result)
```