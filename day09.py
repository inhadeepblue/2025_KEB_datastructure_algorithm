class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def insert(root, value):
    if root is None:
        node = TreeNode()
        node.data = value
        return node

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    current = root
    while current:
        if value == current.data:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return None


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data} ", end='')


def delete(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:  # 자식이 두 개인 경우
            root.data = find_min(root.right).data
            root.right = delete(root.right, root.data)
    return root


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    while True:
        print("\n--- 트리 관리 메뉴 ---")
        print("1. 값 삽입")
        print("2. 값 삭제")
        print("3. 값 찾기")
        print("4. 트리 확인 (후위 오더)")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        if choice == '1':
            value = int(input("삽입할 값을 입력하세요: "))
            root = insert(root, value)
            print(f"{value} 삽입 완료")
        elif choice == '2':
            value = int(input("삭제할 값을 입력하세요: "))
            if search(root, value):
                root = delete(root, value)
                print(f"{value} 삭제 완료")
            else:
                print(f"{value}은(는) 트리에 존재하지 않습니다.")
        elif choice == '3':
            value = int(input("찾고 싶은 값을 입력하세요: "))
            if search(root, value):
                print(f"{value}을(를) 찾았습니다.")
            else:
                print(f"{value}이(가) 존재하지 않습니다.")
        elif choice == '4':
            post_order(root)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")