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

    print("BST 구성 완료")
    post_order(root)

    print()
    print(root.data)
    # find_number = int(input())
    # if search(root, find_number):
    #     print(f"{find_number}을(를) 찾았습니다")
    # else:
    #     print(f"{find_number}이(가) 존재하지 않습니다")

    delete_number = int(input())
    if search(root, delete_number):
        root = delete(root, delete_number)
        print(f"{delete_number} 삭제 완료")
    else:
        print(f"{delete_number}은(는) 트리에 존재하지 않습니다.")

    post_order(root)
    print()
    print(root.data)