def matrix_from_xls(file_w_path,column,xcycle,skip):
    """Reads csv file and produces 2-D matrix
    """
    import numpy as np
    
    data_tmp = np.array(np.genfromtxt(file_w_path, delimiter=',',skip_header=1)) # Read csv file
    data_yr_tmp = data_tmp[:,column]
    numdat = len(data_yr_tmp)
#    data_yr = data_yr_tmp[skip:-(xcycle-skip+numdat%xcycle)] # start at skip
    data_yr = data_yr_tmp[skip:-((numdat-skip)%xcycle)] # start at skip + 1 and go as close to end of data as possible
    data_2D = np.reshape(np.array(data_yr), (-1,xcycle)) #2D matrix of data in numpy format
    
    print 'whole eqn ', xcycle-skip+numdat%xcycle 
    print 'xcycle ',xcycle
    print 'skip ',skip
    print 'numdat ',numdat
    print 'numdat%xcycle ', numdat%xcycle
    
    
    return data_2D
