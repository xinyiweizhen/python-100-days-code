"""
    二分查找（常规写法）：
    接受一个有序数组和一个元素
"""
def binary_search(list, target):
    start = 0
    # 为什么减1？ 因为数组下标都是从0开始的
    end = len(list) - 1
    # 重点: 因为闭区间，所以到了begin等于end时，其实区间内还有一个值要判断，因此只有begin>end的时候才能停止
    while start <= end:
        mid = (start + end) // 2  # //为截断除法， 返回整数， /为真除法，返回浮点数
        if list[mid] == target:
            return list[mid]
        elif list[mid] > target:
            # 搜索范围变为[left, mid - 1]
            end = mid - 1
        else:
            # 搜索范围变成[mid + 1, end]
            start = mid + 1
    return None

if __name__ == '__main__':
    array = [1, 2, 3, 5, 6, 8, 10, 77]
    print(binary_search(array, 6))