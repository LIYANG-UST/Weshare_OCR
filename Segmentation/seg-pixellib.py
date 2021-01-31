import pixellib

#semantic segmentation
from pixellib.semantic import semantic_segmentation

segment_img = semantic_segmentation()

segment_img.load_ade20k_model("./model/deeplabv3_xception65_ade20k.h5")

segment_img.segmentAsAde20k("./img/1.jpg", overlay=True, output_image_name="sem_seg_res.jpg")

#instance segmentation
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("./model/mask_rcnn_coco.h5")
segment_image.segmentImage("./img/1.jpg", show_bboxes = True, output_image_name = "ins_seg_res.jpg")