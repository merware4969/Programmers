### 문제 링크

[](https://programmers.co.kr/learn/courses/30/lessons/12954#qna)

### **문제 설명**

함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

### **제한 조건**

- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.

### **입출력 예**

| x | n | answer |
| --- | --- | --- |
| 2 | 5 | [2,4,6,8,10] |
| 4 | 3 | [4,8,12] |
| -4 | 2 | [-4, -8] |

---

### 나의 풀이

```python
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + (i * x))
    return answer
```

한 번에 처음으로 코드가 에러 없이 실행된거 같다. 내 풀이는 answer라는 배열을 만든 후 그 배열에 append로 x와 x를 n의 수만큼 반복해서 더하는 방식으로 풀었다.

### 가장 간결한 답

```python
def number_generator(x, n):
    return [i * x + x for i in range(n)]
```

위 답은 훨씬 더 간결하게 한줄로 코드를 만들었다. for문 자체를 아예 한 줄에 넣어서 사용해도 에러 없이 잘 나온다. 배열 자체를 return하고 안에 for문을 넣어서 완성한 걸 보니 같은 풀이로도 더 간단하게 풀 수 있는 것을 알았다.
