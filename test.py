# from PIL import Image

# img = Image.open('tmp/ikea.jpg')
# img = img.convert("RGBA")
# datas = img.getdata()

# newData = []
# for item in datas:
#     if item[0] >= 253 and item[1] >= 253 and item[2] >= 251:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("tmp/ikea.png", "PNG")

import json
import os
import shutil
from pprint import pprint

with open('result.json') as f:
  datas = json.load(f)
  for data in datas:
    target_name = '{}_{}.jpg'.format(data['name'], data['number']).replace('/','／') .replace('\\','＼')
    target_path = os.path.join('targets', target_name)
    images = data['images']
    if len(images) == 1:
      source_path = os.path.join('images', images[0]['path'])
      print('copying {} to {}'.format(source_path, target_path))
      shutil.copy(source_path, target_path)
    else:
      print('missing {}'.format(target_name))

