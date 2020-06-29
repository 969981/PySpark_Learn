from pyspark import SparkConf, SparkContext
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf = conf)
sc = SparkContext.getOrCreate(conf)
a = np.array(Image.open('/home/hadoop/IMG/change_search/样例一.bmp'))
# 数组的长和宽
a = a[0:200, 0:200]
rdd1 = sc.parallelize(a.ravel())
rdd2 = rdd1.map(lambda word: (word, 1)). \
    reduceByKey(lambda a, b: a + b)
rdd3 = rdd2.sortByKey()
t1 = rdd3.collect()
for i in range(1, 1001):
    path = '../data/' + str(i) + '.npy'
    b = np.load(path)
    d = b[0:200, 0:200]
    rdd4 = sc.parallelize(d.ravel())
    rdd5 = rdd4.map(lambda word: (word, 1)). \
        reduceByKey(lambda a, b: a + b)
    rdd6 = rdd5.sortByKey()
    t2 = rdd6.collect()
    if (t1 == t2):
        print(path)
        break
