from pyspark import SparkConf, SparkContext
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class Getoutofloop(Exception):
    pass


conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf = conf)
sc = SparkContext.getOrCreate(conf)
a = np.array(Image.open('/home/hadoop/IMG/part_search/特征一.bmp'))
# 数组的长和宽
x, y = a.shape
rdd1 = sc.parallelize(a.ravel())
rdd2 = rdd1.map(lambda word: (word, 1)). \
    reduceByKey(lambda a, b: a + b)
rdd3 = rdd2.sortByKey()
t1 = rdd3.collect()
try:
    for i in range(1, 1001):
        path = '../data/' + str(i) + '.npy'
        b = np.load(path)
        x1, y1 = b.shape
        for j in range(0, x1 - x + 1):
            for k in range(0, y1 - y + 1):
                c = b[j:j + x, k:k + y]
                d = c.ravel()
                rdd4 = sc.parallelize(d)
                rdd5 = rdd4.map(lambda word: (word, 1)). \
                    reduceByKey(lambda a, b: a + b)
                rdd6 = rdd5.sortByKey()
                t2 = rdd6.collect()
                if (t1 == t2):
                    print(path)
                    # 局部图左上点在原图的位置
                    print(j, k)
                    # 局部图右下点在原图的位置
                    print(j + x - 1, k + y - 1)
                    raise Getoutofloop()
except Getoutofloop:
    pass
