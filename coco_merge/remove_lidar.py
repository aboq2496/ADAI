import os
import shutil

src_path = "../data/3DBB/data_2" ## sunny dir 
lidar_path = src_path + '/lidar'
label_path = src_path + '/label'

def remove_lidar(lidar_path, label_path):
    lidar_files = os.listdir(lidar_path)
    label_files = os.listdir(label_path)
    for i in lidar_files:
        if i[:6]+'.json' not in label_files:
            print(i[:6]+'.json')
            os.remove(lidar_path+'/'+i[:6]+'.pcd')


def remove_label(lidar_path, label_path):
    lidar_files = os.listdir(lidar_path)
    label_files = os.listdir(label_path)
    for i in label_files:
        if i[:6]+'.pcd' not in lidar_files:
            print(i[:6]+'.pcd')
            os.remove(label_path+'/'+i[:6]+'.json')
# def remove_bin(lidar_path, label_path):
#     lidar_files = os.listdir(lidar_path)
#     label_files = os.listdir(label_path)
#     for i in lidar_files:
#         if i[:6]+'.json' not in label_files:
#             print(i[:6]+'.json')
#             if i[:6]+'.json' in label_files:
#                 os.remove(label_path+'/'+i[:6]+'.json')
      

remove_label(lidar_path, label_path)
remove_lidar(lidar_path, label_path)