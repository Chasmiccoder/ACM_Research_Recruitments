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
#img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# Converting the image read to a numpy array
img = np.array( image )

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

for i in unique_colours:
    #if (i[0] > 13 and i[0] < 17) and ( i[1] > 25 and i[1] < 29 ) and ( i[2] > 110 and i[2] < 114 ):
    print( i )


cv2.imwrite('opncv_sample.png', img)  












