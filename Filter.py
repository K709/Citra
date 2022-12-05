import cv2 as cv
import numpy as np

def pencil(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    neg = 255-gray
    blur = cv.GaussianBlur(neg,ksize=(21,21),sigmaX=0,sigmaY=0)

    dodge = cv.divide(gray,255-blur,scale=256)
    burn = 255-cv.divide(255-dodge,255-blur,scale=256)

    return burn

def cartoonize(img):
    img_grey  = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    img_blur = cv.medianBlur(img_grey,3)
    img_bb = cv.bilateralFilter(img, 15, 75,75)
    edges = cv.adaptiveThreshold(img_blur,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 3)

    imgf=np.float32(img_bb).reshape(-1,3)
    criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,20,1.0)
    compactness,label,center=cv.kmeans(imgf,5,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
    center=np.uint8(center)
    final_img=center[label.flatten()]
    final_img=final_img.reshape(img_bb.shape)
    final=cv.bitwise_and(final_img,final_img,mask=edges)

    return final

def cekSepia(n):
    if n > 255:
        return 255
    else:
        return n

def sephia(img):
    image = np.array(img)
    for i in range(len(image)):
        for j in range(len(image[0])):
            tr = (
                (image[i, j, 2] * 0.393)
                + (image[i, j, 1] * 0.769)
                + (image[i, j, 0] * 0.189)
            )
            tg = (
                (image[i, j, 2] * 0.349)
                + (image[i, j, 1] * 0.686)
                + (image[i, j, 0] * 0.168)
            )
            tb = (
                (image[i, j, 2] * 0.272)
                + (image[i, j, 1] * 0.534)
                + (image[i, j, 0] * 0.131)
            )
            image[
                i,
                j,
            ] = (cekSepia(tb), cekSepia(tg), cekSepia(tr))
    image=cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image

def anaglyph(img):
    add_red = np.full([img.shape[0],img.shape[1],3],[0,0,255], 'uint8')
    add_blue = np.full([img.shape[0],img.shape[1],3],[255,0,0], 'uint8')
    slide = 20

    red = img.copy()
    red = red[:, slide:red.shape[1]]
    red[:,:,0] = red[:,:,1] = 0
    red_copy = add_red.copy()
    red_copy[:red.shape[0],:red.shape[1]] = red

    blue = img.copy()
    blue = blue[:, 0:blue.shape[1]-slide]
    blue[:,:,1] = blue[:,:,2] = 0
    blue_copy = add_blue.copy()
    blue_copy[0:img.shape[0],slide:img.shape[1]] = blue

    green = img.copy()
    green[:,:,0] = green[:,:,2] = 0

    multiply = cv.bitwise_or(green,red_copy)
    multiply = cv.bitwise_or(multiply,blue_copy)

    return multiply