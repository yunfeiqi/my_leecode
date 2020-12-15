#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/12/14 21:08:27
@Author  :   sam.qi
@Version :   1.0
@Desc    :   二叉树广度优先-层序遍历
'''


from typing import OrderedDict


class TreeNode(object):
    def __init__(self, left, right, value: int) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.value = value


class LevelOrder(object):
    '''
        二叉树层序遍历
    '''

    def level_order(self, node):
        # defination
        values = []
        stack = []

        stack.append(node)
        while len(stack) > 0:
            cur_level_cnt = len(stack)
            layer_values = []
            for idx in range(cur_level_cnt):
                # pop and append value
                _node = stack.pop()
                layer_values.append(_node.value)

                # left insert
                if _node.left is not None:
                    stack.insert(0, _node.left)

                # right insert
                if _node.right is not None:
                    stack.insert(0, _node.right)

            if len(layer_values) > 0:
                values.append(layer_values)

        # return
        return values


if __name__ == "__main__":
    node1 = TreeNode(None, None, 1)
    node2 = TreeNode(None, None, 2)
    node3 = TreeNode(node1, node2, 3)
    node4 = TreeNode(node3, None, 4)
    node5 = TreeNode(None, None, 5)
    node6 = TreeNode(node4, node5, 6)

    print("***********层序遍历****************")
    order = LevelOrder()

    print("层序遍历:{}".format(order.level_order(node6)))
