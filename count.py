import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage import color as colorp

image_copy = plt.imread("img/balls_and_rects.png")
image = image_copy.copy()
image = colorp.rgb2hsv(image)[:, :, 0]
rect_colors = {}
circle_colors = {}
cimage = np.unique(image) * 10
cimage = np.ceil(cimage)
cimage = np.unique(cimage)
image = np.ceil(image * 10)
i = 0
for color in cimage:
    img = image.copy()
    img[img != color] = 0
    lb = label(img)
    rect_colors[str(i)] = 0
    circle_colors[str(i)] = 0
    regions = regionprops(lb)
    for region in regions:
        if np.all(region.image):
            rect_colors[str(i)] += 1
        else:
            circle_colors[str(i)] += 1
    i += 1
print("All = ", np.sum(list(rect_colors.values())) + np.sum(list(circle_colors.values())))
print("Rectangle = ", rect_colors)
print("Circle = ", circle_colors)
