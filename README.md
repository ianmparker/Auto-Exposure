# Auto-Exposure Calibration: A Python Implementation


My LinkedIn: https://www.linkedin.com/in/ian-parker-596011142/
--------------------------------------

# Overview

This project is an integral component of a larger initiative aimed at detecting basketball events (available at Basketball Event Detection). The primary challenge encountered during the data collection phase was the variability in outdoor lighting conditions, which could range from bright sunlight to overcast skies or even sunset.

To mitigate these issues and enhance image quality, I have developed an auto-exposure calibration project that employs gamma correction. This technique can be applied to any underexposed or overexposed image to adjust its exposure, thereby making it more visually discernible.

The application of this project is significant when processing an image through a trained model, as it facilitates the model’s ability to detect objects, poses, and events.


--------------------------------------

# Sample Input 

![underexposed_image](https://github.com/ianmparker/Auto-Exposure/assets/18231849/9696eb86-49bc-496a-8c38-ab6028fa4852)

--------------------------------------

# Sample Output

![image](https://github.com/ianmparker/Auto-Exposure/assets/18231849/fcc45dc3-6921-4af6-bc3c-0e051b2ac309)


--------------------------------------

# Next Steps

As the project evolves towards real-time event detection in the field, the capacity to calibrate auto-exposure in real-time will become increasingly critical.

There exist numerous auto-exposure techniques in the realm of image processing, beyond gamma correction, such as:

  - Histogram Equalization
  - Reinforcement Learning using a Markov Decision Process
  - Adaptive Metering
    
As I delve deeper into these topics and gain a more comprehensive understanding of the challenges and constraints associated with real-time basketball event detection, I anticipate incorporating one of these methods into my project.

--------------------------------------

# References: 

  - basket-event-detection: https://github.com/ianmparker/basket-event-detection
  - Personalized Exposure Control Using Adaptive Metering and Reinforcement Learning: https://ar5iv.labs.arxiv.org/html/1803.02269
  - histograms: https://github.com/ianmparker/Histograms
