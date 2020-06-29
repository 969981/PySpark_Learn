from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('../IMG/data/1.bmp')

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(img_gray, cmap=plt.cm.gray)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.axis([0, 255, 0, max(hist)])
plt.show()
print(hist)
