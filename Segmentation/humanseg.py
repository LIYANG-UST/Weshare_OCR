import os 
import sys 
import cv2
import paddlehub as hub 

# 1.加载模型 
humanseg = hub.Module(name="deeplabv3p_xception65_humanseg") 

# 2.指定待抠图图片目录 
path = './img/' 
files = [path + i for i in os.listdir(path)] 
#dirs = os.listdir(path) 
#for diretion in dirs: 
    #files.append(path + diretion) 
#files = './2.jpg'

# 3.抠图 
#results = humanseg.segmentation(data={"image": files}, output_dir='humanseg_output') 
#result = humanseg.segmentation(images=[cv2.imread('2.jpg')],output_dir='humanseg_output.jpg')
result = humanseg.segmentation(data={"image": files})
'''
for result in results: 
    print(result['origin']) 
    print(result['processed']) 
'''