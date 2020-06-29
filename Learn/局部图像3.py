import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 500.npy
a = np.array(Image.open('../IMG/part_search/特征三.bmp'))
# 数组的长和宽
x, y = a.shape
for i in range(1, 1001):
    path = './data/' + str(i) + '.npy'
    b = np.load(path)
    x1, y1 = b.shape
    for j in range(0, x1 - x + 1):
        for k in range(0, y1 - y + 1):
            c = b[j:j + x, k:k + y]
            if (a == c).all():
                print(path)
                exit(0)
