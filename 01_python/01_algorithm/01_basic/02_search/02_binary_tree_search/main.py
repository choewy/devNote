# 이진트리 : 노드의 최대 Branch가 2인 트리
# 이진탐색트리(binary search tree, BST) : 왼쪽 노드에는 해당 노드보다 작은 값, 오른쪽 노드에는 해당 노드보다 큰 값을 가진 이진트리
# 이진트리탐색 : 이진탐색트리를 통해 찾고자 하고자 하는 데이터를 탐색
# 시간복잡도 : 평균적으로 O(Log₂n)이지만, 모든 노드가 최상위 노드보다 클 경우는 O(n)


class Node:
    def __init__(self, node):
        self.node = node
        self.left, self.right = None, None


class NodeTree:
    def __init__(self, head):
        self.head = head
        self.current_node = None
        self.parent_node = None
        self.change_node = None
        self.change_parent_node = None

    def insert(self, node):
        self.current_node = self.head
        while True:
            if node < self.current_node.node:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(node)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(node)
                    break

    def search(self, node):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.node == node:
                return True
            elif node < self.current_node.node:
                self.current_node = self.current_node.left
                print(self.current_node.node)
            else:
                self.current_node = self.current_node.right
                print(self.current_node.node)
        return False

    def delete(self, node):
        exits = False

        self.current_node = self.head
        while self.current_node:
            if self.current_node.node == node:
                exits = True
                break
            elif node < self.current_node.node:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right

        if not exits:
            return False

        if not self.current_node.left and not self.current_node.right:
            if node < self.parent_node.node:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

        elif self.current_node.left and not self.current_node.right:
            if node < self.parent_node.node:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left

        elif not self.current_node.left and self.current_node.right:
            if node < self.parent_node.node:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right

        elif self.current_node.left and self.current_node.right:
            if node < self.parent_node.node:
                self.change_node = self.current_node.right
                self.change_parent_node = self.current_node.right

                while self.change_node.left:
                    self.change_parent_node = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right:
                    self.change_parent_node.left = self.change_node.right
                else:
                    self.change_parent_node.left = None

                self.parent_node.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

            else:
                self.change_node = self.current_node.right
                self.change_parent_node = self.current_node.right

                while self.change_node.left:
                    self.change_parent_node = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right:
                    self.change_parent_node.left = self.change_node.right
                else:
                    self.change_parent_node.left = None

                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.change_node.right

        return True

    def inquiry(self, head):
        if head is None:
            return []

        return self.inquiry(head.left) + [head.node] + self.inquiry(head.right)
