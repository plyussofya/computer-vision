import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load("D:\\Users\\plyus\\Desktop\\универ\\Введение в компьютерное зрение\\Counting objects\\ps.npy.txt")

mask1 = np.array([[1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1]])

mask2 = np.array([[1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1]])

mask3 = np.array([[1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1]])

mask4 = np.array([[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]])

mask5 = np.array([[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]])

print(f"The total number of objects in the binary image: {np.max(label(image))}")

figure1 = label(binary_erosion(image, mask1)).max()
print(f"Number of objects of the 1 type: {figure1}")
print(f"Number of objects of the 2 type: {label(binary_erosion(image, mask2)).max() - figure1}")
print(f"Number of objects of the 3 type: {label(binary_erosion(image, mask3)).max() - figure1}")
print(f"Number of objects of the 4 type: {label(binary_erosion(image, mask4)).max()}")
print(f"Number of objects of the 5 type: {label(binary_erosion(image, mask5)).max()}")