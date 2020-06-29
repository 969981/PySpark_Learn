import numpy as np
from PIL import Image

im = np.array(Image.open('../IMG/data/1.bmp'))
a = im.ravel()
np.save('./1.npy', a)
