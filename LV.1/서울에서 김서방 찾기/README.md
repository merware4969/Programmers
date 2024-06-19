### 문제 링크 ****

https://programmers.co.kr/learn/courses/30/lessons/12919

### **문제 설명**

String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

### **제한 사항**

seoul은 길이 1 이상, 1000 이하인 배열입니다.

seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.

"Kim"은 반드시 seoul 안에 포함되어 있습니다.

![입출력 예](https://blog.kakaocdn.net/dn/brDrIb/btsjqwzACqF/190RQwApjcEk2dTDSb6W80/img.png)

입출력 예

---

### 나의 풀이

```python
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 {}에 있다'.format(i)

    return answer
```

for문이나 if문을 생략하고 더 간략히 만들 수도 있을 것 같다.

최적의 답안은 아래 코드인데, index를 사용해서 훨씬 간단하게 코드를 줄였다.

```python
def findKim(seoul):
	# 함수를 완성하세요
	return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))
```
