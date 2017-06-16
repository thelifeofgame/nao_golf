# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import sys
import time
import cv2
from cv2 import *
import numpy
import choose0
import Image
from naoqi import *



def getloacation(width,left):
    x0 = 3.0
    y0 = 0.5
    height_x = 10.0
    r = float(width)/height_x
    x = x0/r
    y = ((x/x0) * (float(left)/320.0))*y0
    return x,y
def landmarkdetect(IP, PORT,camID):


    camProxy = ALProxy("ALVideoDevice", IP, PORT)


    resolution = 2  # VGA``
    colorSpace = 11  # RGB
    videoClient = camProxy.subscribe("python_client",  resolution, colorSpace, 5)

    camProxy.setParam(18,camID)

    naoImage = camProxy.getImageRemote(videoClient)
    camProxy.unsubscribe(videoClient)
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]

    array = naoImage[6]


    im_cv = numpy.zeros((imageHeight, imageWidth, 3), numpy.uint8)

    im_cv.data = array

    #im_cv = cv2.imread("img3.jpg",1)
    b, g, r = cv2.split(im_cv)
    img1 = cv2.merge([r, g, b])
    img3 = cv2.cv.fromarray(img1)
    #img3=cv.LoadImage("img3.jpg",1)
    cv.SaveImage("save1.jpg",img3)
    imgHSV = cv.CreateImage(cv.GetSize(img3), 8, 3)
    cv.CvtColor(img3, imgHSV, cv.CV_RGB2HSV)

    cimg,cimg_c=hsvProceed(imgHSV)
    # cv.ShowImage("imgHSV", imgHSV)
    # cv.ShowImage("cimg", cimg)
    # cv.WaitKey(5)




    #
    # img3 = cv.LoadImage("save1.jpg",1)
    # imgHSV = cv.CreateImage(cv.GetSize(img3), 8, 3)
    #
    # cv.CvtColor(img3, imgHSV, cv.CV_RGB2HSV)
    # cimg, cimg_c=hsvProceed(imgHSV)
    # cv.ShowImage("s",cimg_c)





    storage = cv2.cv.CreateMemStorage(0)
    cnts = cv.FindContours(cimg,storage,cv2.cv.CV_RETR_LIST,cv2.cv.CV_CHAIN_APPROX_SIMPLE)
    currtnt=cnts
    x = 0.0
    Area = 0
    left_right = 0
    up_down = 0
    if camID == 0:
      areamax = 6000
      areamin = 350
      value = img3.height/7
    else :
      areamax = 5000
      areamin = 400
      value = 0

    while cnts:
        rect = cv2.cv.BoundingRect(cnts,0)
        area = rect[2]*rect[3]
        rect_center_x = rect[0] + rect[2] / 2
        rect_center_y = rect[1] + rect[3] / 2
        # if camID == 1:
        #  radio_c = choose0.radio(cimg_c,rect)
        # if camID == 0:
        #  radio_c = choose0.choose02(cimg_c,rect)

        radio = float(rect[2])/rect[3]
        if rect[1]>10:

          if area > areamin:
             if area < areamax:
                if radio > 0.1:
                     if radio < 1.0:
                      #if radio_c ==   1:

                       # cv2.cv.DrawContours(img3, cnts, (255, 255, 0), (255, 255, 0), 0, 1)
                       # cv2.cv.Rectangle(img3,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(0,0,255),1)

                       #choose0.radio(cimg_c,rect)
                       rect_center_x = rect[0] + rect[2]/2
                       rect_center_y = rect[1] + rect[3]/2

                       Area = rect[2]*rect[3]
                       left_right = rect_center_x - cimg.width / 2
                       up_down = rect_center_y - cimg.height / 2
                       x, y = getloacation(rect[2],left_right)


        cnts = cnts.h_next()

    # cv2.cv.ShowImage("fsfs", img3)
    # cv.WaitKey(1)
    return Area,left_right,x



def hsvProceed(img):
    single = cv.CreateImage(cv.GetSize(img),8,1)
    single_c = cv.CreateImage(cv.GetSize(img),8,1)
    width=0
    height=0
    while(1):
        while(1):
            if (img[height,width][0] > 70)and(img[height,width][0] < 95)and(img[height,width][1] > 53)and(img[height,width][1] < 230):#and(img[height,width][2]<200):
                single[height,width] = 255
                single_c[height, width] = 255
            else:
                single[height, width] = 0
                single_c[height, width] = 0
            height =height+1
            if(height==480):
                height=0
                break
        width=width+1
        if(width==640):
            break
    cv.Erode(single,single)
    cv.Dilate(single, single)
    cv.Erode(single_c, single_c)
    cv.Dilate(single_c, single_c)
    # cv.ShowImage("rgb",single)
    # cv.WaitKey()
    return single,single_c

#if __name__ == '__main__':

if __name__ == '__main__':
        IP="192.168.1.104"
        #IP="127.0.0.1"
        PORT=9559
        #lookat(IP, PORT)
        #a,s,d,f,g=findball(IP, PORT)
        # if(g==1):
        #     print "ss"
        # else:
        #     print "sss"

       # while 1:
         #findball(IP, PORT)
        landmarkdetect(IP,PORT,0)
    #cv2.imshow("fsfs", img)
        #cv2.waitKey(0)



