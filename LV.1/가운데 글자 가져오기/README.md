### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12903

### **문제 설명**

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

### 재한사항

- s는 길이가 1 이상, 100이하인 스트링입니다.

### 입출력 예

| s | return |
| --- | --- |
| "abcde" | "c" |
| "qwer" | "we" |

---

### 나의 풀이

```python
def solution(s):
    if len(s)%2 == 1:
        return s[(len(s)/2)]
    elif len(s)%2 == 0:
        return s[(len(s)/2)-1] + s[(len(s)/2)]
```

에러가 떠서 보니 파이썬에서 인덱싱을 할 때 정수 나눗셈(**`//`**)을 사용해야 한다고 한다. 내가 사용한 일반 나눗셈(**`/`**)은 부동 소수점 숫자를 반환한다고 한다.

```python
def solution(s):
    if len(s)%2 == 1:
        return s[(len(s)//2)]
    elif len(s)%2 == 0:
        return s[(len(s)//2)-1] + s[(len(s)//2)]
```

/를 //로 바꾸니 오류 없이 정상 출력했다.

### 가장 간결한 답

```python
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
```

(len(str)-1)//2 이부분이 짝수냐 홀수냐에 상관없이 만든다. 인덱스는 항상 0 번째부터 출발하니까, length를 아예 1을 빼버리고 //2를 한다면 짝수는 1을 하나 더빼서 그전의 인덱스부터 가져올 수 있다… ㄷㄷ

power 즉 홀수는 str[2:3] 으로 나오니 파이썬의 슬라이싱은 2부터 3이전까지를 의미하니 w하나만이 출력된다. ㄷㄷ
