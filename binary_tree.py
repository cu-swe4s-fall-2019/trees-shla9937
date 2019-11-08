class Node:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.value[0] == data[0]:
            self.value.append(data[1])
            return False
        elif self.value[0] > data[0]:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def search(self, key):
        if self.value[0] == key:
            return self.value
        elif self.value[0] > key:
            if self.left_child:
                return self.left_child.search(key)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.search(key)
            else:
                return False


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def search(self, key):
        if self.root:
            return self.root.search(key)
        else:
            return False


if __name__ == '__main__':
    None
