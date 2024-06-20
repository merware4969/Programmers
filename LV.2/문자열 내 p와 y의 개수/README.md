### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12916

### **문제 설명**

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

### 제한사항

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

### 입출력 예

| s | answer |
| --- | --- |
| "pPoooyY" | true |
| "Pyy" | false |

### 입출력 예 설명

입출력 예 #1

'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2

'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.

---

### 나의 풀이

```python
def solution(s):
    p_list = []
    y_list = []
    s = list(s)
    if [p,P,y,Y] in s:
        for c in range(s):
            if c == p:
                p_list.append(c)
            elif c == P:
                p_list.append(c)
            elif c == y:
                y_list.append(c)
            elif c == Y:
                y_list.append(c)
        if len(p_list) == len(y_list):
            return True
        return False
```

일단 무식하게 p,P,y,Y가 s 안에 들어있는지 if 문을 만들고 각각 다 p랑y가 있는 경우를 if문으로 만들어주고 p_list와 y_list 각각 안에 넣어 길이가 같으면 True가 나오게끔 해주었다.

**NameError: name 'p' is not defined**

라는 에러가 떴다. 아마 p, P, y, Y라는 변수를 지정해주지 않아서 그런 것 같다.

각각 p와 y의 count 값을 0으로 셋팅해놓고 반복문으로 값을 하나씩 추가해주는 것으로 비교하여 같으면 True로 아니면 False로 나오게 해주었다.

```python
def solution(s):
    p_count = 0
    y_count = 0
    
    for char in s:
        if char in 'pP':
            p_count += 1
        elif char in 'yY':
            y_count += 1
    
    return p_count == y_count
```
### 성능 요약
통과 (0.01ms, 10.1MB)
### 채점 결과
정확성: 100.0\
합계: 100.0 / 100.0

### 제일 간결한 답:

```python
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
#print( numPY("pPoooyY") )
#print( numPY("Pyy") )
```

lower 함수를 통해 문자열의 대문자 P, Y를 소문자로 바꾸고 count()라는 집계함수를 이용해 수를 세주었다.
