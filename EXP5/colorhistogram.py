
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("flower.jpg")

if img is None:
    print("Error: Image not found")
else:
    # Define colors and channel names
    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    # Plot the histogram for each color channel
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=names[i])

    # Set graph details
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.xlim([0, 256])

    # Display the histogram
    plt.show()

    print("Color Histogram Analysis completed successfully")
