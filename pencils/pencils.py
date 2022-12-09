import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import regionprops, label
from skimage.morphology import binary_closing

pencils = 0
for i in range(1, 13):
    count = 0
    image = cv2.imread(f'images\\img ({i}).jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray[gray > 125] = 0
    gray[gray != 0] = 255
    gray = binary_closing(binary_closing(gray))
    labeled = label(gray)
    regions = regionprops(labeled)

    for region in regions:
        if region.area > 250000 and region.equivalent_diameter > 550 and region.equivalent_diameter < 700:
            count += 1
            pencils += 1
    print(f"Изображение {i}: {count}")

print(f"Cуммарное количество карандашей на всех изображениях: {pencils}")