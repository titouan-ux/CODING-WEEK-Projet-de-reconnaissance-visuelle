import cv2


def resize_image(img, new_dim):
    """resizes image

    Parameters
    ----------
    img: array
        image to be resized

    new_dim: tuple of 2
        dims of new image

    Returns
    -------
    np array
        new image"""
    return cv2.resize(img, new_dim)


def BGR_to_gray(image):
    """transform an image in black and white

    Parameters
    ----------
    img: array
        image to be smoothed

    Returns
    -------
    greyscale img (array)"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
