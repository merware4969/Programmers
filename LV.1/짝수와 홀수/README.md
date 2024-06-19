### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12937

### **문제 설명**

정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

### 제한 조건

- num은 int 범위의 정수입니다.
- 0은 짝수입니다.

### 입출력 예

| num | return |
| --- | --- |
| 3 | "Odd" |
| 4 | "Even" |

---

### 나의 풀이

```python
def solution(num):
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"
```

한 줄로 작성해볼 순 없을까..

### 가장 간결한 답

```python
def evenOrOdd(num):
    #함수를 완성하세요
    if num%2:
        return "Odd"

    return "Even"
```
