### 문제 링크

[](https://programmers.co.kr/learn/courses/30/lessons/12922)

### **문제 설명**

길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

### **제한 조건**

n은 길이 10,000이하인 자연수입니다.

![입출력 예시](https://blog.kakaocdn.net/dn/cDFlSX/btshrxGBO2H/kWP0IEjnIBj58M319GKUW0/img.png)

입출력 예시

---

### 나의 풀이

n의 값이 짝수냐 홀수냐에 따라 경우가 달라지기 때문에 if문으로 짝수 홀수 경우를 나누고 '수박'이라는 문자열을 만들어 2로 n을 나눈 값으로 문자열을 곱해 반복시켰다.

```python
def solution(n):
    answer = ''
    if n%2 == 0:
        answer = '수박'*(n/2)
        return answer
    elif n%2 != 0:
        answer = '수박'*(n/2) + '수'
        return answer
```

하지만 에러가 나왔고 n의 값이 실수형일 때 에러가 난다고 하는것 같다.

따라서 '/' 대신 정수 몫을 구해주는 '//' 으로 바꾸어주었더니 에러가 나지 않고 잘 실행되었다.

```python
def solution(n):
    answer = ''
    if n%2 == 0:
        answer = '수박'*(n//2)
        return answer
    elif n%2 != 0:
        answer = '수박'*(n//2) + '수'
        return answer
```
