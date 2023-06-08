# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:48:24 2023

@author: stein
"""

import scipy
import numpy as np

def simple_math(x):
    a = np.arange(x)
    data={"array":a}
    scipy.io.savemat('test_true_ans.mat',data)

#print("True test working")