#Binary tree data structure
class TreeNode:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addNode(self, TreeNode):
        self.children.append(TreeNode)

t = TreeNode('Drinks', [])
t2 = TreeNode('Cold', [])
t3 = TreeNode('Hot', [])
t.addNode(t2)
t.addNode(t3)

print(t)