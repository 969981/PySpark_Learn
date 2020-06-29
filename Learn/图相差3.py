import numpy as np
from PIL import Image

# 匹配样例一  600
a = np.array(Image.open('../IMG/change_search/样例二.bmp'))
# 将二维矩阵转为一维矩阵
a = a.ravel()
max1 = 0
ans = ''
for i in range(1, 1001):
    path = './data/' + str(i) + '.npy'
    b = np.load(path)
    b = b.ravel()
    if sum(a == b) > max1:
        max1 = sum(a == b)
        ans = path
print(ans)
