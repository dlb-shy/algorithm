# -*- coding: utf-8 -*-
__author__ = 'dlb'

def bubble_sort(data, reverse=False):
    """
    冒泡排序 时间复杂度 时间复杂度为 O(n^2)
    相邻元素两两比较，把较大的元素放到后面，在一轮比较完成之后，最大的元素就位于最后一个位置了，就好像是气泡，慢慢的浮出了水面一样。
    :param data: list type data
    :param reverse: 默认正序，值为True是倒序
    :return: list type data
    """
    if not reverse:
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    else:
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


def selection_sort(data, reverse=False):
    """
    选择排序，
    是逐个确定元素位置的思想。同样是 n 遍循环，第一轮时，每一个元素都与第一个元素比较，
    如果比第一个元素大，则与之交换，这样一轮过后，第一个元素就是最小的了，第二轮开始每个元素与第二个位置的元素比较，
    如果大，则与第二位置的元素交换，以此类推，达到排序的目的
    时间复杂度也是 O(n^2)
    :param data: list type data
    :param reverse:
    :return: list type data
    """
    if not reverse:
        for i in range(len(data)-1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data
    else:
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] > data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data


def insert_sort(data, reverse=False):
    '''
    插入排序的思想是把一个数据插入到一个有序序列中，从而得到一个新的序列加一的有序序列，
    时间复杂度为O(n^2)
    :param data:
    :param reverse:
    :return:
    '''
    if not reverse:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0:
                if data[j] > key:
                    data[j+1] = data[j]
                    data[j] = key
                j -= 1
        return data
    else:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0:
                if data[j] < key:
                    data[j+1] = data[j]
                    data[j] = key
                j -= 1
        return data


def quick_sort(data, reverse=False):
    '''
    首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，
    所有比它大的数都放到它后面，这个过程称为一趟快速排序，之后再递归排序两边的数据。
    O(nlogn)
    :param data:
    :return: 
    '''
    if len(data) <= 1:
        return data
    if not reverse:
        first = data[0]
        left = quick_sort([l for l in data[1:] if l < first])
        right = quick_sort([r for r in data[1:] if r >= first])
        return left + [first] + right
    else:
        first = data[0]
        left = quick_sort([l for l in data[1:] if l >= first], reverse=True)
        right = quick_sort([r for r in data[1:] if r < first], reverse=True)
        return left + [first] + right


if __name__ == '__main__':
    data = [6, 1, 34, 54, 12, 65, 47, 89]
    res = quick_sort(data, reverse=True)
    print(res)
