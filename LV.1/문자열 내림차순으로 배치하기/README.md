### 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/12917

### **문제 설명**

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.

s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

### 제한 사항

- str은 길이 1 이상인 문자열입니다.

### 입출력 예

| s | return |
| --- | --- |
| "Zbcdefg" | "gfedcbZ" |

---

### 나의 풀이

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

처음엔 for문으로 문자열의 문자 하나씩 루프를 돌면서 짜려고 시도하다가 잊고 있던 join의 메서드로 더 쉽게 할 수 있다는 것이 생각났다. join 메서드는 리스트로 인자를 받기 때문에 문자열을 정렬해서 리스트로 반환하는 sorted 메서드로 s문자열을 정렬시키는데 reverse=True로 줘서 역순으로 정렬되어 마무리 했다.

### 성능 요약

0.01ms, 10.2MB

### 채점 결과

정확성: 100.0
합계: 100.0 / 100.0
