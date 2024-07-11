### 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/12948

### **문제 설명**

프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.

전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 `*`으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건

- phone_number는 길이 4 이상, 20이하인 문자열입니다.

### 입출력 예

| phone_number | return |
| --- | --- |
| "01033334444" | "*******4444" |
| "027778888" | "*****8888" |

---

### 나의 풀이

```python
def solution(phone_number):
    answer = []
    for i in range(len(phone_number)):
        if i < len(phone_number)-4:
            answer.append("*")
        elif i == len(phone_number)-4:
            answer.append(phone_number[i])
        elif i > len(phone_number)-4:
            answer.append(phone_number[i])
    return "".join(answer)
```

새로운 문자열 answer를 만들고 끝 4자리 이전까진 *로 채우고 그 이후에는 원래 받는 phone_number 각 index에 해당되는 값을 넣어주었다.

### 성능 요약

0.01ms, 10.4MB

### 채점 결과

정확성: 100.0
합계: 100.0 / 100.0

### 가장 간결한 답

```python
def hide_numbers(s):
	return "*"*(len(s)-4)+s[-4:]
```

문자열에 곱셈이 된다는 사실을 배웠다. 언젠가 요긴하게 써먹을 수 있을 것 같다.
