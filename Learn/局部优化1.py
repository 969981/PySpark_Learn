import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# a是b的子集
def issub(a, b):



# 1000.npy
a = np.array(Image.open('../IMG/part_search/特征三.bmp'))
# 数组的长和宽
x, y = a.shape
# for i in range(1, 1001):
path = './data/' + str(1000) + '.npy'
b = np.load(path)
x1, y1 = b.shape
# for j in a:
cnt = 0
c = [1, 2, 3]
d = [1, 3, 4, 2]
print(issub(c, d))
