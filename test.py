# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 21:49:56 2014

@author: haggertr
"""

from matrix_from_xls import matrix_from_xls as mfx

file = 'C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\Cascade_plots\\save tmp\\testdata.xls'

a = mfx(file,1,24,3,filetype='xls')

b=a

print b