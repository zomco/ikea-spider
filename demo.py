from PIL import Image
import json
import os
import shutil
from pprint import pprint

TARGET = 'targets';
SOURCE = 'sources';
RESULT = 'results.json';

def process_by_rgba(source_path, target_path):
  '''
  将图像背景转成透明，并修改图像文件名，保存到目标文件夹
  透明方式是根据像素RGB值判断是否为白色背景，如果符合则把像素A值设为0
  '''
  img = Image.open(source_path)
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = []
  for item in datas:
      if item[0] >= 253 and item[1] >= 253 and item[2] >= 251:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  img.putdata(newData)
  img.save(target_path, "PNG")

def process_by_edge(source_path, target_path):
  '''
  将图像背景转成透明，并修改图像文件名，保存到目标文件夹
  透明方式是根据像素HSV值判断是否为白色背景，如果符合则把像素A值设为0
  '''
  img = Image.open(source_path)
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = []
  for item in datas:
      if item[0] >= 253 and item[1] >= 253 and item[2] >= 251:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  img.putdata(newData)
  img.save(target_path, "PNG")
  
with open(RESULT) as f:
  # 检查原始目录
  # if not os.path.exists(SOURCE):
  #   sys.exit(0)
  # 检查目标目录
  if os.path.exists(TARGET):
    shutil.rmtree(TARGET)
  os.makedirs(TARGET)
  datas = json.load(f)
  for i, data in enumerate(datas):
    images = data['images']
    if len(images) == 1:
      image_path = images[0]['path']
      source_path = os.path.join(SOURCE, image_path)
      new_path = '{}_{}.png'.format(data['name'], data['number']).replace('/','／') .replace('\\','＼')
      target_path = os.path.join(TARGET, new_path)
      print('processing {} to {}'.format(source_path, target_path))
      shutil.copy(source_path, target_path)
      # process_by_rgba(source_path, target_path)
    else:
      print('missing {} item images'.format(i))
