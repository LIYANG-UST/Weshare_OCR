from Stitcher import Stitcher
import cv2

# 读取拼接图片
#imageA = cv2.imread("TestImg/2.jpg")
#imageB = cv2.imread("TestImg/3.jpg")
imageA = cv2.imread("su01.jpg")
imageB = cv2.imread("su02.jpg")

# 把图片拼接成全景图
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()