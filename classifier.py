#The Emotion Face detection Scripts
#You can modify this script as you wish
import cv2
import glob as gb
import random
import numpy as np
#Emotion list
emojis = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] 
 #Initialize fisher face classifier
fisher_face = cv2.face.FisherFaceRecognizer_create()
data = {}
#Function defination to get file list, randomly shuffle it and split 67/33

def getFiles(emotion): 
    files = gb.glob("D:\\faceDetection\\FINAL\\Fera_finalCopy\\final_ dataset\\%s\\*" %emotion)

    random.shuffle(files)
    training = files[:int(len(files)*0.67)] #get first 67% of file list
    prediction = files[-int(len(files)*0.33):] #get last 33% of file list
    return training, prediction
def makeTrainingAndValidationSet():
    print ("Traing and validation set creation : Started")
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emojis:
        training, prediction = getFiles(emotion)
        
        #Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item) #open image
            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
            training_data.append(gray) #append image array to training data list
            #print (gray.shape)
            training_labels.append(emojis.index(emotion))
            
    
        for item in prediction: #repeat above process for prediction set
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emojis.index(emotion))

    return training_data, training_labels, prediction_data, prediction_labels

def runClassifier():
    training_data, training_labels, prediction_data, prediction_labels = makeTrainingAndValidationSet()
    
    print ("training fisher face classifier suing the training data")
    print ("size of training set is:", len(training_labels), "images")
    fisher_face.train(training_data, np.asarray(training_labels))
    fisher_face.save("result/result.xml")
    print ("classification prediction")
    counter = 0
    right = 0
    wrong = 0
    for image in prediction_data:
        pred, conf = fisher_face.predict(image)
        if pred == prediction_labels[counter]:
            right += 1
            counter += 1
        else:
            wrong += 1
            counter += 1
    return ((100*right)/(right + wrong))
#Now run the classifier

metascore = []
for i in range(0,3):
    right = runClassifier()
    print ("got", right, "percent right!")
    metascore.append(right)
print ("\n\nend score:", np.mean(metascore), "percent right!") 
