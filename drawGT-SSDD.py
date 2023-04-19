

import argparse
import os
import sys
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync




import os

import numpy as np
import cv2
import torch

label_path = r'C:\Users\Administrator\Downloads\data\labels\cars5.txt'
image_path = r'C:\Users\Administrator\Downloads\data\cars5.jpg'

#坐标转换，原始存储的是YOLOv5格式
# Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
def xywh2xyxy(x, w1, h1, img):
    label, x, y, w, h = x
    if label ==None:
        return None
    print("原图宽高:\nw1={}\nh1={}".format(w1, h1))
    #边界框反归一化
    x_t = x*w1
    y_t = y*h1
    w_t = w*w1
    h_t = h*h1
    print("反归一化后输出：\n第一个:{}\t第二个:{}\t第三个:{}\t第四个:{}\t\n\n".format(x_t,y_t,w_t,h_t))

    #计算坐标
    top_left_x = x_t - w_t / 2
    top_left_y = y_t - h_t / 2
    bottom_right_x = x_t + w_t / 2
    bottom_right_y = y_t + h_t / 2
    print('标签:{}'.format(names[int(label)]))
    print("左上x坐标:{}".format(top_left_x))
    print("左上y坐标:{}".format(top_left_y))
    print("右下x坐标:{}".format(bottom_right_x))
    print("右下y坐标:{}".format(bottom_right_y))
    return (top_left_x,top_left_y,bottom_right_x,bottom_right_y)
    # 绘图  rectangle()函数需要坐标为整数
    # cv2.rectangle(img, (int(top_left_x), int(top_left_y)), (int(bottom_right_x), int(bottom_right_y)), (0, 255, 0), 2)
    # cv2.imshow('show', img)
    # cv2.imwrite('11.png',img)
    # cv2.waitKey(0)  # 按键结束
    # cv2.destroyAllWindows()


if __name__=="__main__":
    src_dir= r"D:\wan\BaiduNetdiskDownload\SSDD\image_SSDD"
    save_dir=r"D:\wan\BaiduNetdiskDownload\SSDD\image_SSDD-GT"
    dir_list = os.listdir(src_dir)
    # names=['Scratch', 'CornerGash', 'Pit', 'Spot', 'Humb', 'Collapse'] # SBS
    # names=[ 'crazing','inclusion','patches','pitted_surface','rolled-in_scale','scratches']  #NEU-DET
    # names=['1_chongkong', '2_hanfeng', '3_yueyawan', '4_shuiban', '5_youban', '6_siban', '7_yiwu', '8_yahen', '9_zhehen', '10_yaozhe']    # GC_10
    names=['ship']
    for txt_path in dir_list:
        if not txt_path.endswith(".txt"):
            continue
        with open(src_dir+"/"+txt_path, 'r') as f:
            try:
                lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)  # labels
                print(lb)
            except:
                continue

        # 读取图像文件
        img = cv2.imread(src_dir+"/"+str(txt_path.replace('.txt','.jpg')))
        h, w = img.shape[:2]
        annotator = Annotator(img, line_width=3, example=str(names))
        for x in lb:
            # 反归一化并得到左上和右下坐标，画出矩形框
            xyxy=xywh2xyxy(x, w, h, img)
            if xyxy == None:
                continue
            # Write results
            print(lb)
            c = int(x[0])  # integer class
            label =  f'{names[c]}'
            annotator.box_label(xyxy, label, color=colors(c, True))
        im0 = annotator.result()
        save_path=save_dir+"/"+txt_path.replace('.txt','.jpg')
        print(save_path)
        cv2.imwrite(save_path, im0)

# 原文链接：https://blog.csdn.net/weixin_46034990/article/details/124634755