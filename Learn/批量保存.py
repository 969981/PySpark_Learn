import numpy as np
from PIL import Image

dir = '../IMG/data/'
for i in range(1, 1001):
    name = str(i) + '.bmp'
    path = dir + name
    savepath = './data/' + str(i) + '.npy'
    im = np.array(Image.open(path))
    np.save(savepath, im)
