import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 3, 4])
    # 定义数组下标
    index = np.arange(0, 5)
    # 找到两个数组相等元素的下标位置
    print(index[a == b])
    # 找到两个数组不相等元素的下标位置
    print(index[a != b])
