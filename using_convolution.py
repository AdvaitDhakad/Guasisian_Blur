import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = Image.open('grayscale.jpg')
ar = np.array(img)
# ar = ar[:100, :100]
# print(ar)
filter = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

# print(filter[1])
print(ar.shape)
# print(ar[:3, :])

def convolve(img, filter):
    img_alt = np.zeros(shape=((img.shape[0]-2), (img.shape[1]-2), (img.shape[2])))
    # print(f'img:{img.shape}')
    # print(img_alt.shape)
    for i in range(img_alt.shape[0]):
        for j in range(img_alt.shape[1]):
            for k in range(img_alt.shape[2]):
                # print(((img[i:(i+3), j:(j+3), k]) * filter).sum()//9, end=" ")
                img_alt[i][j][k] = ((img[i:(i+3), j:(j+3), k]) * filter).sum()//9
            # print(" ")
    return img_alt

# for i in range(0, 10):
#     for j in range(0, 3):
#         print(ar[i][j], end=" ")
#     print(" ")
# print(ar.ndim)
# print(ar.shape)
# print
# print(ar.mean())
# print(ar.std())
# z_score = ar.mean()/ar.std()
# print(z_score)
# final_arr = np.multiply(ar, [1,1,1])
# for i in range(0, 10):
#     for j in range(0, 3):
#         print(final_arr[i][j], end=" ")
#     print(" ")
# new_img = Image.fromarray(ar, 'RGB')


new_img = convolve(ar, filter).astype(np.int64)
new_img = convolve(new_img, filter).astype(np.int64)
new_img = convolve(new_img, filter).astype(np.int64)
new_img = convolve(new_img, filter).astype(np.int64)
new_img = convolve(new_img, filter).astype(np.int64)
new_img = convolve(new_img, filter).astype(np.int64)

print(new_img.shape)
plt.imshow(new_img)
plt.show()
plt.savefig("after_convolution.jpg")