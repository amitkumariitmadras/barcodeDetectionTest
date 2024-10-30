# from pyzbar import pyzbar
# import cv2

# image = cv2.imread('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_0.jpg')
# barcodes = pyzbar.decode(image)
# for barcode in barcodes:
#     (x, y, w, h) = barcode.rect
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     barcodeData = barcode.data.decode('utf-8')
#     barcodeType = barcode.type
#     text = "{} ( {} )".format(barcodeData, barcodeType)
#     cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

#     print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))

# cv2.imshow("Image", image)
# cv2.waitKey(0)


import cv2
from pyzbar import pyzbar
import numpy as np

# Load the image
image = cv2.imread('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute the gradient in the x-direction
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradX = cv2.convertScaleAbs(gradX)

# Blur the gradient image
blurred = cv2.blur(gradX, (9, 9))

# Threshold the image
_, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# Apply morphological operations to close gaps between lines
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Perform erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

# Find contours in the thresholded image
contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for contour in contours:
    # Compute the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)
    # Extract the region of interest (ROI)
    roi = image[y:y+h, x:x+w]
    # Decode the barcode in the ROI
    barcodes = pyzbar.decode(roi)
    for barcode in barcodes:
        # Compute the coordinates relative to the original image
        (bx, by, bw, bh) = barcode.rect
        bx += x
        by += y
        # Draw the bounding box around the barcode
        cv2.rectangle(image, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)
        # Decode the barcode data
        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        text = "{} ( {} )".format(barcodeData, barcodeType)
        # Put the text above the barcode
        cv2.putText(image, text, (bx, by - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
        # Print the barcode type and data
        print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))

# Show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
