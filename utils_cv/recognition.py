import tensorflow.keras.applications.resnet50
from utils_cv.dico_predators import predators
from utils_cv.transformation import resize_image


model = tensorflow.keras.applications.resnet50.ResNet50(
    classifier_activation='softmax')


def ind_max(ls):
    """Parameters
    ----------
    list or np.array

    Returns
    -------
    int,float
        index and maximum of the input"""
    ind, max = 0, ls[0]
    for i in range(0, len(ls)):
        if ls[i] > max:
            max = ls[i]
            ind = i
    return(ind, ls[ind])


def drop(ls, a):
    """Parameters
    ----------
    list or np.array, element wished to delete

    Returns
    -------
    list or np.array
        input without the element"""
    new = []
    for elem in ls:
        if elem != a:
            new.append(elem)
    return(new)


def recognition(image, precision=0.8):
    """ 
    Parameters
    ----------
    image : np.array
    precision : float
        name of photo file
        precison (sum of all probability of predators) with a default value of 0.8
    Returns
    -------
    str,float or list of str
        Name of the animal, followed by the probability of recognition
        Error message si nor predator are detected
        """
    image = resize_image(image, (224, 224))
    image = image.reshape(1, 224, 224, 3)
    ftures = model.predict(image)
    ls_proba = ftures[0]
    ind_animals, proba = ind_max(ls_proba)
    proba_predator = 0
    for index_animals in predators:
        proba_predator += ls_proba[index_animals]
    if proba_predator > precision:
        animal = predators[ind_animals]
        return((proba,animal))
    else:
        return("No predator, stay in your bed")

