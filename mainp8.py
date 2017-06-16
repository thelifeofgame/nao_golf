import math
import almath
import time
import argparse
import redball000
import time
import landmark1
from naoqi import ALProxy

robotIP = "127.0.0.1"
IP = robotIP
PORT = 9559
# ********************motion init
motionProxy = ALProxy("ALMotion", robotIP, PORT)
# *******************posture init
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
# ***********************Memory init
memoryProxy = ALProxy("ALMemory", robotIP, PORT)
camProxy = ALProxy("ALVideoDevice", IP, PORT)
landMarkProxy = ALProxy("ALLandMarkDetection", IP, PORT)
memoryProxy = ALProxy("ALMemory", IP, PORT)


def StandToGetstick():
    postureProxy.goToPosture("Stand", 0.4)

    names = ['RShoulderRoll', 'RElbowRoll']
    angleLists = [-20.0 * almath.TO_RAD, 2.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    names = ['RShoulderRoll', 'RElbowYaw', 'RShoulderPitch']
    angleLists = [-45.0 * almath.TO_RAD, -4.0 * almath.TO_RAD, 4.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    motionProxy.openHand('RHand')
    time.sleep(20.0)
    motionProxy.closeHand('RHand')
    motionProxy.setStiffnesses('RHand', 1.0)

    names = ['RShoulderPitch', 'RElbowYaw', 'RShoulderRoll']
    angleLists = [84.0 * almath.TO_RAD, 68.0 * almath.TO_RAD, -25.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)


def HitBall(power):
    postureProxy.goToPosture("Stand", 0.4)
    names = ['RShoulderRoll', 'RElbowRoll']
    angleLists = [-25.0 * almath.TO_RAD, 2.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    names = ['RShoulderRoll', 'RElbowYaw', 'RShoulderPitch']
    angleLists = [-45.0 * almath.TO_RAD, -4.0 * almath.TO_RAD, 4.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    names = ['RWristYaw', 'RElbowYaw', 'RShoulderRoll', 'RElbowRoll', 'RShoulderPitch']
    angleLists = [-100.0 * almath.TO_RAD, 100.0 * almath.TO_RAD, 0.0 * almath.TO_RAD, 9.0 * almath.TO_RAD,
                  9.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0, 2.5, 3]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(2.0)

    names = 'RWristYaw'
    angleLists = 60.0 * almath.TO_RAD
    timeLists = power
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)
    time.sleep(1.0)

    names = ['RShoulderRoll', 'RElbowRoll', 'RShoulderPitch']
    angleLists = [0.0 * almath.TO_RAD, -20.0 * almath.TO_RAD, -20.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0, 2.5, 3]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(2.0)

    names = 'RWristYaw'
    angleLists = -100.0 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    names = ['RShoulderPitch', 'RElbowRoll', 'RShoulderRoll', 'RElbowYaw', 'RWristYaw']
    angleLists = [4 * almath.TO_RAD, -45.0 * almath.TO_RAD, -45.0 * almath.TO_RAD, -4.0 * almath.TO_RAD,
                  4.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0, 2.5, 3]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(2.0)

    names = ['RShoulderPitch', 'RElbowYaw', 'RShoulderRoll']
    angleLists = [84.0 * almath.TO_RAD, 68.0 * almath.TO_RAD, -25.0 * almath.TO_RAD]
    timeLists = [1.0, 1.5, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)


def Movex(d):
    x = d
    y = 0.0
    theta = 0.0
    motionProxy.moveTo(x, y, theta)
    # sleep_time=0.7
    # mdistance=0.15
    # if(d>0):
    #     while(1):
    #         if (d<=mdistance):
    #             x = d
    #             y = 0.0
    #             theta = 0.0
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             break
    #         else:
    #             x =mdistance
    #             y = 0.0
    #             theta = 0.0
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             d=d-mdistance
    # else:
    #     d=-d
    #     while(1):
    #         if (d<=mdistance):
    #             x = -d
    #             y = 0.0
    #             theta = 0.0
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             break
    #         else:
    #             x = -mdistance
    #             y = 0.0
    #             theta = 0.0
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             d=d-mdistance


def Movey(d):
    sleep_time = 0.5
    mdistance = 0.15
    if (d > 0):
        while (1):
            if (d <= mdistance):
                x = 0
                y = d
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(sleep_time)
                break
            else:
                x = 0.0
                y = mdistance
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(sleep_time)
                d = d - mdistance
    else:
        d = -d
        while (1):
            if (d <= mdistance):
                x = 0
                y = -d
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(sleep_time)
                break
            else:
                x = 0.0
                y = -mdistance
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(sleep_time)
                d = d - mdistance


def Movet(t):
    x = 0.0
    y = 0.0
    theta = t
    motionProxy.moveTo(x, y, theta)
    # sleep_time = 0.7
    # mdistance = math.pi/10
    # if(t>0):
    #     while(1):
    #         if (t<=( mdistance)):
    #             x = 0
    #             y = 0
    #             theta = t
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             break
    #         else:
    #             x = 0.0
    #             y = 0.0
    #             theta = mdistance
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             t=t-( mdistance)
    # else:
    #     t=-t
    #     while(1):
    #         if (t<=( mdistance)):
    #             x = 0
    #             y = 0
    #             theta = -t
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(mdistance)
    #             break
    #         else:
    #             x = 0.0
    #             y = 0.0
    #             theta = -math.pi/24
    #             motionProxy.moveTo(x, y, theta)
    #             #time.sleep(sleep_time)
    #             t=t-( mdistance)


def turnhead(Yaw, Picth):
    names = ["HeadPitch", "HeadYaw"]
    angleLists = [Picth * almath.TO_RAD, Yaw * almath.TO_RAD]
    timeLists = [1.0, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)


def DetecteLandmark():
    camProxy.setParam(18, 0)
    landmarkTheoreticalSize = 0.1
    currentCamera = "CameraTop"
    ip = robotIP
    period = 500
    landMarkProxy.subscribe("Test_LandMark", period, 0.0)
    for i in range(0, 10):
        time.sleep(0.5)
        markData = memoryProxy.getData("LandmarkDetected")
        if (markData is None or len(markData) == 0):
            continue
        else:
            if (len(markData) == 1):
                wzCamera = markData[1][0][0][1]
                wyCamera = markData[1][0][0][2]

                # Retrieve landmark angular size in radians.
                angularSize = markData[1][0][0][3]

                # Compute distance to landmark.
                distanceFromCameraToLandmark = landmarkTheoreticalSize / (2 * math.tan(angularSize / 2))

                motionProxy = ALProxy("ALMotion", ip, 9559)

                # Get current camera position in NAO space.
                transform = motionProxy.getTransform(currentCamera, 2, True)
                transformList = almath.vectorFloat(transform)
                robotToCamera = almath.Transform(transformList)

                # Compute the rotation to point towards the landmark.
                cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, wyCamera, wzCamera)

                # Compute the translation to reach the landmark.
                cameraToLandmarkTranslationTransform = almath.Transform(distanceFromCameraToLandmark, 0, 0)

                # Combine all transformations to get the landmark position in NAO space.

                robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform * cameraToLandmarkTranslationTransform
                landMarkProxy.unsubscribe("Test_LandMark")
                # print  "landmark detect",robotToLandmark.r1_c4,robotToLandmark.r2_c4,robotToLandmark.r3_c4,distanceFromCameraToLandmark
                return 1, robotToLandmark.r1_c4, robotToLandmark.r2_c4, robotToLandmark.r3_c4, distanceFromCameraToLandmark
            else:
                wzCamera = markData[1][0][0][1]
                wyCamera = markData[1][0][0][2]

                # Retrieve landmark angular size in radians.
                angularSize = markData[1][0][0][3]

                # Compute distance to landmark.
                distanceFromCameraToLandmark = landmarkTheoreticalSize / (2 * math.tan(angularSize / 2))

                motionProxy = ALProxy("ALMotion", ip, 9559)

                # Get current camera position in NAO space.
                transform = motionProxy.getTransform(currentCamera, 2, True)
                transformList = almath.vectorFloat(transform)
                robotToCamera = almath.Transform(transformList)

                # Compute the rotation to point towards the landmark.
                cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, wyCamera, wzCamera)

                # Compute the translation to reach the landmark.
                cameraToLandmarkTranslationTransform = almath.Transform(distanceFromCameraToLandmark, 0, 0)

                # Combine all transformations to get the landmark position in NAO space.

                robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform * cameraToLandmarkTranslationTransform
                landMarkProxy.unsubscribe("Test_LandMark")
                # print  "landmark detect", robotToLandmark.r1_c4, robotToLandmark.r2_c4, robotToLandmark.r3_c4, distanceFromCameraToLandmark
                return 1, robotToLandmark.r1_c4, robotToLandmark.r2_c4, robotToLandmark.r3_c4, distanceFromCameraToLandmark

    landMarkProxy.unsubscribe("Test_LandMark")
    # print  "landmark detect fff"
    return 0, 0, 0, 0, 0


def DetecteLandmark_my():
    xx = 0.0
    for i in range(0, 5):
        # time.sleep(1.0)
        size, left, xx = landmark1.landmarkdetect(IP, PORT, 0)
        if ((size != 0) & (left != 0)):
            return 1, size, left, xx
        else:
            # print  "landmark_my detect fff"
            return 0, 0, 0, 0


# ***************************************************
def closeball1_sub_far():
    pass


# to cancel the effect of landmark
def closeball1_sub_land():
    DetecteLandmark()


# close to down cam,and adjust the just position to ball
def closeball1(threshold):
    LEFT_ = 0
    redball000.lookat(robotIP, PORT)
    count = 1
    count0 = 0
    flag_p = 0
    flag_n = 0
    while (1):
        if (count0 == 10):
            Movey(0.5)
        size, left, top, cam, isfind = redball000.findball(robotIP, PORT)
        if (isfind == 1):

            if (cam == 1):

                if (left <= threshold) & (left >= -threshold):
                    break
                elif (left > threshold):
                    flag_p = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_n = 0
                    x = 0.0
                    y = 0.0
                    theta = -1 * math.pi / (10 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)

                elif (left < - threshold):
                    flag_n = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_p = 0
                    x = 0.0
                    y = 0.0
                    theta = math.pi / (10 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)
            else:
                if (top <= -10):
                    if (left < 30):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 30):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.45)
                elif (-10 <= top <= 50):
                    if (left < 25):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 25):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.30)
                else:
                    if (left < 25):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 25):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.15)


        else:
            if (LEFT_ == 0):
                count0 = count0 + 1
                x = 0.0
                y = 0.0
                theta = math.pi / 8
                motionProxy.moveTo(x, y, theta)
            else:
                count0 = count0 + 1
                x = 0.0
                y = 0.0
                theta = -math.pi / 8
                motionProxy.moveTo(x, y, theta)


# **********************************
def oldclose(threshold):
    LEFT_ = 0
    redball000.lookat(robotIP, PORT)
    count = 1
    flag_p = 0
    flag_n = 0
    while (1):
        size, left, top, cam, isfind = redball000.findball(robotIP, PORT)
        if (isfind == 1):

            if (cam == 1):

                if (left <= threshold) & (left >= -threshold):
                    break
                elif (left > threshold):
                    flag_p = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_n = 0
                    x = 0.0
                    y = 0.0
                    theta = -1 * math.pi / (8 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)

                elif (left < - threshold):
                    flag_n = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_p = 0
                    x = 0.0
                    y = 0.0
                    theta = math.pi / (8 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)
            else:
                Movex(0.25)
                if (left < 20):
                    x = 0.0
                    y = 0.0
                    theta = math.pi / 16
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)
                elif (left > 20):
                    x = 0.0
                    y = 0.0
                    theta = -1 * math.pi / 16
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)
        else:
            if (LEFT_ == 0):
                x = 0.0
                y = 0.0
                theta = math.pi / 8
                motionProxy.moveTo(x, y, theta)
            else:
                x = 0.0
                y = 0.0
                theta = -math.pi / 8
                motionProxy.moveTo(x, y, theta)


# **************************8
def closeball1_right(threshold):
    LEFT_ = 0
    redball000.lookat(robotIP, PORT)
    count = 1
    count0 = 0
    flag_p = 0
    flag_n = 0
    while (1):
        if (count0 == 10):
            Movey(0.5)
        size, left, top, cam, isfind = redball000.findball(robotIP, PORT)
        if (isfind == 1):

            if (cam == 1):

                if (left <= threshold) & (left >= -threshold):
                    break
                elif (left > threshold):
                    flag_p = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_n = 0
                    x = 0.0
                    y = 0.0
                    theta = -1 * math.pi / (10 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)

                elif (left < - threshold):
                    flag_n = 1
                    if ((flag_p == 1) & (flag_n == 1)):
                        count = count + 1
                        flag_p = 0
                    x = 0.0
                    y = 0.0
                    theta = math.pi / (10 * (2 * count))
                    motionProxy.moveTo(x, y, theta)
                    time.sleep(1.5)
            else:
                if (top <= -10):
                    if (left < 30):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 30):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.45)
                elif (-10 <= top <= 50):
                    if (left < 25):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 25):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.30)
                else:
                    if (left < 25):
                        x = 0.0
                        y = 0.0
                        theta = math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    elif (left > 25):
                        x = 0.0
                        y = 0.0
                        theta = -1 * math.pi / 15
                        motionProxy.moveTo(x, y, theta)
                        time.sleep(1.5)
                    Movex(0.15)


        else:
            if (LEFT_ == 0):
                count0 = count0 + 1
                x = 0.0
                y = 0.0
                theta = math.pi / 8
                motionProxy.moveTo(x, y, theta)
            else:
                count0 = count0 + 1
                x = 0.0
                y = 0.0
                theta = -math.pi / 8
                motionProxy.moveTo(x, y, theta)


# *********************************************************
def closeball2(threshold, close1):
    redball000.lookat(robotIP, PORT)
    while (1):

        size, left, top, cam, isfind = redball000.findball(robotIP, PORT)
        if (isfind == 1):

            if (top >= threshold):
                closeball1(close1)
                break



            elif (-60 <= top < 20):
                x = 0.02
                y = 0.0
                theta = 0
                motionProxy.moveTo(x, y, theta)
                time.sleep(1.8)
                closeball1(close1)
            elif (20 <= top < threshold):
                x = 0.02
                y = 0.0
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(1.8)
                closeball1(27)

            elif (top < -60):
                x = 0.07
                y = 0.0
                theta = 0.0
                motionProxy.moveTo(x, y, theta)
                time.sleep(1.8)

        else:
            pass



            #  distance in meter 0.011


def runtohitball90(threshold, topdistance, ditance):
    # turn head
    # detecteland
    # Movex(-0.08)
    close1_ = 23

    count = 0
    while (1):
        names = ["HeadPitch", "HeadYaw"]
        angleLists = [0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
        timeLists = [1.0, 2.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(2.0)

        isfindLand, x, y, z, d = DetecteLandmark()

        time.sleep(2.0)
        # print  "landmark"
        if (isfindLand == 0):
            # print x, threshold + ditance, ditance - threshold
            count = count + 1
            Movey(0.10)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)
        elif (((x - ditance) < threshold) & ((x - ditance) > -threshold)):
            # print x,threshold+ditance,ditance-threshold
            return x, y, z, d
        elif (x - ditance < -threshold):
            # print x, threshold + ditance, ditance - threshold
            Movey(-0.02)
            redball000.lookat(robotIP, PORT)
            # *************************************
            closeball1(17)
            closeball2(topdistance, close1_)
        else:
            count = count + 1
            Movey(0.05)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)


# *************************************************
def runtohitball90_n(threshold, topdistance, ditance):
    # turn head
    # detecteland
    # Movex(-0.08)
    close1_ = 23
    count = 0
    while (1):
        names = ["HeadPitch", "HeadYaw"]
        angleLists = [0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
        timeLists = [1.0, 2.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(2.0)

        isfindLand, x, y, z, d = DetecteLandmark()

        time.sleep(2.0)
        # print  "landmark"
        if (isfindLand == 0):
            count = count + 1
            Movey(-0.06)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)
        elif (((x - ditance) < threshold) & ((x - ditance) > -threshold)):
            return x, y, z, d
        elif ((x - ditance) < threshold):

            Movey(0.02)
            redball000.lookat(robotIP, PORT)
            # *************************************
            closeball1(17)
            closeball2(topdistance, close1_)
        else:
            count = count + 1
            Movey(-0.03)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)


# **************************************
def newruntohitball(threshold, topdistance, ditance):
    # turn head
    # detecteland
    # Movex(-0.08)
    close1_ = 23
    count = 0
    fivefindlandmark = 0
    while (1):
        names = ["HeadPitch", "HeadYaw"]
        angleLists = [0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
        timeLists = [1.0, 2.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(2.0)
        isfindLand, x, y, z, d = DetecteLandmark()
        time.sleep(2.0)
        # print  "landmark"
        # 90 degre cannot find
        if (isfindLand == 0):
            for i in range(0, 5):
                # ***********************
                names = ["HeadPitch", "HeadYaw"]
                angleLists = [0.0 * almath.TO_RAD, (60.0 - i * 30.0) * almath.TO_RAD]
                timeLists = [1.0, 2.0]
                isAbsolute = True
                motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                time.sleep(1.0)
                # *****************************
                isfindLand, x, y, z, d = DetecteLandmark()
                # find landmark

                if (isfindLand == 1):
                    if (i == 0):
                        t_ = 0.08
                    elif (i == 1):
                        t_ = 0.12
                    elif (i == 2):
                        t_ = 0.16
                    elif (i == 3):
                        t_ = 0.20
                    elif (i == 4):
                        t_ = 0.24
                    elif (i == 5):
                        t_ = 0.30
                    Movey(t_)
                    Movet(-0.75 * (math.atan(t_ / ditance)))
                    fivefindlandmark = 1
                    break
                else:
                    pass
            if (fivefindlandmark == 0):
                t_ = 0.30
                Movey(t_)
                Movet(0.75 * math.atan(t_ / ditance))
            closeball1(20)
            closeball2(topdistance, close1_)



        elif (((x - ditance) < threshold) & ((x - ditance) > -threshold)):
            # print x,threshold+ditance,ditance-threshold
            return x, y, z, d
        elif (x - ditance < -threshold):
            # print x, threshold + ditance, ditance - threshold
            Movey(-0.04)
            redball000.lookat(robotIP, PORT)
            # *************************************
            closeball1(17)
            closeball2(topdistance, close1_)
        else:
            count = count + 1
            Movey(0.04)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)


# **************************************




def runtohitball(threshold, topdistance, ditance):
    # ***********************
    close1_ = 23
    names = ["HeadPitch", "HeadYaw"]
    angleLists = [0.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
    timeLists = [1.0, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    # *****************************
    while (1):
        isfindLand, x, y, z, d = DetecteLandmark()
        # find landmark
        if (isfindLand == 1):
            if (x < 0):
                # this value need y=0.25+((-x)/y)*(-x),x=0.25
                Movey(0.3)
                Movex(0.3 + (((-x) / y) * (-x)))
                # print (0.25+(((-x)/y)*(-x)))
                # 20cm -> value  = 50?
                closeball1(17)
                closeball2(topdistance, close1_)
                return runtohitball90(threshold, topdistance, ditance)
            if (x >= 0):
                # theoretics value
                mm = (-0.2 / (math.tan(((3.14159 / 4) - math.atan(x / y)))))
                # print mm
                Movey(mm)
                # Movey(0.15)
                closeball1(17)
                closeball2(topdistance, close1_)
                return runtohitball90(threshold, topdistance, ditance)
        # if not find ball
        else:
            # first consider the best position

            # ***********************
            names = ["HeadPitch", "HeadYaw"]
            angleLists = [0.0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
            timeLists = [1.0, 2.0]
            isAbsolute = True
            motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
            time.sleep(1.0)

            # *****************************


            isfindLand, x, y, z, d = DetecteLandmark()
            if (isfindLand == 1):
                closeball1(17)
                closeball2(topdistance, close1_)
                return runtohitball90(threshold, topdistance, ditance)

            else:
                for i in range(0, 5):
                    # ***********************
                    names = ["HeadPitch", "HeadYaw"]
                    angleLists = [0.0 * almath.TO_RAD, (30.0 + i * 30.0) * almath.TO_RAD]
                    timeLists = [1.0, 2.0]
                    isAbsolute = True
                    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                    time.sleep(1.0)

                    # *****************************

                    isfindLand, x, y, z, d = DetecteLandmark()
                    # find landmark
                    if (isfindLand == 1):
                        if (i == 0):
                            Movey(0.05)
                            closeball1(17)
                            closeball2(topdistance, close1_)
                            return runtohitball90(threshold, topdistance, ditance)
                        if (i <= 3):
                            return runtohitball90(threshold, topdistance, ditance)
                        if (i == 4):
                            if (x >= 0):
                                return runtohitball90(threshold, topdistance, ditance)
                            else:
                                return runtohitball90_n(threshold, topdistance, ditance)
                        if (i == 5):
                            if (x >= 0):
                                return runtohitball90(threshold, topdistance, ditance)
                            else:
                                return runtohitball90_n(threshold, topdistance, ditance)
                        break

                    else:
                        pass

                # ******************************

                names = ["HeadPitch", "HeadYaw"]
                angleLists = [0.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
                timeLists = [1.0, 2.0]
                isAbsolute = True
                motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                time.sleep(1.0)

                # *********************************************
                for i in range(0, 5):

                    # ***********************
                    names = ["HeadPitch", "HeadYaw"]
                    angleLists = [0.0 * almath.TO_RAD, -1 * (30.0 + i * 30.0) * almath.TO_RAD]
                    timeLists = [1.0, 2.0]
                    isAbsolute = True
                    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                    time.sleep(1.0)

                    # *****************************

                    isfindLand, x, y, z, d = DetecteLandmark()
                    # find landmark
                    # find landmark
                    if (isfindLand == 1):
                        if (i <= 3):
                            Movey(0.9)
                            Movex(0.45)
                            Movet(-math.pi / 1.5)
                            closeball1(17)
                            closeball2(topdistance, close1_)
                            return runtohitball90(threshold, topdistance, ditance)
                        if (i == 4):
                            Movey(1.0)
                            Movex(0.5)
                            Movet(-math.pi / 1.5)
                            closeball1(17)
                            closeball2(topdistance, close1_)
                            return runtohitball90(threshold, topdistance, ditance)

                        if (i == 5):
                            Movey(1.4)
                            Movex(1.2)
                            Movet(-math.pi / 1.5)
                            closeball1(17)
                            closeball2(topdistance, close1_)
                            return runtohitball90(threshold, topdistance, ditance)

                        break

                    else:
                        pass

        Movey(0.4)
        Movex(0.5)
        break


# ***************************************************************************************
def far_ball():
    close1_ = 23
    topdistance = 30
    Ldistance = 30
    threshold = 20
    while (1):
        isfindLand, size, x, ss = DetecteLandmark_my()
        if (isfindLand == 0):
            count = count + 1
            Movey(0.06)
            redball000.lookat(robotIP, PORT)
        elif (((x - Ldistance) < threshold) & ((x - Ldistance) > -threshold)):
            return size
        elif (x - Ldistance < -threshold):
            Movey(-0.02)
            closeball1(17)
            closeball2(topdistance, close1_)


# ********************************************************************************** -70~-190
# -60,
def runtohitball90_far(threshold, topdistance, ditance):
    # turn head
    # detecteland
    # Movex(-0.08)
    adj = 0.08
    close1_ = 23
    count = 0
    while (1):
        names = ["HeadPitch", "HeadYaw"]
        angleLists = [0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
        timeLists = [1.0, 2.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(2.0)

        isfindLand, size, x, ss = DetecteLandmark_my()
        # print x,threshold+ditance,ditance-threshold
        time.sleep(2.0)
        # print  "landmark"
        if (isfindLand == 0):
            count = count + 1
            Movey(0.12)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)

        elif (((x - ditance) > threshold) & ((x - ditance) < -threshold)):
            return size, x
        elif ((x - ditance) < threshold):

            Movey(-0.03)
            redball000.lookat(robotIP, PORT)
            # *************************************
            closeball1(17)
            closeball2(topdistance, close1_)
        else:
            count = count + 1
            Movey(0.04)
            redball000.lookat(robotIP, PORT)
            closeball1(17)
            closeball2(topdistance, close1_)


# **********************************************************************************
def newruntohitball_far(threshold, topdistance, ditance):
    xx = 0.0
    i = 0
    close1_ = 27
    count = 0
    fivefindlandmark = 0
    while (1):
        names = ["HeadPitch", "HeadYaw"]
        angleLists = [0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
        timeLists = [1.0, 2.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(2.0)
        isfindLand, size, xx, ss = DetecteLandmark_my()
        # print xx,threshold+ditance,ditance-threshold
        # time.sleep(2.0)
        # print  "landmark"
        # 90 degre cannot find
        if (isfindLand == 0):
            while (1):
                # ***********************
                names = ["HeadPitch", "HeadYaw"]
                angleLists = [0.0 * almath.TO_RAD, (90.0 - i * 30.0) * almath.TO_RAD]
                timeLists = [1.0, 2.0]
                isAbsolute = True
                motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                time.sleep(1.0)
                # *****************************
                isfindLand, size, xx, ss = DetecteLandmark_my()
                # find landmark

                if (isfindLand == 1):
                    if (i == 0):
                        t_ = 0.08
                    elif (i == 1):
                        t_ = 0.12
                    elif (i == 2):
                        t_ = 0.16
                    elif (i == 3):
                        t_ = 0.20
                    elif (i == 4):
                        t_ = 0.24
                    elif (i == 5):
                        t_ = 0.30
                    Movey(t_)
                    Movet(-(math.atan(t_ / ditance) + math.pi / 16))
                    fivefindlandmark = 1
                    i = i + 1
                    i = 0
                    break
                else:
                    i = i + 1
                    pass

                if (i == 6):
                    i = 0
                    break
            if (fivefindlandmark == 0):
                t_ = 0.30
                Movey(t_)
                Movet(-(math.atan(t_ / ditance) + math.pi / 16))
            closeball1(close1_)
            closeball2(topdistance, close1_)



        elif (((xx - ditance) > threshold) & ((xx - ditance) < -threshold)):
            return size, xx
        else:
            count = count + 1
            Movey(0.04)
            redball000.lookat(robotIP, PORT)
            closeball1(close1_)
            closeball2(topdistance, close1_)


# **********************************special for 1   3****

def runtolandmark_face(threshold):
    flag_n = 0
    flag_p = 0
    count = 1
    ##print "s"
    while (1):
        isfindLand, size, left, xx = DetecteLandmark_my()
        # print "my",xx
        if (isfindLand == 0):
            Movet(math.pi / 6)
        else:
            if (left <= threshold) & (left >= -threshold):
                # print "return",size,left,xx
                return size, left, xx

            elif (left > threshold):
                flag_p = 1
                if ((flag_p == 1) & (flag_n == 1)):
                    count = count + 1
                    flag_n = 0
                x = 0.0
                y = 0.0
                theta = -1 * math.pi / (8 * (2 * count))
                motionProxy.moveTo(x, y, theta)
                time.sleep(1.5)

            elif (left < - threshold):
                flag_n = 1
                if ((flag_p == 1) & (flag_n == 1)):
                    count = count + 1
                    flag_p = 0
                x = 0.0
                y = 0.0
                theta = math.pi / (8 * (2 * count))
                motionProxy.moveTo(x, y, theta)
                time.sleep(1.5)


# ***********************************************************************************
def runtolandmark13(threshold):
    while (1):
        size, left, x = runtolandmark_face(50)
        if (x <= threshold):
            break
        elif (x >= 3.5):
            Movex(0.45)
        elif (x >= 2.5):
            Movex(0.3)
        elif (x >= 1.5):
            Movex(0.2)


# *******************************************************************************
def runtolandmark2(threshold):
    runtolandmark13(threshold)
    Movex(0.5)


# **********************************************************************************
def runtohitball_far(topdistance):
    # ***********************
    close1_ = 23
    closeball1(17)
    # **************
    closeball2(30, close1_)  # 55

    names = ["HeadPitch", "HeadYaw"]
    angleLists = [0.0 * almath.TO_RAD, 0.0 * almath.TO_RAD]
    timeLists = [1.0, 2.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)

    # *****************************
    while (1):
        isfindLand, size, x, ss = DetecteLandmark_my()
        # find landmark
        if (isfindLand == 1):
            if (x < 0):
                # this value need y=0.25+((-x)/y)*(-x),x=0.25
                # ***********************************
                names = ["HeadPitch", "HeadYaw"]
                angleLists = [0.0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
                timeLists = [1.0, 2.0]
                isAbsolute = True
                motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                time.sleep(1.0)
                far_ball()
                # **************************************
                return size
            if (x >= 0):
                # ***************
                names = ["HeadPitch", "HeadYaw"]
                angleLists = [0.0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
                timeLists = [1.0, 2.0]
                isAbsolute = True
                motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
                time.sleep(1.0)
                far_ball()
                # ********************
                return size
        # if not find ball
        else:
            # first consider the best position
            # ***********************


            # *****************************
            names = ["HeadPitch", "HeadYaw"]
            angleLists = [0.0 * almath.TO_RAD, 90.0 * almath.TO_RAD]
            timeLists = [1.0, 2.0]
            isAbsolute = True
            motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
            time.sleep(1.0)
            return far_ball()

        break


def first(robotIP, PORT):
    leftArmEnable = False
    rightArmEnable = False
    motionProxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)

    HitBall(0.43)
    Movex(0.01)  # xxxxxxxxxxxxxxxxxxxxxxxxxxx
    time.sleep(1.0)
    Movet(math.pi / 2)
    Movex(0.9)
    while (1):
        # Movet(math.pi/2.8)
        # run to ball
        closeball1(23)
        # #**************
        closeball2(30, 23)
        # run to hit ball position   wtih 0


        x0, y0, z0, dis = newruntohitball(0.10, 30, 0.22)
        Movex(-0.02)

        # closeball2(58, 25)
        # choose power depending on the distant
        if (dis < 1.0):

            HitBall(0.42)

        elif (dis <= 1.2):
            HitBall(0.42)
        elif (dis >= 1.2):
            HitBall(0.42)


def second(robotIP, PORT):
    # hitball  max=0.27
    leftArmEnable = False
    rightArmEnable = False
    motionProxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)
    # ******************************************
    HitBall(0.42)  # 2 0.45eeeeeeeeeeeeeeeeeeeeeee xxxxxxxxxxx
    Movex(0.01)  # xxxxxxxxxxxxxxxxxxxxxxxxxxx
    time.sleep(1.0)
    Movet(math.pi / 2)  # 2eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxxxx
    Movex(0.4)
    runtolandmark_face(70)
    runtolandmark13(2.9)
    Movey(-0.9)
    Movex(1.0)
    runtolandmark_face(50)
    runtolandmark13(2.0)
    # ******************************************


    while (1):
        # Movet(math.pi/2.8)
        # run to ball
        closeball1(23)
        # #**************
        closeball2(30, 23)
        # run to hit ball position   wtih 0


        x0, y0, z0, dis = newruntohitball(0.10, 30, 0.22)
        Movex(-0.02)

        # closeball2(58, 25)
        # choose power depending on the distant
        if (dis < 1.0):

            HitBall(0.42)

        elif (dis <= 1.2):
            HitBall(0.42)
        elif (dis >= 1.2):
            HitBall(0.42)


def third(robotIP, PORT):
    leftArmEnable = False
    rightArmEnable = False
    motionProxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)
    #     #******************************************3******************************************

    HitBall(0.8)  ##333eeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    Movex(0.01)  # hold,maintance    eeeeeeeeeeeeeeeeeee
    time.sleep(1.0)
    Movet(math.pi / 1.9)  # 3333333333eeeeeeeeeeeeeeeeeeeeeeeeeee
    #
    Movex(0.3)  # cancel eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # Movet(-math.pi / 4)#333333
    # #
    # #
    closeball1(23)  # eeeeeeeeeeeeeeeeeeeeeee
    # # # # # # # **************
    # Movey(0.3)#33333333333eeeeeeeeeeeeeeeeeeeeeeeee
    # Movex(0.4)#333333333
    # Movet(-math.pi / 1.2)
    # # # # run to hit ball position   wtih 0
    # # #
    # closeball1(23)#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # # # # # **************
    closeball2(30, 23)  # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # size,x= runtohitball90_far(-60 , 30 ,-130)
    newruntohitball_far(-85, 30, -115)  # 30eeeeeeeeeeeeeeeeeeeeeeeeee
    HitBall(0.41)
    runtolandmark_face(70)
    runtolandmark13(1.8)
    # #print "SS",x
    # closeball2(49, 23)
    # # # choose power depending on the distant
    # #
    # #
    # HitBall(0.41)#eeeeeeeeeeeeeeeeeeeeeeeeeee
    # Movet(math.pi / 1.8)#eeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # Movex(1.6)#eeeeeeeeeeeeeeeeeeeeeeeee
    while (1):
        # Movet(math.pi/2.8)
        # run to ball
        closeball1(23)
        # #**************
        closeball2(30, 23)
        # run to hit ball position   wtih 0


        x0, y0, z0, dis = newruntohitball(0.10, 30, 0.22)
        Movex(-0.02)

        # closeball2(58, 25)
        # choose power depending on the distant
        if (dis < 1.0):

            HitBall(0.42)

        elif (dis <= 1.2):
            HitBall(0.42)
        elif (dis >= 1.2):
            HitBall(0.42)






