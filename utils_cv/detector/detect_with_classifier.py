from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
import tensorflow.keras.applications.resnet50
from utils_cv.detector.utilitary import resize
from utils_cv.detector.detection_helping import sliding_window, image_pyramid
import numpy as np
import time
import cv2


WIDTH = 600
PYR_SCALE = 1.5
WIN_STEP = 16
ROI_SIZE = (200, 150)
INPUT_SIZE = (224, 224)

model = tensorflow.keras.applications.resnet50.ResNet50(
    classifier_activation='softmax')

# load the input image from disk, resize it such that it has the
# has the supplied width, and then grab its dimensions


def object_detector(filename,min_conf=0.8, visualize = -1):
    """object_detector

    Parameters
    ----------
    filename: name of the file (str)
    min_conf : minimum for the detection (float)
    visualize : number in order to visualize photos or not (array). No vizualisation if number is negative

    Returns
    -------
    ls_image : list of objects detected (list of np.array)
    """
    # orig = cv2.imread(absolut_path("../"+ filename))
    orig = cv2.imread(filename)
    try:
        orig = resize(orig, width=WIDTH)
    except AttributeError:
        return ()
    (H, W) = orig.shape[:2]
    # initialize the image pyramid
    pyramid = image_pyramid(orig, scale=PYR_SCALE, minSize=ROI_SIZE)
    # initialize two lists, one to hold the ROIs generated from the image
    # pyramid and sliding window, and another list used to store the
    # (x, y)-coordinates of where the ROI was in the original image
    rois = []
    locs = []
    # time how long it takes to loop over the image pyramid layers and
    # sliding window locations
    start = time.time()

    # loop over the image pyramid
    for image in pyramid:
        # determine the scale factor between the *original* image
        # dimensions and the *current* layer of the pyramid
        scale = W / float(image.shape[1])
        # for each layer of the image pyramid, loop over the sliding
        # window locations
        for (x, y, roiOrig) in sliding_window(image, WIN_STEP, ROI_SIZE):
            # scale the (x, y)-coordinates of the ROI with respect to the
            # *original* image dimensions
            x = int(x * scale)
            y = int(y * scale)
            w = int(ROI_SIZE[0] * scale)
            h = int(ROI_SIZE[1] * scale)
            # take the ROI and preprocess it so we can later classify
            # the region using Keras/TensorFlow
            roi = cv2.resize(roiOrig, INPUT_SIZE)
            roi = img_to_array(roi)
            roi = preprocess_input(roi)
            # update our list of ROIs and associated coordinates
            rois.append(roi)
            locs.append((x, y, x + w, y + h))
            # check to see if we are visualizing each of the sliding
            # windows in the image pyramid
        if visualize > 0:
            # clone the original image and then draw a bounding box
            # surrounding the current region
            clone = orig.copy()
            cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # show the visualization and current ROI
            cv2.imshow("Visualization", clone)
            cv2.imshow("ROI", roiOrig)
            cv2.waitKey(50)
            cv2.destroyAllWindows

    # show how long it took to loop over the image pyramid layers and
    # sliding window locations
    end = time.time()
    print("[INFO] looping over pyramid/windows took {:.5f} seconds".format(
        end - start))
    # convert the ROIs to a NumPy array
    rois = np.array(rois, dtype="float32")
    # classify each of the proposal ROIs using ResNet and then show how
    # long the classifications took
    start = time.time()
    preds = model.predict(rois)
    end = time.time()
    print("[INFO] classifying ROIs took {:.5f} seconds".format(
        end - start))
    # decode the predictions and initialize a dictionary which maps class
    # labels (keys) to any ROIs associated with that label (values)
    preds = imagenet_utils.decode_predictions(preds, top=1)
    ls_image_crop = []

    # loop over the predictions
    for (i, p) in enumerate(preds):
        # 	# grab the prediction information for the current ROI
        (imagenetID, label, prob) = p[0]
        # filter out weak detections by ensuring the predicted probability
        # is greater than the minimum probability
        if prob >= min_conf:
            # grab the bounding box associated with the prediction and
            # convert the coordinates
            box = locs[i]
            (x, y, z, k) = box
            w = z-x
            h = k-y
            clone = orig.copy()
            crop_image = clone[y:y+h, x:x+w]
            ls_image_crop.append(crop_image)
    return(ls_image_crop)

