#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2020/12/14 20:04:02
@Author  :   sam.qi
@Version :   1.0
@Desc    :   二叉树深度优先遍历,前序、中序、后序
'''


from typing import ValuesView


class TreeNode(object):
    def __init__(self, left, right, value: int) -> None:
        super().__init__()
        self.left = left
        self.right = right
        self.value = value


class Recurssive(object):
    '''
        基于递归的方法实现
    '''

    def traversal_leftorder(self, node):
        '''
            DFS-前序遍历
        '''

        values = []

        def leftorder(node):
            # terminator
            if node is None:
                return
            values.append(node.value)
            leftorder(node.left)
            leftorder(node.right)

        leftorder(node)
        return values

    def traversal_inorder(self, node):
        '''
            DFS-中序遍历
        '''
        values = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.value)
            inorder(node.right)
        inorder(node)
        return values

    def traversal_postorder(self, node):
        values = []

        def post_order(node):
            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            values.append(node.value)

        post_order(node)
        return values


class Stack(object):
    '''
        基于推栈方式实现
        使用堆栈模拟循环
    '''

    def traversal_leftOrder(self, node):
        '''
            DFS-前序遍历
        '''
        # defination
        values = []
        stack = []

        # terminator
        if node is None:
            return values

        stack.append(node)

        # process
        while len(stack) > 0:
            _node = stack.pop()
            if _node is not None:
                values.append(_node.value)

                # 堆栈特点-需要先把right入栈
                stack.append(_node.right)
                stack.append(_node.left)

        return values

    def traversal_inOrder(self, node):
        '''
            DFS-中序遍历
        '''
        values = []
        stack = []

        while node or stack:
            if node is not None:
                # 一直将左子树压入栈内
                stack.append(node)
                node = node.left
            else:
                # 去除父节点
                _node = stack.pop()
                values.append(_node.value)
                # 遍历当前节点右子树
                node = _node.right

        return values

    def traversal_postOrder(self, node):
        '''
            DFS-后序遍历
            后序遍历只需要将 root right left 逆序就可以
        '''
        # defination
        values = []
        stack = []

        stack.append(node)
        while len(stack) > 0:
            _node = stack.pop()
            if _node is not None:
                values.append(_node.value)
                stack.append(_node.left)
                stack.append(_node.right)

        values.reverse()
        return values


if __name__ == "__main__":
    node1 = TreeNode(None, None, 1)
    node2 = TreeNode(None, None, 2)
    node3 = TreeNode(node1, node2, 3)
    node4 = TreeNode(node3, None, 4)
    node5 = TreeNode(None, None, 5)
    node6 = TreeNode(node4, node5, 6)

    print("***********递归方法****************")
    recur = Recurssive()
    print("前序遍历:{}".format(recur.traversal_leftorder(node6)))
    print("中序遍历:{}".format(recur.traversal_inorder(node6)))
    print("后序遍历:{}".format(recur.traversal_postorder(node6)))

    print("***********堆栈方法****************")
    stack = Stack()
    print("前序遍历:{}".format(stack.traversal_leftOrder(node6)))
    print("中序遍历:{}".format(stack.traversal_inOrder(node6)))
    print("后序遍历:{}".format(stack.traversal_postOrder(node6)))
