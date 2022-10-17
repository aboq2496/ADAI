import os
import shutil
import time
import json
from functions_for_merge_coco import *

import glob
from tqdm import tqdm

src_path = "../data/2DBB1" 



new_path = src_path + '_merge' 
image_path = new_path + '/images'
json_path = new_path + '/annotations'

if not os.path.isdir(new_path):
	os.mkdir(new_path)
if not os.path.isdir(image_path):
	os.mkdir(image_path)
if not os.path.isdir(json_path):
	os.mkdir(json_path)

def rename_file(path):
    output = os.listdir(path)
    

    for i, j in enumerate(output):
        for a in ['annotations', 'images']:
            json = os.listdir(path+'/' +j+'/'+a)
           
            for name in json:
                src = os.path.join(path+'/' +j+'/'+a, name)
                dst = os.path.join(path+'/' +j+'/'+a, str(i) + name)
                os.rename(src, dst)
           
        
        
        
        
 

def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list



def copy_all_file(file_list, json_path, image_path):
    for src_path in file_list:
        if src_path.endswith('n'):
            file = src_path.split("/")[-1]
            shutil.copyfile(src_path, json_path+"/"+file)
        else:
            file = src_path.split("/")[-1]
            shutil.copyfile(src_path, image_path+"/"+file)
            print("파일 {} 작업 완료".format(file)) # 작업한 파일명 출력

        
def modify_json(path):

    files = os.listdir(path)
    for file in files:
        with open(path + '/'+file, "r") as json_files:
            json_data = json.load(json_files)
            print(json_data['images'][0]['file_name'])
            print(file)
            json_data['images'][0]['file_name'] = file[:-5] + '.jpg'

        with open(path + '/'+file, 'w') as outfile:
            json.dump(json_data, outfile)

        



def merge_multiple_cocos(path: str):
    '''
    :param path: Coco json's path
    :return: Merged coco json file
    '''
    project_files = (glob.glob(os.path.join(path, '*.json')))
    merged = {}
    merged['images'], merged['annotations'], merged['categories'] = [], [], []
    for index, path in enumerate(tqdm(project_files)):
        coco = config_reader(path)
        coco = get_the_unique_id_image(coco, 1000000000*(index+1))
        coco = get_unique_id_annotation(coco, 1000000000*(index+1))
        merged['images'] = coco['images'] + merged['images']
        merged['annotations'] = coco['annotations'] + merged['annotations']
        if index == (len(project_files)-1):
            merged['categories'] = coco['categories']
    return merged






start_time = time.time() # 작업 시작 시간 

rename_file(src_path)

file_list = read_all_file(src_path)
copy_all_file(file_list, json_path, image_path)

modify_json(json_path)

save_coco_file(merge_multiple_cocos(json_path),'merged_test')

print("=" * 40)
print("time : {}".format(time.time() - start_time)) # 총 소요시간 계산