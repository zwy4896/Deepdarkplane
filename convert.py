import os
import cv2
from skimage import io

path = 'assets\\images'

for root, dirs, files in os.walk(path):
    for file in files:
        if '.ico' not in file:
            image = io.imread(os.path.join(root, file))
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
            cv2.imwrite(os.path.join(root, file), image)