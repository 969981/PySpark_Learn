import numpy as np
from PIL import Image

# 匹配样例一  220
a = np.array(Image.open('../IMG/full_search/样例一.bmp'))
for i in range(1, 1001):
    path = './data/' + str(i) + '.npy'
    b = np.load(path)
    if np.array_equiv(a, b):
        print(path)
        break

# 匹配样例二 853
a = np.array(Image.open('../IMG/full_search/样例二.bmp'))
for i in range(1, 1001):
    path = './data/' + str(i) + '.npy'
    b = np.load(path)
    if np.array_equiv(a, b):
        print(path)
        break
