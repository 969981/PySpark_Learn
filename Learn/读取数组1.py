import numpy as np
from PIL import Image

a = np.load('./1.npy')
print(a)
b = np.reshape(a, (512, 512))
print(b)
img = Image.fromarray(b)
img.save('./test.png')
