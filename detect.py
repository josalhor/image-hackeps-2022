import cv2
import numpy as np
from matplotlib import pyplot as plt
import json
import sys
  
# reading image
img = cv2.imread(sys.argv[1])
logo = cv2.imread('daily-hack3/reference-images/logo.png')

with open('colors.types') as f:
    colors = json.load(f)

numbers_fig = {
    fig_type: 0 for fig_type in colors
}

colors_fig = {
    color_type: 0 for color_type in ['r', 'g', 'b']
}

for fig_type, colors in colors.items():
    for color in colors:
        b,g,r = color
        if r > g and r > b:
            ct = 'r'
        elif g > r  and g > b:
            ct = 'g'
        else:
            ct = 'b'
        color = np.array(color)

        img_in_range = cv2.inRange(img, color, color)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # setting threshold of gray image
        # _, threshold = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(
            img_in_range, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # list for storing names of shapes
        for i, contour in enumerate(contours):
            # here we are ignoring first counter because 
            # findcontour function detects whole image as shape
            # if i == 0:
            #     continue
        
            area = cv2.contourArea(contour)
            if area < 105:
                continue
            approx = cv2.approxPolyDP(
                contour, 0.01 * cv2.arcLength(contour, True), True)
            print(len(approx))
            (x, y, w, h) = cv2.boundingRect(approx)
            ratio = float(w) / float(h)
            if ratio <= 1.5 and 0.5 <= ratio:
                rect_type = "quadrats"
            else:
                rect_type = "rectangles"
            if len(approx) == 3:
                if fig_type == "triangles":
                    numbers_fig[fig_type] += 1
                    colors_fig[ct] += 1
            elif len(approx) == 4:
                if fig_type == "triangles":
                    numbers_fig[fig_type] += 1
                    colors_fig[ct] += 1
                if rect_type == fig_type:
                    numbers_fig[fig_type] += 1
                    colors_fig[ct] += 1
            elif len(approx)>= 4 and  len(approx) <= 8:
                if rect_type == fig_type:
                    numbers_fig[fig_type] += 1
                    colors_fig[ct] += 1
            elif len(approx) > 14:
                if fig_type == "cercles":
                    numbers_fig[fig_type] += 1
                    colors_fig[ct] += 1
        # print(numbers_fig)
        # cv2.imshow('shapes', img_in_range)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

# print(numbers_fig)

logo_color_min = [[20,70,180]]
logo_color_min = np.array(logo_color_min)
logo_color_max = [[80,180,255]]
logo_color_max = np.array(logo_color_max)


mask = cv2.inRange(img, logo_color_min, logo_color_max)
img_in_range = cv2.bitwise_and(img, img, mask=mask)
img_in_range = cv2.cvtColor(img_in_range, cv2.COLOR_BGR2GRAY)

mask = cv2.inRange(logo, logo_color_min, logo_color_max)
logo = cv2.bitwise_and(logo, logo, mask=mask)
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(img_in_range,logo,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
matching = 0
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    matching += 1

# displaying the image after drawing contours
# cv2.imshow('shapes', img_in_range)
  
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(f"""Classificació:

----------- COLOR ------------

Vermelles:      {colors_fig['r']}
Verdes:         {colors_fig['g']}
Blaves:         {colors_fig['b']}

----------- FORMES -----------

Triangles:      {numbers_fig["triangles"]}
Quadrats:       {numbers_fig["quadrats"]}
Rectangles:     {numbers_fig["rectangles"]}
Cercles:        {numbers_fig["cercles"]}

------ LOGOS LLEIDAHACK ------

Logos:          {matching}""")