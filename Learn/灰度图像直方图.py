from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

src = cv2.imread('../IMG/data/1.bmp')
# cv2.imshow("src", src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(src)
print(src.ravel())
# density是显示占比
plt.hist(src.ravel(), 256, density=True)
plt.show()
