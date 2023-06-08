# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

On my machine, I am using a virtual environment with python 3.9, as my Matlab Version is 2022a.

2P machine also has matlab 2022a, so this script would work.

Mesmerize is compatiable with python 3.9
"""
#import packages:  **Note! import the packages in the called notebooks themselves!**




#This all worked!! 

#Enter Mode:
mode=11
    
true_test_var=True
'''
#This was totally not needed:
if true_test==True:
    get_ipython().run_line_magic('run','-i -t true_test.py','mode')
else:
    get_ipython().run_line_magic('run','-i -t false_test.py')

'''

import true_test   #here is how to call the scripts that I have made.
ans=true_test.simple_math(mode)


"""
Now I just need to write this so that I can call maskRCNN or mesmerize. 

For mesmerize I am gong to need to make sure the enviornment is set up right on the computer. 

I think MaskRCNN also needs caiman, so I should follow the steps for installing mesmerize. 

"""


