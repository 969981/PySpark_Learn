import numpy as np
from PIL import Image
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf=conf)
sc = SparkContext.getOrCreate()
# 匹配样例一  220
a = np.array(Image.open('../IMG/full_search/样例一.bmp'))
for i in range(1, 1001):
    path = 'TXT1/data/' + str(i) + '.txt'
    t1 = sc.textFile(path)
    c = np.array(t1.collect(), dtype=np.int). \
        reshape(512, 512)
    if (a == b).all():
        print(path)
        break

# 匹配样例二 853
a = np.array(Image.open('../IMG/full_search/样例二.bmp'))
for i in range(1, 1001):
    path = './data/' + str(i) + '.npy'
    b = np.load(path)
    if (a == b).all():
        print(path)
        break
