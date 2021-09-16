#  Stress Detector Investigator !



# Stress Detector Recognition Classifier Model :

Facial expression for emotion detection has always been an easy task for humans, but achieving the same task with a computer algorithm is quite challenging. With the recent advancement in computer vision and machine learning, it is possible to detect emotions from images.In this project,we propose a novel technique called Stress Detector recognition using convolutional neural networks,python and flask. Facial expressions are the vital identifiers for human feelings, because it corresponds to the emotions. Most of the times (roughly in 55% cases), the facial expression is a nonverbal way of emotional expression, and it can be considered as concrete evidence to uncover whether an individual is speaking the truth or not.

:golf: Our Stress Detector Classifier Model can take input via following ways : :point_down:
- **Real-time Video input** <br>

- **Upload Images from the System** <br>
<img width="896" alt="sad" src="https://user-images.githubusercontent.com/57671048/98131077-f103d580-1ee0-11eb-9dc3-905f3884ee1b.png"><br>
- **Provide URL of the Image** <br>
<img width="897" alt="angry" src="https://user-images.githubusercontent.com/57671048/98131265-1e508380-1ee1-11eb-92b5-12c7677c08c0.png"><br>
<img width="884" alt="happy" src="https://user-images.githubusercontent.com/57671048/98131204-10026780-1ee1-11eb-999b-0182a68ce529.png"><br>
- It predicts the **Emotion of users** and also gives **Graphical Visualization** of **Emotions** as shown above.

## :loop: Tech Stack used :point_down:
- Python
- Flask
- HTML, CSS
- Deep Learning (CNN)

## :boom: Getting Started: Steps to run the Project in your local device !!
- Clone the repository to your System using `git clone`
- Example : `git clone https://github.com/ashigup/Stress-Detector`
- Create a new [Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) with python 3.7.0 version. 
- Go in Stress-Detector folder using `cd Stress-Detector`
- Install all the dependencies with `pip install -r requirements.txt`.
- Update your twilio credentials in `camera.py` .
- Now run the `main.py` file. 
- Once it shows `Running on http://127.0.0.1:5000/` go to *http://127.0.0.1:5000/* in your browser.


## :computer: Coding Structure:

- Import the required Packages and Libraries.
- Data analysis and Creating Training and Validation Batches.
- Create a CNN using 4 Convolutional Layers including *Batch Normalization*,
*Activation*, *Max Pooling*, *Dropout* Layers followed by *Flatten* Layer, 2 Fully
*Connected dense* Layers and finally Dense Layer with *SoftMax* Activation
Function.
- Compile the model using `Adam` Optimizer and categorical cross entropy
loss function.
- Training the model for 15 epochs and then Evaluating the model as well as
saving the model Weights in `.h5` Values
- Saving the model as `JSON` string.
- Creating a Class in a separate file to reload the model and its weights to
make predictions and return the probabilities of each emotion.
- Creating one more class in a Separate file which takes in the `Real-time
Video input` and returns frames of Images with a Circle detecting the face
and putting text of its emotion on it.
- A python script is also created which upon running yields the `Graphical`
`Visualization` of Emotions present in the Image provided.
- Finally creating a file which inherits form all the Classes defined by us and
deploys our application using *Flask*.
<img src="https://miro.medium.com/max/1864/1*oURfHMP1--ttXnDx0heusg.png">

### Excited to contribute to the Project ? Head over Open Issues [here](https://github.com/ashigup)

## Project Admin :point_down:


[![](https://avatars.githubusercontent.com/u/49528910?s=400&u=2f9de0906c4fa20d9e0a4348e4c65414fc3c0147&v=4)](https://github.com/ashigup)

[Ashish Kumar](https://www.linkedin.com/in/ashish-kumar--/)





