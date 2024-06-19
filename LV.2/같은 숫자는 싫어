### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12906

### **문제 설명**

배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

- arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
- arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

### 제한사항

- 배열 arr의 크기 : 1,000,000 이하의 자연수
- 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

### 입출력 예

| arr | answer |
| --- | --- |
| [1,1,3,3,0,1,1] | [1,3,0,1] |
| [4,4,4,3,3] | [4,3] |

### 입출력 예 설명

입출력 예 #1,2

문제의 예시와 같습니다.

---

### 나의 풀이

answer라는 배열에 이미 arr[0]인 즉, 첫번째 값을 미리 넣어두고 range(1, len(arr))을 통해 2번째 값부터 반복하게끔 짜놓았다.

```python
def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
```

### 제일 간결한 답:

```python
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
```

a 배열의 마지막 값 (a[-1:])이 [i]와 같으면 continue로 반복을 건너뛰어버린다. 그렇지 않으면 아래에 append로 i 값만을 a 배열에 추가한다.

continue라는 함수를 새로 알게되었다.
