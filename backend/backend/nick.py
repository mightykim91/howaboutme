import os
import json

file_path = './nicks.json'
with open(file_path, 'r', encoding='UTF-8-sig') as json_file:
    nicks = json.load(json_file)
    print(nicks)
    print(len(nicks))
image_file_path = './dummy_images'
file_names = os.listdir(image_file_path)
file_names.sort()
file_names = file_names[1:]
print(len(file_names))
print(file_names)
for i,name in enumerate(file_names):
    src = os.path.join(image_file_path,name)
    dst = nicks[i] + '.jpeg'
    dst = os.path.join(image_file_path,dst)
    os.rename(src,dst)
