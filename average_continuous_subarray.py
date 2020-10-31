#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
    Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
    (1+3+2+6−1)/5=>2.2
    (3+2+6−1+4)/5=>2.8
    (2+6−1+4+1)/5=>2.4
    ...
    Output: [2.2, 2.8, 2.4, 3.6, 2.8]

    https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr
"""


def find_averages_of_subarrays(size, array):
    first = 0
    second = size - 1
    total = sum(array[0:second + 1])
    averages = [total / size]
    second += 1
    while second < len(array):
        total += (array[second] - array[first])
        first += 1
        averages.append(total / size)
        second += 1
    return averages


"""
    Answer Code
"""
# def find_averages_of_subarrays(K, arr):
#   result = []
#   windowSum, windowStart = 0.0, 0
#   for windowEnd in range(len(arr)):
#     windowSum += arr[windowEnd]  # add the next element
#     # slide the window, we don't need to slide if we've not hit the required window size of 'k'
#     if windowEnd >= K - 1:
#       result.append(windowSum / K)  # calculate the average
#       windowSum -= arr[windowStart]  # subtract the element going out
#       windowStart += 1  # slide the window ahead
#
#   return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
