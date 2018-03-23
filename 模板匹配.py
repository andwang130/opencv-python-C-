import cv2
import numpy as np
def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)  #打开对比图片
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)#颜色空间转换
    cv2.imshow('dede',image)
    template = cv2.imread(Target,0)#  打开模板图片
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) #两张图片进行对比，cv2.TM_CCOEFF_NORMED对比类型
    tutp=cv2.minMaxLoc(res)
    print(tutp)
    # threshold = value  #传入的对比阀值
    # for i in res:
    #     print(i)
    # loc = np.where( res >= threshold)
    # print(loc)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
    #     print(pt)
    # cv2.imshow('Detected',img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
image=("temlpath.jpg")
Target=('len.jpg')
value=0.99
mathc_img(image,Target,value)