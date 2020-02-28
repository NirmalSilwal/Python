import os
import sys
from PIL import Image

source_path = sys.argv[1]
destination_path = sys.argv[2]

# print(source_path)
# print(destination_path)

if not os.path.exists(destination_path):
    os.mkdir(destination_path)

for images in os.listdir(source_path):
    filename = images.split('.')[0] + '.png'
    img = Image.open(source_path+'\\'+images)
    img.save(destination_path + '\\' + filename)

print('files saved succsssfully!')