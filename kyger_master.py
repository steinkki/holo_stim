# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:05:09 2023

@author: stein

Version 1 of the engram Master program.

This program will be called from the find_phasor_regions matlab notebook. 
This contains multiple different pipelines that the user can set

Run this script first! 


Need to figure out how to pass the image to this code. 
- I think that the easiest will be to actually save the image as a .tiff file
- Then use this notebook to call the one we want, and combine


Should have a text file output that tells us about the experiment. 

"""


"""
Enter user variables below:
    mode_ : Set to True if you want Kyger to analyze using this method.

"""

print("Running Kyger Master.")

#Enter modes to use:
mode_mesmerize=False     
mode_maskRCNN=False
mode_random=True

#File location:

print("Reading File Input...")
    
file_read="random_image.tif"

print("Done")

"""
Execute Random ROI mode:
"""
num_circles="10"

import os

if mode_random==True:
    print("Executing Kyger Random ROI generation...")
    variable = file_read
    os.environ["File_Location"] = variable    #sets the file location that random can use
    os.environ["Num_ROI"]=num_circles
    os.system("kyger_random.py")    #calls the kyger_random file


"""
Execute Mesmerize Mode:
    
NOTE! Mesmerize must be run in a mesmerize compatible enviornment, and in python 3.9 to be compatible with Matlab. 

"""

if mode_mesmerize==True:
    print("Executing Kyger Mesmerize ROI detection...")
    variable = file_read
    os.environ["File_Location"] = variable    #sets the file location that random can use


"""
Execute MaskRCNN Mode:

NOTE! Mesmerize must be run in a mesmerize compatible enviornment, and in python 3.9 to be compatible with Matlab.

"""
if mode_maskRCNN==True:
    print("Executing Kyger MaskRCNN ROI detection...")
    variable = file_read
    os.environ["File_Location"] = variable    #sets the file location that random can use


"""
Recall outputs from notebooks:
    
- First try to set os.environ[] variables. 
- second try saving each mode as the same file name so that you need less code here.
- This is where I might have the alignment from Matlab happen. 

"""
if mode_random==True:
    contours=os.environ["random_contours"]   #import contours
if mode_mesmerize==True:
    contours=os.environ["random_contours"]   #import contours
if mode_maskRCNN==True:    
    contours=os.environ["random_contours"]   #import contours

"""
Print Metadata to a text file. 

"""


