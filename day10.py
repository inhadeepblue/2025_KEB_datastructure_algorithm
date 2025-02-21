# 요세푸스 1158, 큐
from collections import deque  # 데크를 큐처럼 사용 (dequeue -> popleft, enqueue -> append, rotate)

# 입력
n, k = map(int, input().split())  # "7 3"

# 알고리즘
q = deque(range(1, n+1))  # 데크(큐) 객체 생성
r = list()  # 사망자 순서를 저장할 리스트

while q:
  q.rotate(-(k-1))
  r.append(q.popleft())  # 큐의 dequeue 다음에 리스트에 리턴된 사망자 번호를 추가

# 출력
print("<"+", ".join(map(str, r))+">")  # <3, 6, 2, 7, 5, 1, 4>
