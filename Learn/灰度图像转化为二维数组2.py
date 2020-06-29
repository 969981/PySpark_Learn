import cv2
import numpy as np

# 这个就算了,转的是三维的
src = cv2.imread('../IMG/data/1.bmp')
print(src)
print(src.shape)
print(src.ravel())
