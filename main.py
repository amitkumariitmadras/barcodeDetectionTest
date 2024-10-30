# import pyzbar

# # print(pyzbar.__version__)

# from PIL import Image
# from pyzbar.pyzbar import decode, ZBarSymbol

# img = Image.open('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_0.jpg')

# decoded_list = decode(img)

# print(type(decoded_list))
# # <class 'list'>

# print(len(decoded_list))

# print(type(decoded_list))

# print(decoded_list[0].type)

# print(decoded_list[0].data.decode())

# print(decoded_list[0].rect)
# print(decoded_list[0].polygon)


# from PIL import Image, ImageDraw, ImageFont
# from pyzbar.pyzbar import decode

# # img = Image.open('data/src/barcode_qrcode.jpg')
# img = Image.open('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')


# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('Arial.ttf', size=20)  # Set 'arial.ttf' for Windows

# for d in decode(img):
#     draw.rectangle(((d.rect.left, d.rect.top), (d.rect.left + d.rect.width, d.rect.top + d.rect.height)),
#                    outline=(0, 0, 255), width=3)
#     draw.polygon(d.polygon, outline=(0, 255, 0), width=3)
#     draw.text((d.rect.left, d.rect.top + d.rect.height), d.data.decode(),
#               (255, 0, 0), font=font)

# img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/resultPillow140.jpg')


# from PIL import Image, ImageDraw, ImageFont, ImageEnhance
# from pyzbar.pyzbar import decode


# from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
# from pyzbar.pyzbar import decode


# # Load and preprocess the image
# img = Image.open('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')

# # Convert image to grayscale
# img = img.convert('L')

# # Enhance contrast
# enhancer = ImageEnhance.Contrast(img)
# img = enhancer.enhance(2.5)  # Increase contrast further

# # Enhance brightness
# brightness_enhancer = ImageEnhance.Brightness(img)
# img = brightness_enhancer.enhance(1.5)  # Increase brightness

# # Apply sharpen filter
# img = img.filter(ImageFilter.SHARPEN)

# # Apply adaptive thresholding (convert to binary image)
# img = img.point(lambda p: p > 128 and 255)  # Thresholding to make it binary

# # Detect and annotate the barcode
# draw = ImageDraw.Draw(img)
# font = ImageFont.load_default()  # Load default font

# # Loop through detected barcodes
# for d in decode(img):
#     # Draw rectangle around barcode (use single int for grayscale color)
#     draw.rectangle(((d.rect.left, d.rect.top), (d.rect.left + d.rect.width, d.rect.top + d.rect.height)),
#                    outline=255, width=3)  # 255 is white in grayscale mode
#     # Draw the barcode text below the detected area
#     draw.text((d.rect.left, d.rect.top + d.rect.height), d.data.decode(),
#               255, font=font)  # Text in white color (255)

# # Save the annotated image
# img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/resultPillow140b.jpg')



# worked for 140

# from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
# from pyzbar.pyzbar import decode

# # Load the image
# img = Image.open('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')


# # Preprocess the image
# img = img.convert('L')  # Convert to grayscale
# enhancer = ImageEnhance.Contrast(img)
# img = enhancer.enhance(2.5)  # Increase contrast
# brightness_enhancer = ImageEnhance.Brightness(img)
# img = brightness_enhancer.enhance(1.5)  # Increase brightness
# img = img.filter(ImageFilter.SHARPEN)  # Sharpen the image
# img = img.point(lambda p: p > 128 and 255)  # Thresholding for binary conversion

# # Prepare to annotate the image
# draw = ImageDraw.Draw(img)
# font = ImageFont.load_default()  # Load default font

# # Try detecting the barcode at different angles
# detected = False
# for angle in range(0, 360, 15):  # Rotate from 0 to 345 degrees in 15-degree steps
#     rotated_img = img.rotate(angle, expand=True)
#     barcodes = decode(rotated_img)
    
#     if barcodes:
#         detected = True
#         for d in barcodes:
#             # Print the decoded barcode text to console
#             barcode_text = d.data.decode()
#             print("Detected barcode text:", barcode_text)

#             # Draw rectangle around barcode on the rotated image
#             draw.rectangle(((d.rect.left, d.rect.top), 
#                             (d.rect.left + d.rect.width, d.rect.top + d.rect.height)),
#                            outline=255, width=3)  # White outline in grayscale mode
            
#             # Draw the barcode data text below the detected area
#             draw.text((d.rect.left, d.rect.top + d.rect.height), d.data.decode(),
#                       255, font=font)  # Text in white color (255)
        
#         # Stop if barcode is detected in any rotation
#         break

# # Save the result
# if detected:
#     img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/resultPillow140d.jpg')
# else:
#     print("Barcode not detected at any rotation angle.")

# # Save the annotated image
# img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/resultPillow140a.jpg')



from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from pyzbar.pyzbar import decode

# Load the image
img = Image.open('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')

# Preprocess the image
img = img.convert('L')  # Convert to grayscale
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2.5)  # Increase contrast
brightness_enhancer = ImageEnhance.Brightness(img)
img = brightness_enhancer.enhance(1.5)  # Increase brightness
img = img.filter(ImageFilter.SHARPEN)  # Sharpen the image
img = img.point(lambda p: p > 128 and 255)  # Thresholding for binary conversion

img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/PresultPillow140e.jpg')

# Prepare to annotate the image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Load default font

# Variable to keep track of the top-most barcode
top_barcode = None

# Try detecting the barcode at different angles
for angle in range(0, 360, 15):  # Rotate from 0 to 345 degrees in 15-degree steps
    rotated_img = img.rotate(angle, expand=True)
    barcodes = decode(rotated_img)
    
    if barcodes:
        for d in barcodes:
            # Check if this barcode is higher in the image (closer to the top)
            if top_barcode is None or d.rect.top < top_barcode.rect.top:
                top_barcode = d

        # Stop further rotation if we find a barcode
        if top_barcode:
            break

# If a barcode was found, annotate and print its information
if top_barcode:
    barcode_text = top_barcode.data.decode()
    print("Detected top-most barcode text:", barcode_text)

    # Draw rectangle around the top-most barcode
    draw.rectangle(((top_barcode.rect.left, top_barcode.rect.top), 
                    (top_barcode.rect.left + top_barcode.rect.width, top_barcode.rect.top + top_barcode.rect.height)),
                   outline=255, width=3)  # White outline in grayscale mode
    
    # Draw the barcode data text below the detected area
    draw.text((top_barcode.rect.left, top_barcode.rect.top + top_barcode.rect.height), 
              barcode_text, 255, font=font)  # Text in white color (255)
    
    # Save the result
    img.save('/Users/amit/Desktop/GoodMove/barcodeDetection/resultPillow0e.jpg')
else:
    print("No barcode detected or unable to determine top-most barcode.")



# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# # img = cv2.imread('data/src/barcode_qrcode.jpg')
# img = cv2.imread('/Users/amit/Desktop/GoodMove/barcodeDetection/bucketFinal_140.jpg')


# for d in decode(img):
#     img = cv2.rectangle(img, (d.rect.left, d.rect.top),
#                         (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (255, 0, 0), 2)
#     img = cv2.polylines(img, [np.array(d.polygon)], True, (0, 255, 0), 2)
#     img = cv2.putText(img, d.data.decode(), (d.rect.left, d.rect.top + d.rect.height),
#                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)

# cv2.imwrite('/Users/amit/Desktop/GoodMove/barcodeDetection/result140.jpg', img)