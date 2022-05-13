#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_binary_tree(indexes):
    node_list = [None for _ in range(len(indexes))]

    for idx in range(len(indexes)):
        node = Node(idx + 1)
        node_list[idx] = node

    for idx in range(len(indexes)):
        left, right = indexes[idx]
        node = node_list[idx]
        if left != -1:
            node.left = node_list[left - 1]
        if right != -1:
            node.right = node_list[right - 1]

    return node_list


def swap(node_list, node):
    node_inst = node_list[node - 1]
    node_inst.left, node_inst.right = node_inst.right, node_inst.left


def dfs(node, result):
    if not node:
        return
    dfs(node.left, result)
    result.append(node.val)
    dfs(node.right, result)


def walk(root):
    result = []
    dfs(root, result)
    return result


def swapNodes(indexes, queries):
    # Write your code here
    node_list = build_binary_tree(indexes)
    root = node_list[0]
    result = []
    for query in queries:
        swap(node_list, query)
        result.append(walk(root))

    return result


if __name__ == '__main__':
    n = 17
    indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13],
               [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1],
               [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    queries_count = 2
    queries = [2, 3]

    result = swapNodes(indexes, queries)
    print(result)
