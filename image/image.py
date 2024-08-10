import sys
import os
from PIL import Image

old_file = sys.argv[1]
new_file = sys.argv[2]

if not os.path.exists(new_file):
    os.makedirs(new_file)

for filename in os.listdir(old_file):
    first_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join (old_file,filename))
    img.save(f'{new_file}/{first_name}.png',"PNG")