from scipy import misc
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = np.array(Image.open('../IMG/data/1.bmp'))
plt.imshow(im)
plt.savefig('./2.png')
