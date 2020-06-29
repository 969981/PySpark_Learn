import numpy as np
from PIL import Image

im = np.array(Image.open('../IMG/data/1.bmp'))

# 保存为整数
np.savetxt("out1.txt", im, fmt="%d")  # 改为保存为整数，以逗号分隔
b1 = np.loadtxt("out1.txt")  # load 时也要指定为逗号分隔
