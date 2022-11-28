import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import label, regionprops

def group_colors(colors):
    groups = [[colors[0]],]
    delta = np.mean(np.diff(colors))
    for i in range(1, len(colors)):
        previous = colors[i-1]
        current = colors[i]
        if current - previous > delta:
            groups.append([])
        groups[-1].append(current)
    return groups

im = plt.imread("balls_and_rects.png")
hsv = color.rgb2hsv(im)
binary = hsv[:, :, 0].copy()
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled) 

colors = []
for reg in regions:
    cy, cx = reg.centroid
    colors.append(hsv[int(cy), int(cx), 0])
colors = sorted(colors)

balls = []
rects = []
for region in regions:
    if np.mean(region.image) == 1.0:
        rects.append(region)
    else:
        balls.append(region)

colors_balls=[]
colors_rects=[]
for region in regions:
    cy, cx = region.centroid
    colour = hsv[int(cy), int(cx)][0]
    if region in balls:
        colors_balls.append(colour)
    else:
        colors_rects.append(colour)

result_balss = dict()
result_rects = dict()
for grp in group_colors(sorted(colors_balls)):
    result_balss[np.mean(grp)] = len(grp)
for grp in group_colors(sorted(colors_rects)):
    result_rects[np.mean(grp)] = len(grp)

print(f"Oбщее количество фигур: {np.max(labeled)}")
print(f"Количество кругов: {len(balls)}. Количество прямоугольников: {len(rects)}")
print(f"Количество оттенков: {len(group_colors(colors))}")
print(f"Количество кругов по оттенкам: {result_balss}")
print(f"Количество прямоугольников по оттенкам: {result_rects}")