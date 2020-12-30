"""
Computer Vision Task - 
We need to superimpose Image_1.png on top of Image_2.png after removing the white colour and
blue background in Image_1
"""

from PIL import Image
from numpy import asarray
import numpy as np
import cv2
 
"""
img = Image.open( "Image_1.png" )

image_as_array = asarray( img )

print( "Datatype of the image extracted as an array: ", type( image_as_array ) )
print( "Shape of the image: ", image_as_array.shape )
print( "Image as the array:\n", image_as_array )

# Creating Pillow image from our numpyarray 
pilImage = Image.fromarray( image_as_array ) 
print(type(pilImage)) 
  
# Let us check  image details 
print(pilImage.mode) 
print(pilImage.size)
"""

# Reading the image using Opencv
image = cv2.imread('Image_1.png') 
  
# BGR -> RGB 
# we receive colours in GBR format
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# Converting the image read to a numpy array
img = np.array( img )


unique_colours = [ ]

# Obtaining all the unique colours:
for i in img:
    for j in i:
        k = j.tolist( )
        if k not in unique_colours:
            unique_colours.append( k )

print( "Number of Unique Colours: ", len(unique_colours) )
#print( "Unique Colours:\n", unique_colours )

"""
Now we need to find the RGB Code of the blue background:
Open the image using MSPaint
Use the 'select colour' tool
Click on edit colours
The RGB Code will appear at the side :P

RGB ( 15, 27, 112 ) for the blue background.
"""

# This segment of the code removes the blue background and converts all
# pixels with background colour to white pixels
bg = [15,27,112]
for i in range(len(img)):
    
    for pixel_index in range( len(img[i]) ):
        pixel = img[i][pixel_index]
        temp = pixel.tolist( )
        if temp == bg:
            pixel = np.array( [255,255,255] )
            img[i][pixel_index] = pixel


# Importing Image_2
image_2 = cv2.imread('Image_2.jpg')
img_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)
img_2 = np.array( image_2 )

# Comparing the shapes of these two images:
print( "Shape of Image 1: ", img.shape )     # (1134, 1137, 3)
print( "Shape of Image 2: ", img_2.shape )   # (498,  883,  3)
  
# Resizing img 1, since its resolution is bigger than necessary
img = np.array( cv2.resize(img, (883,498), interpolation = cv2.INTER_NEAREST) ) 

# Comparing the shapes of these two images again:
print( "Shape of Image 1: ", img.shape )     # (498,  883,  3)
print( "Shape of Image 2: ", img_2.shape )   # (498,  883,  3)

"""
for i in range( len(img_2) ):
    for pixel_index in range( len(img_2[i]) ):

        pixel = img_2[i][pixel_index]

        i
"""






cv2.imwrite('opncv_sample.png', img)  

print("Process Complete!")












