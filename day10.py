from typing import List
class Node:
    def __init__(self, value):
        self.value = value
        self.link = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


    def append(self, value):
        new_node = Node(value)
        if not self.head:  # 원형 링크드 리스트 첫 번째 노드가 추가 되면
            self.head = new_node  # 첫 번째 노드가 head
            new_node.link = self.head  # 자기 자신을 가르키는 노드로 셋업
        else:
            current = self.head
            while current.link != self.head:  # 맨 마지막 노드까지 반복 (노드가 헤드를 가르키지 않는 경우 loop)
                current = current.link
            current.link = new_node  # 현재 헤드였던 노드는 더 이상 헤드가 아니고 새노드를 가르킨다
            new_node.link = self.head  # 마지막에 생성된 노드는 헤드를 가르키도록 한다 (원형 링크드 리스트 유지)


    def josepush(self, k) -> List:
      r = list()  # 사망자를 순서대로 저장할 리스트
      current = self.head

      while current.link != current:  # 최후의 1인이 남을 때 까지
        for _ in range(k-1):
          current = current.link  # 노드 이동
        r.append(current.value)  # 사망자 추가

        if current == self.head:  # 삭제될 노드가 head
          self.head = self.head.link  # head 다음 노드로 head를 update
        # 원형 링크드 리스트에서 삭제된 노드 앞뒤 노드를 연결하는 작업
        prev = self.head
        while prev.link != current:
          prev = prev.link  # prev 이동
        prev.link = current.link  # 삭제될 노드의 링크를 이전 노드에게 전달
        current = prev.link  # 새로운 current (삭제된 노드 바로 앞 노드)

      r.append(current.value)
      return r


n, k = map(int, input().split())  # "7 3"
circular_linked_list = CircularLinkedList()

for i in range(1, n+1):
  circular_linked_list.append(i)

result = circular_linked_list.josepush(k)  # [3, 6, 2, 7, 5, 1, 4]
# join / str / map
# result = [3, 6, 2, 7, 5, 1, 4]
print("<"+", ".join(map(str, result))+">")  # <3, 6, 2, 7, 5, 1, 4>
