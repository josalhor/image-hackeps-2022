import cv2
import numpy as np
from matplotlib import pyplot as plt
import json
  
# reading image
# img = cv2.imread('daily-hack3/test-images/test3.png')

def get_colors_image(path, top=13):
    img = cv2.imread(path)
    rng = 255*255*255
    domain = [None] * rng

    for channel in img:
        for value in channel:
            (r,g,b) = value
            index = r + g*254 + b*254*254 
            d = domain[index]
            if d is None:
                domain[index] = (tuple(map(int, value)), 1)
            else:
                domain[index] = d[0], d[1] + 1

    domain_filt = []

    for value in domain:
        if value is not None:
            domain_filt.append(value)

    domain_filt.sort(key=lambda x: x[1], reverse=True)
    domain_filt = domain_filt[:top]

    values = {}
    for value in domain_filt:
        if value is not None:
            value, count = value
            values[value] = count
    
    for rm_col in [(0,0,0),(255,255,255)]:
        if rm_col in values:
            del values[rm_col]
    return list(set(values))

# cercles = get_colors_image('daily-hack3/reference-images/cercles.png')
# quadrats = get_colors_image('daily-hack3/reference-images/quadrats.png')
# rectangles = get_colors_image('daily-hack3/reference-images/rectangles.png')
# triangles = get_colors_image('daily-hack3/reference-images/triangles.png')

# all_colors = [cercles, quadrats, rectangles, triangles]
# for i, color1 in enumerate(all_colors):
#     for j, color2 in enumerate(all_colors[i + 1:], i + 1):
#         if color1 is color2: continue
#         inte = color1.intersection(color2) 
#         print(inte, i, j)


# with open('colors.types', 'w+') as f:
#     json.dump({
#         'cercles': cercles,
#         'quadrats': quadrats,
#         'rectangles': rectangles,
#         'triangles': triangles,
#     }, f)

logo = get_colors_image('daily-hack3/reference-images/logo.png', top=2)

with open('logo.types', 'w+') as f:
    json.dump({
        'logo': logo,
    }, f)

exit(1)