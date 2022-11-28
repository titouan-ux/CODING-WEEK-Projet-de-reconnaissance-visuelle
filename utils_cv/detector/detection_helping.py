from utils_cv.detector.utilitary import resize


def sliding_window(image, step, ws):
    """sliding window

    Browse the image with a rectangle 

    Parameters
    ----------
    image : image to analyze (np.array)
    step : step of the slicing (float)
    ws: window  size (tuple of len = 2)
    -------
    """
    # slide a window across the image
    for y in range(0, image.shape[0] - ws[1], step):
        for x in range(0, image.shape[1] - ws[0], step):
            # yield the current window
            yield (x, y, image[y:y + ws[1], x:x + ws[0]])


def image_pyramid(image, scale=1.5, minSize=(224, 224)):
    """image_pyramid

        Parameters
        ----------
        image : image to analyze (np.array)
        scale : scale of the image modified during pyramid
        minSize : size minimum

        Returns
        -------
        np array
            new image"""
    # yield the original image
    yield image
    # keep looping over the image pyramid
    while True:
        # compute the dimensions of the next image in the pyramid
        w = int(image.shape[1] / scale)
        image = resize(image, width=w)
        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        # yield the next image in the pyramid
        yield (image)