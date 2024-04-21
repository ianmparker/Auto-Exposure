# Auto-Exposure
Simple Auto Exposure project in Python
My LinkedIn: https://www.linkedin.com/in/ian-parker-596011142/
--------------------------------------

# Overview

As a part of my overarching basketball event detection project (https://github.com/ianmparker/basket-event-detection) , I ran into issues when capturing footage outdoors. 

It's hard to get ideal lightning conditions for data collection when it is an especially sunny day, overcast, sunset etc...

In order to impove image quality I've developed a simple auto exposure project that uses gamma correction. 

It can be used to take any image that is underexposed or overexposed and use gamma correction to make the image easier to view. 

This will be key when running an image though a trained model, as it will be easier for the model to detect objects, poses, and events. 


--------------------------------------

# Sample Input 

![underexposed_image](https://github.com/ianmparker/Auto-Exposure/assets/18231849/9696eb86-49bc-496a-8c38-ab6028fa4852)

--------------------------------------

# Sample Output

![image](https://github.com/ianmparker/Auto-Exposure/assets/18231849/fcc45dc3-6921-4af6-bc3c-0e051b2ac309)


--------------------------------------

# Next Steps

As I progress in development and expand to real-time event detection in the field, the ability to calibrate the auto exposure in real-time will be crucial. 

There are many other auto-exposure techniques used in image processing in additon to gama correction such as: 
  - Histogram Equalization
  - Reinforcement Learning using a Markov Decision making Process
  - Adaptive Metering

As I continue to explore these topics and get a better understaing of the challanges and constraints of real time basketball event detection I will likely use one of these methods. 

--------------------------------------

# References: 

  - basket-event-detection: https://github.com/ianmparker/basket-event-detection
  - Personalized Exposure Control Using Adaptive Metering and Reinforcement Learning: https://ar5iv.labs.arxiv.org/html/1803.02269
  - histograms: https://github.com/ianmparker/Histograms
