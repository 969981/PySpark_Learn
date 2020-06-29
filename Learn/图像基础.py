from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# from matplotlib.pylab import imshow

# 将灰度图片转化为二维数组
im = np.array(Image.open('../IMG/data/1.bmp'))
# 数组的维度和类型
# print(im.shape, im.dtype)
# print(im)
# print(im[511, 511])
img = Image.fromarray(im)
# img = img.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB
plt.imshow(img)
plt.show()
# 保存图片
# img.save("./1.png")