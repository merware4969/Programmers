### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12931

### **문제 설명**

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.

예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

### 제한사항

- N의 범위 : 100,000,000 이하의 자연수

---

### 입출력 예

| N | answer |
| --- | --- |
| 123 | 6 |
| 987 | 24 |

### 입출력 예 설명

입출력 예 #1

문제의 예시와 같습니다.

입출력 예 #2

9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.

---

### 나의 풀이

```python
def solution(n):
    list_n = list(n)
    for i range(list_n)    
        n/10^i + (n - (10^i)*(n/10^i))/10^i +  

    return answer
```

이런식으로 작성하려 했는데.. 음 너무 복잡해지는거 같다.. 좀 더 쉽게 할 수 없을까?

알아보니  “**`[char for char in "apple"]`**은 문자열 **`"apple"`**의 각 문자를 리스트의 요소로 추가” 한다는 사실을 알았다.
즉, 문자열을 for문의 in 범위로 주면 각 문자마다 순회한다.

```python
def solution(n):
    list_n = [num for num in str(n)]
    sum_n = sum(list_n)
    return sum_n
```

이런식으로 짜줬더니 에러가 나왔다. num이 문자형 그대로 들어가서 sum을 해줄 수가 없다. num을 int형으로 변경해야 한다.

```python
def solution(n):
    list_n = [int(num) for num in str(n)]
    sum_n = sum(list_n)
    return sum_n
```

에러 없이 잘 작동한다. ^^

### 가장 간결한 답

```python
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)
```

1. **기본 조건 확인 (종료 조건)**:
    
    ```python
    if number < 10:
        return number
    ```
    
    - 이 부분은 재귀 함수의 기본 조건입니다. **`number`**가 한 자릿수이면, 그대로 그 숫자를 반환합니다.
    - 예를 들어, **`number`**가 5이면 **`5`**를 반환합니다.
2. **재귀 호출 및 각 자릿수 합 계산**:
    
    ```python
    return number % 10 + sum_digit(number // 10)
    ```
    
    - 이 부분은 재귀 호출과 각 자릿수의 합을 계산하는 부분입니다.
    - **`number % 10`**은 **`number`**의 마지막 자릿수를 구합니다.
    - **`sum_digit(number // 10)`**은 **`number`**의 마지막 자릿수를 제외한 나머지 숫자에 대해 동일한 작업을 수행하는 재귀 호출입니다.
    - 각 호출에서 마지막 자릿수를 더하고, 재귀적으로 나머지 자릿수를 더한 결과를 반환합니다.
