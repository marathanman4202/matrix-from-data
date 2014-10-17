# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 21:49:56 2014

@author: haggertr
"""

from matrix_from_xls import matrix_from_xls as mfx

#file = 'C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\Cascade_plots\\save tmp\\testdata.xls'
#file = 'C:\\code\\matrix-from-data\\testdata.xls'
file = '1e__IjqMLBBVLqBHWZiIORkPbz6W8PQlSPVeodQBM8Oc'  #google key

a = mfx(file,1,24,7,filetype='gsheet')

b=a

print b