import numpy as np
from PIL import Image

dir = '../IMG/data/'
for i in range(1, 1001):
    name = str(i) + '.bmp'
    path = dir + name
    savepath = './txt1/' + str(i) + '.txt'
    # 去掉ravel则是保存为二维的数组
    im = np.array(Image.open(path)).ravel()
    np.savetxt(savepath, im, fmt="%d")
