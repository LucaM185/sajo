# take all the images in this folder and convert from png to jpg and downscale to ~500KB

import pandas as pd
import os
from PIL import Image

# get all the png files in the current directory
png_files = [f for f in os.listdir() if f.endswith('.png')]

# convert each png file to jpg
for file in png_files:
    # read the png file
    img = Image.open(file)
    
    # calculate dimensions to get roughly 500KB jpg
    # assuming typical compression ratios, aim for ~2.5M pixels
    target_pixels = 2500000
    ratio = (target_pixels / (img.size[0] * img.size[1])) ** 0.5
    new_width = int(img.size[0] * ratio)
    new_height = int(img.size[1] * ratio)
    
    # resize and convert to jpg with moderate compression
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    img.convert('RGB').save(file.replace('.png', '.jpg'), quality=85, optimize=True)
    
    # delete the png file
    os.remove(file)

print(f"Converted and downscaled {len(png_files)} png files to jpg")