class TreeObj:

    def __init__(self, indx: int, value: str =None) -> None:
        self.index = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self) -> "TreeObj":
        return self.__left

    @left.setter
    def left(self, obj: "TreeObj") -> None:
        self.__left = obj

    @property
    def right(self) -> "TreeObj":
        return self.__right

    @right.setter
    def right(self, obj: "TreeObj") -> None:
        self.__right = obj


class DecisionTree:

    @classmethod
    def predict(cls, root: "TreeObj", x: list):
        obj = root
        indx = obj.index
        while True:
            if obj.left and obj.right:
                if x[indx]:
                    obj = obj.left
                    indx = obj.index
                else:
                    obj = obj.right
                    indx = obj.index
            else:
                break
        return obj.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: "TreeObj" = None, left: bool = True) -> "TreeObj":
        if node:
            if left:
                node.left = obj
                return node.left
            else:
                node.right = obj
                return node.right
        else:
            return obj




assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"