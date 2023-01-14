
## some general info about the project:
#### the project is for fun but after finishing it i discovered that there is a far more better ways to make Face recognition
#### -thes project recognize the following celebrities: "Kevin Hart" ,"ben_afflek" ,"dwayne_johnson" ,"elton_john" ,"jerry_seinfeld", "madonna" , "mindy_kaling", "Ryan Reynolds"
#### -i gathered the images from the internet and some from kaggle ,20 image per person in training and validation (160 in total).
#### -before this i made the same project but with 3 celebrities and 66 image per person with 93 testing accuracy so i decreased the number of training data and added more class just for fun XD
#### i built a network but at best achieved a 65% accuracy so i replaced it with vgg16 it is inside the building file anyway u can check it out
#### the model is 1.5g so i can't upload it here
# Face-Detection-and-Recognition-using-VGG16-and-openCV:
#### step 1: Face Detection and gathering trainng data: 

i used openCV cascades(haarcascade_frontalface_default.xml) to detect all the faces inside an image and crop/save the resulting image to train my model the code is show in the **photo_crop.py** file

#### step 2:processing the data and fine tuning the model to do so i used the following techniques:
- loading the data into a numpy array
- splitting it into training testing and validation
- vgg16 was designed to classify 1000 different classes so i replaced the softmax layer with a 8 output one
- at last evaluate the model and the result is 73% accuracy
**vgg16.py** file
#### 3 step:
**faceRecognition.py**
just for visualizing the results.

some test images the (input/output):

![1](https://user-images.githubusercontent.com/57813196/212487952-a423abf9-0f46-4074-900a-b733d98ec72e.png)

![2](https://user-images.githubusercontent.com/57813196/212496086-9bf0edd5-a2e5-4282-a9ad-0c7de5b9143e.png)





