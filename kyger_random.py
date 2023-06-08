# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:22:24 2023

@author: stein

Generate Random ROI's

"""
#Test variables
file_loc="random_image.tif"
num_circles=10



#Trying without having to write a function first


#Import the file location:
import os
#file_loc = os.environ["File_Location"]  
#num_circles=os.environ["Num_ROI"]


from PIL import Image, ImageDraw

# Open the TIFF file
image = Image.open(file_loc)

# Display some information about the image
print("Image format:", image.format)
print("Image mode:", image.mode)
print("Image size:", image.size)

#Draw some random circles on the image:
    
import random


def draw_random_circles(image, num_circles):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    circle_centers = []

    for _ in range(num_circles):
        radius = random.randint(10, 50)
        x = random.randint(radius, width - radius)
        y = random.randint(radius, height - radius)
        circle_centers = (x, y)

        # Check if the new circle overlaps with existing circles
        overlapping = any(
            ((x - center_x) ** 2 + (y - center_y) ** 2) <= (radius + existing_radius) ** 2
            for (center_x, center_y, existing_radius) in circle_centers
        )

        if not overlapping:
            draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill="red")
            circle_centers.append((x, y, radius))

    return circle_centers

# Draw random circles on the image
circle_locations = draw_random_circles(image, num_circles)

# Display the image with circles
image.show()

# Save the modified image as a new TIFF file
from datetime import datetime
current_datetime = datetime.now()  # Get the current date and time
datetime_string = current_datetime.strftime("%Y%m%d_%H%M%S")  # Convert the datetime object to a string
#print("Current date and time:", datetime_string)
save_name="random_ROI_"+datetime_string+".tif"   #name of the file
image.save(save_name)

#save the contours:
#try making a new variable:
os.environ["random_contours"]=circle_locations


# Close the image
image.close()

# Print the circle locations
for x, y, radius in circle_locations:
    print("Circle at ({}, {}) with radius {}".format(x, y, radius))
    
    
    
print("Kyger Random ROI Generation complete.")
