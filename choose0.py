import cv
import math
def radio(img,rect):
    white_l = 0.0
    black_l = 0.0
    white_r = 0.0
    black_r = 0.0
    white_u = 0.0
    black_u = 0.0
    white_d = 0.0
    black_d = 0.0
    l_r = 0
    u_d = 0
    l_u = 0
    r_d = 0
    radio_w_b = 0.0
    white_black = 0
    rect_center_x = rect[0] + rect[2] / 2
    rect_center_y = rect[1] + rect[3] / 2
    center_value = img[rect_center_y,rect_center_x]
    left_up = img[rect[1],rect[0]]
    left_down = img[rect[1]+rect[3],rect[0]]
    right_up = img[rect[1],rect[0]+rect[2]]
    right_down = img[rect[1]+rect[3],rect[0]+rect[2]]
    fourpoints = left_down + left_up + right_down +right_up
    i = rect[0]
    j = rect[1]


    while(1):
        while(1):
            if img[j,i] == 255.0:
                white_l = white_l + 1.0
            else :
                black_l = black_l + 1.0
            j = j + 1
            if (j == rect[1]+rect[3]):
                j = 0
                break
        i = i + 1
        if (i == rect[0]+rect[2]):
            i = 0
            break
    # i = rect[0]+rect[2]/2
    # j = rect[1]
    # # for i in range((rect[0]+rect[2]/2),(rect[0]+rect[2]),1):
    # #     for j in range(rect[1],rect[1]+rect[3],1):
    # while(1):
    #     while(1):
    #         if img[j,i] == 255.0:
    #             white_r = white_r + 1.0
    #         else :
    #             black_r = black_r + 1.0
    #         j = j + 1
    #         if j == rect[1]+rect[3]:
    #             j = 0
    #             break
    #     i = i + 1
    #     if i == rect[0]+rect[2]:
    #         i = 0
    #         break
    #
    # i = rect[0]
    # j = rect[1]
    # # for i in range(rect[0],(rect[0]+rect[2]),1):
    # #     for j in range(rect[1],(rect[1]+rect[3]/2),1):
    # while(1):
    #     while(1):
    #         if img[j,i] == 255.0:
    #             white_u = white_u + 1.0
    #         else :
    #             black_u = black_u + 1.0
    #         j = j + 1
    #         if j == rect[1]+rect[3]/2:
    #             j = 0
    #             break
    #     i = i + 1
    #     if i == rect[0]+rect[2]:
    #         i = 0
    #         break
    # i = rect[0]
    # j = rect[1]+rect[3]/2
    # # for i in range(rect[0],(rect[0]+rect[2]),1):
    # #     for j in range((rect[1]+rect[3]/2),(rect[1]+rect[3]),1):
    # while(1):
    #     while(1):
    #         if img[j,i] == 255.0:
    #             white_d = white_d + 1.0
    #         else :
    #             black_d = black_d + 1.0
    #         j = j + 1
    #         if j == rect[1]+rect[3]:
    #             j = 0
    #             break
    #     i = i + 1
    #     if i == rect[0]+rect[2]:
    #         i = 0
    #         break
    # white = (white_r + white_l + white_d + white_u) / 2
    # black = (black_d + black_u + black_r + black_l) / 2
    white = white_l
    black = black_l
    if black != 0:
     radio_w_b =  black/white
    # # if(white_r!=0)and(white_d!=0)and(white_u!=0)and(black!=0):
    # #     radio_l_r = white_l / white_r
    # #     radio_u_d = white_u / white_d
    # #     radio_l_u = white_l / white_u
    # #     radio_r_d = white_r / white_d
    # #
    # #
    # #
    # #     if radio_l_r > 0.7:
    # #         if radio_l_r < 1.3:
    # #             l_r = 1
    # #     if radio_u_d > 0.7:
    # #         if radio_u_d < 1.3:
    # #             u_d = 1
    # #     if radio_l_u > 0.7:
    # #         if radio_l_u < 1.3:
    # #             l_u = 1
    # #     if radio_r_d > 0.7:
    # #         if radio_r_d < 1.3:
    # #             r_d = 1
    # if radio_w_b > 2.8:
    #         white_black = 1




    ret = 0
    # if white_black == 1:
    if center_value == 255.0:
                if fourpoints < 300.0:
                    ret = 1
    return ret
def choose2(img,rect):
    white_l = 0.0
    black_l = 0.0
    white_r = 0.0
    black_r = 0.0
    white_u = 0.0
    black_u = 0.0
    white_d = 0.0
    black_d = 0.0
    l_r = 0
    u_d = 0
    l_u = 0
    r_d = 0
    white_black = 0
    radio_w_b = 0.0
    rect_center_x = rect[0] + rect[2] / 2
    rect_center_y = rect[1] + rect[3] / 2
    center_value = img[rect_center_y,rect_center_x]
    left_up = img[rect[1],rect[0]]
    left_down = img[rect[1]+rect[3],rect[0]]
    right_up = img[rect[1],rect[0]+rect[2]]
    right_down = img[rect[1]+rect[3],rect[0]+rect[2]]
    fourpoints = left_down + left_up + right_down +right_up
    for i in range(rect[0],(rect[0]+rect[2]/2),1):
        for j in range(rect[1],rect[1]+rect[3],1):
            if img[j,i] == 255.0:
                white_l = white_l + 1.0
            else :
                black_l = black_l + 1.0

    for i in range((rect[0]+rect[2]/2),(rect[0]+rect[2]),1):
        for j in range(rect[1],rect[1]+rect[3],1):
            if img[j,i] == 255.0:
                white_r = white_r + 1.0
            else :
                black_r = black_r + 1.0

    for i in range(rect[0],(rect[0]+rect[2]),1):
        for j in range(rect[1],(rect[1]+rect[3]/2),1):
            if img[j,i] == 255.0:
                white_u = white_u + 1.0
            else :
                black_u = black_u + 1.0

    for i in range(rect[0],(rect[0]+rect[2]),1):
        for j in range((rect[1]+rect[3]/2),(rect[1]+rect[3]),1):
            if img[j,i] == 255.0:
                white_d = white_d + 1.0
            else :
                black_d = black_d + 1.0
    white = (white_r + white_l + white_d + white_u) / 2
    black = (black_d + black_u + black_r + black_l) / 2
    if(white_r!=0)and(white_d!=0)and(white_u!=0)and(black!=0):
        radio_l_r = white_l / white_r
        radio_u_d = white_u / white_d
        radio_l_u = white_l / white_u
        radio_r_d = white_r / white_d

        radio_w_b = white / black

        if radio_l_r > 0.7:
            if radio_l_r < 1.3:
                l_r = 1
        if radio_u_d > 0.7:
            if radio_u_d < 1.3:
                u_d = 1
        if radio_l_u > 0.7:
            if radio_l_u < 1.3:
                l_u = 1
        if radio_r_d > 0.7:
            if radio_r_d < 1.3:
                r_d = 1
        if radio_w_b > 2.3:
            white_black = 1



    result = l_r + u_d + l_u + r_d
    #print l_r ,u_d ,l_u ,r_d,white_black,fourpoints,radio_w_b
    ret = 0
    if white_black == 1:
         if result >= 2:
            if center_value == 255.0:
                if fourpoints < 300.0:
                    ret = 1
    return ret
def choose_land(img,rect,contours):
    white_l = 0.0
    black_l = 0.0
    white_r = 0.0
    black_r = 0.0
    white_u = 0.0
    black_u = 0.0
    white_d = 0.0
    black_d = 0.0
    white_black = 0
    area_land = 0.0
    area_land = cv.ContourArea(contours)
    rect_center_x = rect[0] + rect[2] / 2
    rect_center_y = rect[1] + rect[3] / 2
    center_value = img[rect_center_y, rect_center_x][0]
    left_up = img[rect[1], rect[0]][0]
    left_down = img[rect[1] + rect[3], rect[0]][0]
    right_up = img[rect[1], rect[0] + rect[2]][0]
    right_down = img[rect[1] + rect[3], rect[0] + rect[2]][0]
    fourpoints = left_down + left_up + right_down + right_up
    Area = float(rect[2])*rect[3]
    for i in range(rect[0], (rect[0] + rect[2] / 2), 1):
        for j in range(rect[1], rect[1] + rect[3], 1):
            if img[j, i][0] == 255.0:
                white_l = white_l + 1
            else:
                black_l = black_l + 1

    for i in range((rect[0] + rect[2] / 2), (rect[0] + rect[2]), 1):
        for j in range(rect[1], rect[1] + rect[3], 1):
            if img[j, i][0] == 255.0:
                white_r = white_r + 1
            else:
                black_r = black_r + 1

    for i in range(rect[0], (rect[0] + rect[2]), 1):
        for j in range(rect[1], (rect[1] + rect[3] / 2), 1):
            if img[j, i][0] == 255.0:
                white_u = white_u + 1
            else:
                black_u = black_u + 1

    for i in range(rect[0], (rect[0] + rect[2]), 1):
        for j in range((rect[1] + rect[3] / 2), (rect[1] + rect[3]), 1):
            if img[j, i][0] == 255.0:
                white_d = white_d + 1
            else:
                black_d = black_d + 1
    white = (white_r + white_l + white_d + white_u) / 2
    black = (black_d + black_u + black_r + black_l) / 2
    radio_b_w = black/white
    if radio_b_w > 0.5:
        if radio_b_w < 1.5:
          white_black = 1

    p = area_land/Area
    if p > 0.65:
        if p < 0.88:
            p = 1
    R1 = area_land/3.14159
    #R1 = math.sqrt(R1)
    R2 = (rect[2]*rect[3])/4
    R = R1 - R2
    R = abs(R)
    if R < 60:
        R = 1

    ret = 0
    if white_black == 1:
     if p == 1:
        if center_value == 255.0:
           if fourpoints >1000 :
             if R == 1:
                ret = 1

    return ret