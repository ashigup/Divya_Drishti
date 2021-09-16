# Let us import the Libraries required.
import cv2
import numpy as np
import time
# from twilio.rest import Client 
import vonage

from model import FacialExpressionModel

# Creating an instance of the class with the parameters as model and its weights.
model = FacialExpressionModel("model.json", "model_weights.h5")

# Loading the classifier from the file.
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
list_for_emotional_weight=[]
a = time.monotonic()

###################################################################################
# Sending SMS 
# SMS will be sent using twilio 
# Currently I am using my free twilio account for demo
# If you want to test it , please add your account credentials


f=1
def send_alert():
    global a
    global f
    b = time.monotonic()
    if((b-a)>15):
        f=0
        a=b
        client = vonage.Client(key="222ce96c", secret="11bYzrXnbKOi2fb7")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
               {
                  "from": "Vonage APIs",
                     "to": "917488160265",
                     "text": "Please hurry \nPatient is sad\n",
                 }
                )

        if responseData["messages"][0]["status"] == "0":
           print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


###################################################################################


class VideoCamera(object):

    """ Takes the Real time Video, Predicts the Emotion using pre-trained model. """

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        """It returns camera frames along with bounding boxes and predictions"""

        # Reading the Video and grasping the Frames
        _, frame = self.video.read()

        # Converting the Color image to Gray Scale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Image size is reduced by 30% at each image scale.
        scaleFactor = 1.3

        # 5 neighbors should be present for each rectangle to be retained.
        minNeighbors = 5

        # Detect the Faces in the given Image and store it in faces.
        faces = facec.detectMultiScale(gray_frame, scaleFactor, minNeighbors)

        # Iterating through all the faces detected
        
        for (x, y, w, h) in faces:

            # Taking the Face part in the Image as Region of Interest.
            roi = gray_frame[y:y+h, x:x+w]

            # Let us resize the Image accordingly to use pretrained model.
            roi = cv2.resize(roi, (48, 48))

            # Let us make the Prediction of Emotion present in the Image.
            prediction = model.predict_emotion(
                roi[np.newaxis, :, :, np.newaxis])

            # Custom Symbols to print with text of emotion.
            Symbols = {"Happy": ":)", "Sad": ":}", "Surprise": "!!",
                       "Angry": "?", "Disgust": "#", "Neutral": ".", "Fear": "~"}

            # Defining the Parameters for putting Text on Image
            Text = str(prediction) + Symbols[str(prediction)]
            Text_Color = (180, 105, 255)
            # print(Text)
            # print(len(list_for_emotional_weight))
            if (len(list_for_emotional_weight)<50):
                
                list_for_emotional_weight.insert(0,Text)
            else:
                list_for_emotional_weight.pop()
                list_for_emotional_weight.insert(0,Text)

                count_sad=list_for_emotional_weight.count('Sad:}') 
                if (count_sad > 10):
                    send_alert()




            Thickness = 5
            Font_Scale = 2
            Font_Type = cv2.FONT_HERSHEY_SIMPLEX

            # Inserting the Text on Image
            cv2.putText(frame, Text, (x, y), Font_Type,
                        Font_Scale, Text_Color, Thickness)

            # Finding the Coordinates and Radius of Circle
            xc = int((x + x+w)/2)
            yc = int((y + y+h)/2)
            radius = int(w/2)

            # Drawing the Circle on the Image
            cv2.circle(frame, (xc, yc), radius, (0, 255, 0), Thickness)

        # Encoding the Image into a memory buffer
        _, jpeg = cv2.imencode('.jpg', frame)

        # Returning the image as a bytes object
        return jpeg.tobytes()
