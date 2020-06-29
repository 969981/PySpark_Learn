import numpy as np
from PIL import Image

# 匹配样例一  220
a = np.array(Image.open('../IMG/change_search/样例一.bmp')).ravel()
b = np.array(Image.open('../IMG/change_search/样例一.bmp')).ravel()
print(sum(a == b))
