import cv2
import numpy as np
from matplotlib import pyplot as plt

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def auto_exposure(img_path):
    # Load the image
    img = cv2.imread(img_path, 0)

    # Apply gamma correction (can be adjusted to get your desired results.)
    gamma_corrected = adjust_gamma(img, 5.0)

    # Calculate histogram for the gamma corrected image
    hist = cv2.calcHist([gamma_corrected],[0],None,[256],[0,256])

    # plot the original image in grayscale
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    # Plot the Gamma Corrected Image
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(gamma_corrected, cmap='gray')
    plt.title('Gamma Corrected Image')
    
    
    # Plot the histogram
    plt.subplot(1, 2, 2)
    plt.plot(hist)
    plt.title('Histogram')
    plt.xlabel('Pixel Values')
    plt.ylabel('Frequency')
    plt.show()

       
# Call the function with the path to your image file
auto_exposure('underexposed_image.jpg')
