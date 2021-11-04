
import sys
# from PIL import Image
import cv2
import dlib
import faceBlendCommon as face
import numpy as np
import matplotlib.pyplot as plt
import cmapy
import os
PREDICTOR_PATH = r"shape_predictor_68_face_landmarks.dat"
faceDetector = dlib.get_frontal_face_detector()

def get_mpl_colormap(cmap_name):
    cmap = plt.get_cmap(cmap_name)

    # Initialize the matplotlib color map
    sm = plt.cm.ScalarMappable(cmap=cmap)

    # Obtain linear color range
    color_range = sm.to_rgba(np.linspace(0, 1, 256), bytes=True)[:,2::-1]

    return color_range.reshape(256, 1, 3)


def createEyeMask(eyeLandmarks, im):
    leftEyePoints = eyeLandmarks
    # Return an array of zeros with the same shape and type as a given array
    eyeMask = np.zeros_like(im)
    # draws a filled convex polygon
    cv2.fillConvexPoly(eyeMask, np.int32(leftEyePoints), (255, 255, 255))
    eyeMask = np.uint8(eyeMask)
    return eyeMask

def findIris(eyeMask, im, thresh):
    r = im[:,:,2]
    # thresh -> 255
    _, binaryIm = cv2.threshold(r, thresh, 255, cv2.THRESH_BINARY_INV)
    # The function constructs and returns the structuring element that can be further passed to cv.erode, cv.dilate
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
    # Dilates an image by using a specific structuring element
    morph = cv2.dilate(binaryIm, kernel, 1)
    # takes single channel images and combines them to make a multi-channel image
    morph = cv2.merge((morph, morph, morph))
    morph = morph.astype(float)/255
    eyeMask = eyeMask.astype(float)/255
    # Calculates the per-element scaled product of two arrays
    iris = cv2.multiply(eyeMask, morph)
    return iris
# Khối lượng tâm là giá trị trung bình đã cân của các pixel 
def findCentroid(iris):
    # mượn từ vật lý. Giả sử rằng mỗi pixel trong hình ảnh có trọng lượng bằng với cường độ của nó. 
    # Sau đó, điểm bạn xác định là centroid (còn gọi là khối tâm) của hình ảnh
    M = cv2.moments(iris[:,:,0])
    # m00 is a sum of gray levels if you calculate moments of an image
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    centroid = (cX,cY)
    return centroid

def createIrisMask(iris, centroid):
    # một danh sách các đường viền
    cnts, _ = cv2.findContours(np.uint8(iris[:,:,0]), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    flag = 10000
    final_cnt = None
    for cnt in cnts:
        # một hình tròn bao phủ hoàn toàn vật thể với diện tích tối thiểu
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        distance = abs(centroid[0]-x)+abs(centroid[1]-y)
        if distance < flag :
            flag = distance
            final_cnt = cnt
        else:
            continue
    (x,y),radius = cv2.minEnclosingCircle(final_cnt)
    center = (int(x),int(y))
    radius = int(radius) - 2

    irisMask = np.zeros_like(iris)
    inverseIrisMask = np.ones_like(iris)*255
    cv2.circle(irisMask,center,radius,(255, 255, 255),-1)
    cv2.circle(inverseIrisMask,center,radius,(0, 0, 0),-1)
    irisMask = cv2.GaussianBlur(irisMask, (5,5), cv2.BORDER_DEFAULT)
    inverseIrisMask = cv2.GaussianBlur(inverseIrisMask, (5,5), cv2.BORDER_DEFAULT)

    return irisMask, inverseIrisMask

def changeEyeColor(im, irisMask, inverseIrisMask,color_tag, Tag_type):
    if Tag_type == "opencv":
        imCopy = cv2.applyColorMap(im, int(color_tag))
    else:
        imCopy = cv2.applyColorMap(im,get_mpl_colormap(color_tag))
    imCopy = imCopy.astype(float)/255
    irisMask = irisMask.astype(float)/255
    inverseIrisMask = inverseIrisMask.astype(float)/255
    im = im.astype(float)/255
    faceWithoutEye = cv2.multiply(inverseIrisMask, im)
    newIris = cv2.multiply(irisMask, imCopy)
    result = faceWithoutEye + newIris
    return result

def float642Uint8(im):
    im2Convert = im.astype(np.float64) / np.amax(im)
    im2Convert = 255 * im2Convert 
    convertedIm = im2Convert.astype(np.uint8)
    return convertedIm

image_fullpath=sys.argv[1]
image_name=sys.argv[2]
color_map_tag = sys.argv[3]
Tag_type = sys.argv[4]
left_eye_thres = sys.argv[5]
right_eye_thres = sys.argv[6]

print("color_map_tag",color_map_tag)
print(type(color_map_tag))
img= cv2.imread(image_fullpath)#Image.open(str(image_fullpath))
image_save_path=image_fullpath.replace(image_fullpath,'result.jpg')


print('image_save_path',image_save_path)

landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)
landmarks = face.getLandmarks(faceDetector, landmarkDetector, img)

# Create eye mask using eye landmarks from facial landmark detection

leftEyeMask = createEyeMask(landmarks[36:42], img)
rightEyeMask = createEyeMask(landmarks[42:48], img)


# Find the iris by thresholding the red channel of the image within the boundaries of the eye mask
width, height,channel = img.shape

leftIris = findIris(leftEyeMask, img, int(left_eye_thres))
rightIris = findIris(rightEyeMask, img, int(right_eye_thres))  
# Find the centroid of the binary image of the eye
leftIrisCentroid = findCentroid(leftIris)
rightIrisCentroid = findCentroid(rightIris)

# Generate the iris mask and its inverse mask
leftIrisMask, leftInverseIrisMask = createIrisMask(leftIris, leftIrisCentroid)
rightIrisMask, rightInverseIrisMask = createIrisMask(rightIris, rightIrisCentroid)

# Change the eye color and merge it to the original image

coloredEyesLady = changeEyeColor(img, rightIrisMask, rightInverseIrisMask,color_map_tag,Tag_type)
coloredEyesLady = float642Uint8(coloredEyesLady)
coloredEyesLady = changeEyeColor(coloredEyesLady, leftIrisMask, leftInverseIrisMask,color_map_tag,Tag_type)


cv2.imwrite("C://Users//Admin//XLA//django_project//static//output//result.jpg",255*coloredEyesLady)

