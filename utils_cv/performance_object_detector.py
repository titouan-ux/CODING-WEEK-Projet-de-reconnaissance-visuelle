import os
import tensorflow.keras.applications.resnet50
from utils_cv.recognition import ind_max
from utils_cv.load import absolut_path
from utils_cv.dico_predators import predators
from utils_cv.transformation import resize_image
from utils_cv.detector.detect_with_classifier import object_detector

model = tensorflow.keras.applications.resnet50.ResNet50(
    classifier_activation='softmax')

def performance_object_detector():
    """ 
    Parameters
    ----------
    Returns
    -------
    (float,float)
        The first float is the rate of well recognized animals in the data base using the function object_detector in order to find the animal on the photo.
        The second float is the rate of predators that are recognized in the data base.
        Rates are betwenn 0 and 1.
        """
    predateur_detecte = 0
    animal_reconnu = 0
    total = 0
    path = absolut_path("..\\images_performance")
    for directory in os.listdir(path):
        for file_name in os.listdir(os.path.join(path, directory)): #we run through the database
            images=object_detector(absolut_path(path+'\\'+directory+'\\'+file_name))
            boo=True
            for img in images: #we run through the differents object dtected
                if boo:  #once we detected a predator we go to the next image
                    img = resize_image(img, (224, 224))
                    img = img.reshape(1, 224, 224, 3)
                    ftures = model.predict(img)
                    ls_proba = ftures[0]
                    index_animal = ind_max(ls_proba)[0]

                    if index_animal in predators:
                        predateur_detecte += 1
                        animal = predators[index_animal]
                        boo=False
                        if directory in animal:
                            animal_reconnu += 1
            total += 1      

    return (animal_reconnu/total, predateur_detecte/total)
