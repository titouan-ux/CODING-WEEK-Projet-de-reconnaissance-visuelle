import os
import tensorflow.keras.applications.resnet50
from utils_cv.recognition import ind_max
import cv2
from utils_cv.load import absolut_path
from utils_cv.dico_predators import predators
from utils_cv.transformation import resize_image

model = tensorflow.keras.applications.resnet50.ResNet50(
    classifier_activation='softmax')


def images_not_detected():
    """ 
    Parameters
    ----------
    Returns
    -------
    (float,float,dict)
        The first float is the rate of well recognized animals in the data base.
        The second float is the rate of predators that are recognized in the data base.
        Rates are betwenn 0 and 1.
        The dictionnary has for keys the photo and for values the animal detected.
        """
    predateur_detecte = 0
    animal_reconnu = 0
    total = 0
    erreurs = {}
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
                predateur_detecte += 1
                animal = predators[index_animal]              
                if directory in animal:
                    animal_reconnu += 1
                else:
                    erreurs[file_name]=predators[index_animal]
            total += 1

    return (animal_reconnu/total, predateur_detecte/total, erreurs)


print(images_not_detected())
