import os
import tensorflow.keras.applications.resnet50
from utils_cv.recognition import ind_max
import cv2
from utils_cv.load import absolut_path
from utils_cv.dico_predators import predators
from utils_cv.transformation import resize_image

model = tensorflow.keras.applications.resnet50.ResNet50(
    classifier_activation='softmax')


def performance():
    """ 
    Returns the rate of well-recognized animals and well-recognized predators.
    Parameters
    ----------
    Returns
    -------
    (float,float)
        The first float is the rate of well recognized animals in the data base.
        The second float is the rate of predators that are recognized in the data base.
        Rates are betwenn 0 and 1.
        """
    detected_predators = 0
    recognized_animals = 0
    total = 0

    path = absolut_path("../images_performance")
    for directory in os.listdir(path):
        for file_name in os.listdir(os.path.join(path, directory)):
            img = cv2.imread(os.path.join(path, directory, file_name))
            img = resize_image(img, (224, 224))
            img = img.reshape(1, 224, 224, 3)
            ftures = model.predict(img)
            ls_proba = ftures[0]
            index_animal = ind_max(ls_proba)[0]

            if index_animal in predators:
                detected_predators += 1
                animal = predators[index_animal]
                if directory in animal:
                    recognized_animals += 1
            total += 1

    return (recognized_animals/total, detected_predators/total)
