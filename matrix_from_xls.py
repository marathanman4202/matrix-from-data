def matrix_from_xls(file_w_path,column,xcycle,skip,filetype='csv'):
    """Reads csv file and produces 2-D matrix
    """
    import numpy as np
    import xlrd

    if filetype == 'csv':
        data_tmp = np.array(np.genfromtxt(file_w_path, delimiter=',',skip_header=1)) # Read csv file
        data_yr_tmp = data_tmp[:,column]
    elif filetype == 'xls':
        workbook = xlrd.open_workbook(file_w_path)
        # get 0th sheet, column, starting at 1st fow
        sheetnum = 0
        rowstart = 1
        data_yr_tmp = np.array(workbook.sheet_by_index(sheetnum).col_values(column)[rowstart:])

    numdat = len(data_yr_tmp)
#    data_yr = data_yr_tmp[skip:-(xcycle-skip+numdat%xcycle)] # start at skip
    data_yr = data_yr_tmp[skip:-((numdat-skip)%xcycle)] # start at skip + 1 and go as close to end of data as possible
    data_2D = np.reshape(np.array(data_yr), (-1,xcycle)) #2D matrix of data in numpy format
    
    
    return data_2D
