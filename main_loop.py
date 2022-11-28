# main_loop structure
# called by gui with email and image folder
# calls detector
# calls recognition
# calls email_sender

from utils_cv.email_sender import send_alert
from utils_cv.recognition import recognition
from utils_cv.detector.utilitary import max_ls
import os
from utils_cv.detector.detect_with_classifier import object_detector

"""used to run the code with gpu acceleration"""
# import ctypes
# cublas = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cublas64_11.dll")
# cublaslt = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cublasLt64_11.dll")
# cufft = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cufft64_10.dll")
# curand = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\curand64_10.dll")
# cusolver = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cusolver64_11.dll")
# cusparse = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cusparse64_11.dll")
# cudnn_infer = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cudnn_cnn_infer64_8.dll")
# cudnn_ops_train = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cudnn_ops_train64_8.dll")
# cudnn_cnn_train = ctypes.WinDLL("C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.2\\bin\\cudnn_cnn_train64_8.dll")

def structure(email, filepath, precision_target=0.8):
    """Runs the detection algorithm and handles the different outputs by either doing nothing or sending an email

    Parameters
    ----------
    email: string
        address to send the email to

    file_path: string
        path of the folder in which to scan the images

    precision_target (opt): float
        confidence level on predator recognition

    Returns
    -------
    Nothing
        Sends an email if a predator is detected in one of the images"""

    #filepath = absolut_path(filepath)

    for file in os.listdir(filepath): # going over all submited images to find predators
        image_detected=object_detector(filepath+"/"+file)
        if len(image_detected)==0:
            print("No image detected")
        else:
            ls_proba=[]
            ls_animal=[]
            for img in image_detected:
                detection_result = recognition(img)
                if detection_result=="No predator, stay in your bed":
                    pass # placeholder
                else:
                    proba,animal = detection_result
                    ls_proba.append(proba)
                    ls_animal.append(animal)
            if len(ls_proba)!=0:
                maximum,indice = max_ls(ls_proba)
                print("email envoyé")
                send_alert(email,ls_animal[indice],filepath+"/"+file)
            else :
                print("pas d'animaux ")
        os.rename(filepath + "/" + file,filepath + "/" + "$"+file)
    print("no more photos")

    for file in os.listdir(filepath):
        if file[0]=="$":
            if (file[-3],file[-2],file[-1])==("j","p","g" )or (file[-3],file[-2],file[-1])==("p","n","g"):
                os.remove(filepath +"/"+file)

