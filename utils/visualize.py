import numpy as np
import cv2

def show_landmark(img, label, circle_option = {'radius':5, 'color':(255, 255, 0), 'thickness':-1}):
  for x, y in label:
    img = cv2.circle(img, (int(x), int(y)), **circle_option)
  return img