import json

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDIctMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        # elif isinstance(value, '__dict__'):
        #     return self._traverse_dict(value.__dict__)
        # isinstance() arg 2 must be a type or tuple of types
        else:
            return value


class BinaryTree(ToDIctMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value
        else:
            return super()._traverse(key, value)

class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

# class JsonMixin(object):
#     @classmethod
#     def from_json(cls, data):
#         kwargs = json.loads(data)
#         return cls(**kwargs)

#     def to_json(self):
#         return json.dumps(self.to_dict())

# class DatacenterRack(ToDictMixin, JsonMixin):
#     def __init__(self, switch=None, machines=None):
#         self.switch = Switch(**switch)
#         self.machines = [
#             Machine(**kwargs) for kwargs in machines
#         ]

# class Switch(ToDictMixin, JsonMixin):
#     # ...

# class Machine(ToDictMixin, JsonMixin):
#     # ...

def main():
    tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)),
                      right=BinaryTree(13, left=BinaryTree(11)))
    print(tree.to_dict())

    root = BinaryTreeWithParent(10)
    root.left = BinaryTreeWithParent(7, parent=root)
    root.left.right = BinaryTreeWithParent(9, parent=root.left)
    print(root.to_dict())

    my_tree = NamedSubTree('foobar', root.left.right)
    print(my_tree.to_dict())

    # serialized = """{
    #     "switch": {"ports": 5, "speed": 1e9},
    #     "machines": [
    #         {"cores": 8, "ram": 32e9, "disk": 5e12},
    #         {"cores": 4, "ram": 16e9, "disk": 1e12},
    #         {"cores": 2, "ram": 4e9, "disk": 500e9}
    #     ]
    # }"""

    # deserialized = DatacenterRack.from_json(serialized)
    # roundtrip = deserialized.to_json()
    # assert json.loads(serialized) == json.loads(roundtrip)

if __name__ == '__main__':
    main()
