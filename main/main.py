# Main file for end-to-end OCR

# Author: LI Yang
# Institution: WeShare

from PaddleOCR import PaddleOCR, draw_ocr
from PIL import Image
import pixellib
from pixellib.instance import instance_segmentation
import os
import cv2

# Initialization
ocr = PaddleOCR(use_angle_cls = True, lang = "ch")
segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")

img_path = "../Img/"
result_list = []
Lot_list = []
CAS_list = []
Serial_list = []


def draw_ocr_result(img, res, index):
    image = Image.open(img).convert('RGB')
    output_name = "./ocr_res/res" + str(index) + ".jpg"
    boxes = [line[0] for line in res]
    texts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    im_show = draw_ocr(image, boxes, texts, scores, font_path='PingFang.ttc')
    im_show = Image.fromarray(im_show)
    im_show.save(output_name)


def instance_segmentation(img, index):
    output_name = "./ins_seg_res/res" + str(index) + ".jpg"
    seg_mask, output = segment_image.segmentImage(img, output_image_name=output_name)
    cv2.imwrite("1.jpg", output)
    #print(output.shape)
    #print(seg_mask['masks'])


def sort_information(res, index):
    texts = [line[1][0] for line in res]
    print(texts)
    for elements in texts:
        if elements.find("lot") != -1 or elements.find("Lot"):
            print(elements)
            Lot_list.append(elements)
    print(Lot_list)


for i in range(1, 24):
    img_name = img_path + 'test' + str(i) + '.jpg'
    instance_segmentation(img_name, i)
    result = ocr.ocr(img_name, cls=True)
    result_list.append(result)
    draw_ocr_result(img_name, result_list[i-1], i)
    sort_information(result_list[i-1], i)






