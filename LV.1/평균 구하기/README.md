### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

### **문제 설명**

정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

### **제한사항**

- arr은 길이 1 이상, 100 이하인 배열입니다.
- arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

### **입출력 예**

| arr | return |
| --- | --- |
| [1,2,3,4] | 2.5 |
| [5,5] | 5 |

---

### 나의 풀이

```python
def solution(arr):
    answer = sum(arr) / len(arr)
    return answer
```

생각보다 쉽다. 그냥 받은 배열의 합을 길이로 나눠주었다.

### 가장 간결한 답

```python
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return sum(list) / len(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
```

가장 간결한 답이랑 똑같긴 한데 따로 변수 지정을 안해주고 바로 return을 한게 차이라면 차이다.
