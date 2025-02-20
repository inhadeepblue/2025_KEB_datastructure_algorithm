class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return root


def search(root, value):
    current = root
    while True:
        if value == current.data:
            print(f"{value}을(를) 찾았습니다")
            break
        elif value < current.data:
            if current.left is None:
                print(f"{value}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{value}이(가) 존재하지 않습니다")
                break
            current = current.right


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data} ", end='')


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)

    print()
    find_number = int(input())
    search(root, find_number)
