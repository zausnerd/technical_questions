#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find if the tree has a path from root to leaf such that the sum of all the node values of that path equal 'S'

Example 1
Input:
                        1
                    2       3
                  4   5   6   7
Output: 10
Explanation:  1 + 3 + 6



__History__
Needed Help:
No Help:
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    # TODO: Write your code here
    return False


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
