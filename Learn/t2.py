from PIL import Image
from scipy.spatial.distance import cosine
import numpy as np

a = np.array(Image.open('../IMG/data/1.bmp')).ravel()
b = np.load('./data/1.npy').ravel()
c = cosine(a, b)
print(c)
