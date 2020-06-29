from pyspark import SparkConf, SparkContext
import numpy as np

conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf = conf)
sc = SparkContext.getOrCreate(conf)
textFile = sc.textFile('TXT1/data/1.txt')
data = textFile.collect()
# 将str转化为int
data = list(map(int, data))
# 通过并行列表创建rdd
rdd = sc.parallelize(data)
# 词频统计
rdd1 = rdd.map(lambda word: (word, 1)). \
    reduceByKey(lambda a, b: a + b)
# 按键排序
rdd2 = rdd1.sortByKey()
print(rdd2.collect())
