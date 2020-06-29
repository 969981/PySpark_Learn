import numpy as np
from pyspark import SparkConf, SparkContext
import matplotlib.pyplot as plt
from PIL import Image

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)
# 读取一维数组
t1 = np.loadtxt('../data1/1.txt', dtype=np.int)
rdd1 = sc.parallelize(t1)
# 统计词频
rdd2 = rdd1.map(lambda word: (word, 1)). \
    reduceByKey(lambda a, b: a + b)
# 按照键排序
rdd3 = rdd2.sortByKey()
