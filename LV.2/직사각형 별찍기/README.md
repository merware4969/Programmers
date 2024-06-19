### 문제 링크

https://programmers.co.kr/learn/courses/30/lessons/12969

### **문제 설명**

이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.

별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

---

### 제한 조건

- n과 m은 각각 1000 이하인 자연수입니다.

---

### 예시

입력

`5 3`

출력

`*****
*****
*****`

---

### 나의 풀이

```python
a, b = map(int, input().strip().split(' '))
for i in b:
    print(a * "*" , "\n " * i)
```

위 코드로 처음에 작성하니 Type Error가 떴다. for문에서 범위 b를 int값으로 줘서 에러가 떴나보다. range(b)로 고쳐보았다.

```python
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print(a * "*" , "\n " * i)
```

바보같은 실수를 했다. 줄바꿈을 해주는 이스케이프 문자 “\n”을 사용했는데 거기에 i를 곱해버리니 그 줄만큼을 띄워버리더라.. 어떻게 손대야 할까.. 흠..

검색해서 알아보니 for문에서 굳이 i와 같은 변수를 사용할 필요 없다더라.. i를 빼고 아니면 i를 조건문에 적었지만 사용하지 않고도 for문으로 반복을 시행할 수 있다.

```python
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print(a * "*")
```

관습적으로 보통 _를 쓴다는데 i를 넣고 돌려도 올바르게 작동한다.

### 가장 간결한 답

```python
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
```

for문을 사용하지 않고 문자열로 완성하는 방법도 있다..
