import cv2
import numpy as np

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

def max_ls(ls):
    """Parameters
    ----------
    list or np.array

    Returns
    -------
    int,float
        maximum of the input and index"""
    max=0
    indice=0
    for i in range(0,len(ls)):
        if ls[i]>max:
            indice=i
            max=ls[i]
    return(max,indice)