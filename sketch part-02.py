import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_to_sketch(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    
    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)
    
    # Create the pencil sketch by dividing the grayscale image by the blurred inverted image
    sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256)
    
    # Display the original image and the sketch side by side
    plt.figure(figsize=(12, 6))
    
    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert to RGB for correct display
    plt.title('Original Image')
    plt.axis('off')
    
    # Plot the sketch
    plt.subplot(1, 2, 2)
    plt.imshow(sketch, cmap='gray')
    plt.title('Pencil Sketch')
    plt.axis('off')
    
    plt.show()

    return sketch

# Provide the path to your image
image_path = input("Enter the path of the image that you want to sketch: ")
# Call the function to convert the image to a sketch
sketch_image = image_to_sketch(image_path)

# Optionally save the sketch image
cv2.imwrite('sketch_image.jpg', sketch_image)
