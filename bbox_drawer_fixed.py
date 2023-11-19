import cv2
import numpy as np
import pandas as pd
import ast
import json
''' Required files
1) Make directory tablets/ with all of the WikiData tablet imgs (https://drive.google.com/open?id=1rGD_AtUNgRyovNAgSuS-jryDLnkWUcAB&usp=drive_copy)
2) Make directory char/ with cutouts from the HaiCuBeDa dataset (https://drive.google.com/drive/u/3/folders/1E3g5zVDFX5YzjLZ4fZyawp6khCxaLFgD)
3) Download the JSON file linked in the discord group (see Timo's message).
'''
bounding_boxes = []
# Load the JSON file from a text file

def get_square_from_quad(arr):
  # This is a lazy algorithm. TODO: Make a better one later
  new_arr = []
  for subarray in arr:
    print("subarr[0]",list(subarray[0]))
    new_arr.append(list(subarray[0]))
  arr = new_arr
  xs = [i[0] for i in arr]
  ys = [i[1] for i in arr]

  small_x = min(xs)
  small_y = min(ys)

  big_x = max(xs)
  big_y = max(ys)

  return ((small_x,big_y),(big_x,small_y))

# Convert Pascal_Voc bb to Yolo
def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
    return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

with open('annojson.txt', 'r') as file:
  # Assuming the JSON data is in a single line, if not, you may need to adjust the reading logic
  data_str = file.read()
  data = json.loads(data_str)

for sign in data.keys():
  print(sign)
  svg_string = data[sign]['target']['selector']['value']
  svg_points = svg_string.split('points="')[1].split('"')[0]
  print(svg_points)
  points = np.array([list(map(float, pair.split(','))) for pair in svg_points.split()], dtype=np.int32).reshape((-1, 1, 2))
  print(points)
  bounding_boxes.append(points)

# Load your image
print("Loading image...")
image = cv2.imread("tablets/ HS 1486.png")
height, width, channels = image.shape
print(width,height)

# Loop through the bounding boxes and overlay them on the image
print("Drawing bounding boxes...")
for points in bounding_boxes:
    print("POINTS:",points)
    new_rect = get_square_from_quad(points)
    print("NEW POINTS:",new_rect)

    #cv2.polylines(image, [points], isClosed=True, color=(255, 0, 0), thickness=20)
    cv2.rectangle(image, new_rect[0], new_rect[1], color=(255,0,0), thickness=20)
    x1 = new_rect[0][0]
    x2 = new_rect[1][0]
    y1 = new_rect[1][1]
    y2 = new_rect[0][1]
    print("x1y1, x2y2:",x1,y1,x2,y2)
    print("YOLO_format: ",pascal_voc_to_yolo(x1,y1,x2,y2,width,height))

    # Press any key to move onto the next frame
    cv2.imshow("tablet",image)
    cv2.waitKey(0)
    print("Press any key to move to next frame...")

# Display the image with bounding boxes
print("Displaying image...")
cv2.imwrite('fixed_bounding_boxes.png', image)
