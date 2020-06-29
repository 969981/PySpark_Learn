from PIL import Image
from scipy.spatial.distance import cosine
import numpy as np

# 余弦相似性
# https://zh.wikipedia.org/wiki/%E4%BD%99%E5%BC%A6%E7%9B%B8%E4%BC%BC%E6%80%A7

# 皮尔逊相关系数
# https://zh.wikipedia.org/wiki/%E7%9A%AE%E5%B0%94%E9%80%8A%E7%A7%AF%E7%9F%A9%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0

a = np.array(Image.open('../IMG/data/1.bmp')).ravel()
b = np.load('./data/1.npy').ravel()
c = cosine(a, b)
print(c)
# 欧氏距离
dist = np.linalg.norm(a - b)
print(dist)

dist1 = np.sqrt(np.sum(np.square(a - b)))
print(dist1)
