from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 使用numpy转换
im = np.array(Image.open('../IMG/data/1.bmp'))
print(im)
# 将二维数组转化为一维数组
print(im.ravel())
print(im.shape)
print(im.ravel().shape)
# 将一维数组恢复为二维数组
print(np.reshape(im.ravel(), (512, 512)))

# 绘制直方图
plt.hist(im.ravel(), 256, [0, 256], density=True)
plt.show()
