from pyspark import SparkConf, SparkContext
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)
# 读取存储的一维矩阵的数据
textFile = sc.textFile("TXT1/data/1.txt")
# 将rdd对象转换为list
t1 = textFile.collect()
# 将string list 转化为int list
t1 = list(map(int, t1))
# 将list转化为一维数组
a = np.array(t1, dtype=np.int)
# 将一维数组转化为二维数组
b = np.reshape(a, (512, 512))
# 将图片绘制出来
plt.imshow(b)
plt.show()
