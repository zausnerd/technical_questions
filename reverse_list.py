#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Given the head of a singly linked list, reverse the list.
    Input:    HEAD
                2
                4
                6
                8
                10
                null
    Output:    HEAD
                10
                8
                6
                4
                2

First completed 01/19/2020 with help
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    while head is not None:
        print(head.value)
        head = head.next


def reverse_list(head):
    first = None
    second = head
    while second is not None:
        third = second.next
        second.next = first
        first = second
        second = third
    return first


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ")
    print_list(head)
    result = reverse_list(head)
    print("Nodes of reversed LinkedList are: ")
    print_list(result)

main()
