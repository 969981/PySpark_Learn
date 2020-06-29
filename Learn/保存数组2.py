import numpy as np
from PIL import Image

# https://www.runoob.com/numpy/numpy-io.html

im = np.array(Image.open('../IMG/data/1.bmp'))

# 保存为浮点数
np.savetxt('out.txt', im)
b = np.loadtxt('out.txt')
# 保存为整数
np.savetxt("out1.txt", im, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
b1 = np.loadtxt("out1.txt", delimiter=",")  # load 时也要指定为逗号分隔
print(b)
print(b1)
