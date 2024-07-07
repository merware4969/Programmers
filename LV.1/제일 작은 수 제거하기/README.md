### 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/12935

### **문제 설명**

정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

### 제한 조건

- arr은 길이 1 이상인 배열입니다.
- 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

### 입출력 예

| arr | return |
| --- | --- |
| [4,3,2,1] | [4,3,2] |
| [10] | [-1] |

---

### 나의 풀이

```python
def solution(arr):
    for i in range(len(arr)):
        if arr[i] == min(arr):
            arr = arr[:i] + arr[i+1:]
    if len(arr) == 0:
        arr = [-1]
    return arr
```

for 문을 사용하여 작성해 보았지만 시간초과와 런타임 에러가 났다. for문 없이 할 수 있는 방법이 없을까

```python
def solution(arr):
    idx = arr.index(min(arr))
    arr = arr[:idx] + arr[idx+1:]
    if len(arr) == 0:
        arr = [-1]
    return arr
```

list 배열의 index를 반환하기 위해 for문 대신 .index() 메서드를 사용했다.

### 성능 요약

0.04ms, 10.3MB

### 채점 결과

정확성: 100.0
합계: 100.0 / 100.0
