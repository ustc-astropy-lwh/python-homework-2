# change the store struct of val

import os
import shutil

# ctreat folder
def mkdir(path):
    folder=os.path.exists(path)
    if not folder:
        os.makedirs(path)
    else:
        print(path)

if __name__=='__main__':
    # tinyimagenet wnid.txt named folder
    file='E:\中科大学习\大三课程\python与深度学习基础\大作业2\imagenet/tiny-imagenet-200/val'
    with open('E:\中科大学习\大三课程\python与深度学习基础\大作业2\imagenet/tiny-imagenet-200\wnids.txt', 'r') as w:
        for line in w.readlines():
            line = line.strip('\n')
            folder=file+'/'+line
            mkdir(folder)
    
    #val_annotations.txt，extract image form val
    with open("E:\中科大学习\大三课程\python与深度学习基础\大作业2\imagenet/tiny-imagenet-200/val/val_annotations.txt", 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            dirlist = []
            imagelist=[]
            dir = line.split()
            dir_name = dir[1:2]
            image_name=dir[0:1]
            dirlist.append(dir_name)
            imagelist.append(image_name)
            a=dirlist[0][0]
            b=imagelist[0][0]
            image_path='E:\中科大学习\大三课程\python与深度学习基础\大作业2\imagenet/tiny-imagenet-200/val/images'+'/'+b
            dir_path='E:\中科大学习\大三课程\python与深度学习基础\大作业2\imagenet/tiny-imagenet-200/val'+'/'+a
            shutil.copy(image_path, dir_path)
