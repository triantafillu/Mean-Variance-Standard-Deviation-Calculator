import numpy as np

def calculate(list):
    #Check whether the matrix is 3x3
    if len(list)!=9:
      raise ValueError( "List must contain nine numbers.")

    #Transform list to matrix
    matrix = np.array(list).reshape((3,3))

    #First column (array of first element of each row)
    ax1_1=np.array([matrix[0, 0], matrix[1,0], matrix[2,0]])
    #Second column
    ax1_2=np.array([matrix[0, 1], matrix[1,1], matrix[2,1]])
    #Third column
    ax1_3=np.array([matrix[0, 2], matrix[1,2], matrix[2,2]])

    #First row
    ax2_1=matrix[0].copy()
    #Second row
    ax2_2=matrix[1].copy()
    #Third row
    ax2_3=matrix[2].copy()

    #For each row, column and for full matrix calculate mean, variance, standard deviaton
    calculations = {'mean': [[np.mean(ax1_1), np.mean(ax1_2), np.mean(ax1_3)],
                            [np.mean(ax2_1), np.mean(ax2_2), np.mean(ax2_3)],
                            np.mean(matrix.ravel())],
                    'variance': [[np.var(ax1_1), np.var(ax1_2), np.var(ax1_3)],
                            [np.var(ax2_1), np.var(ax2_2), np.var(ax2_3)],
                            np.var(matrix.ravel())],
                    'standard deviation': [[np.std(ax1_1), np.std(ax1_2), np.std(ax1_3)],
                            [np.std(ax2_1), np.std(ax2_2), np.std(ax2_3)],
                            np.std(matrix.ravel())],
                    'max': [[np.max(ax1_1), np.max(ax1_2), np.max(ax1_3)],
                            [np.max(ax2_1), np.max(ax2_2), np.max(ax2_3)],
                            np.max(matrix.ravel())],
                    'min': [[np.min(ax1_1), np.min(ax1_2), np.min(ax1_3)],
                            [np.min(ax2_1), np.min(ax2_2), np.min(ax2_3)],
                            np.min(matrix.ravel())],
                    'sum': [[np.sum(ax1_1), np.sum(ax1_2), np.sum(ax1_3)],
                            [np.sum(ax2_1), np.sum(ax2_2), np.sum(ax2_3)],
                            np.sum(matrix.ravel())]}


    return calculations