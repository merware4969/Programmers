### 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/12930

### **문제 설명**

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

### 제한 사항

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

### 입출력 예

| s | return |
| --- | --- |
| "try hello world" | "TrY HeLlO WoRlD" |

### 입출력 예 설명

"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

---

### 나의 풀이

```python
def solution(s):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i].upper()
        else:
            s[i].lower()
    return s
```

문자열은 불변하기 때문에 기존 문자열에 upper, lower를 해줘도 문자열을 변경되지 않았다. 

```python
def solution(s):
    answer = []
    for i in range(len(s)):
        if i % 2 == 0:
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    answer = ''.join(answer)
    return answer
```

문자열이 아닌 새로운 배열을 만들어서  하나씩 문자를 추가해주고 join으로 다시 문자열로 반환시켜주었다. 그럼에도 에러가 떴는데 문제를 다시 읽어보니 전체 문자열 기준 인덱스가 아니라 단어별 인덱스였다. 문자열 사이 공백이 있으면 그 기준으로 다시 인덱스를 카운팅 해야 하는 것이다.

```python
def solution(s):
    words = s.split(' ')
    answers = []
    for word in words:
        answer = []
        for i in range(len(word)):
            if i % 2 == 0:
                answer.append(word[i].upper())
            else:
                answer.append(word[i].lower())
        answers.append(''.join(answer))
    answers = ' '.join(answers)
    return answers
```

생각보다 너무 어려웠다. s 전체 문자열을 split(’ ‘) 공백으로 나누어 각 단어들을 저장하고 for문 이후 단어들을 담을 answers를 선언하고 for문 안에 단어 하나씩을 담을 answer를 선언해주었다. for문을 이중으로 써야하니 많이 헷갈렸다.

### 성능 요약

0.05ms, 10.2MB

### 채점 결과

정확성: 100.0
합계: 100.0 / 100.0
