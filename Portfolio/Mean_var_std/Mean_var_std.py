# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:03:03 2022

@author: jindo
"""

import numpy as np

def calculate(list):
    ''' 
        Calls the function 'calc_matrix_info' on the fuction 'create_matrix' on
        the input list
      
        Args:
            list (list, int or float): 9 digits to be used to create a 3 x 3 
            matrix.

        Returns:
            dict : matrix_mean, matrix_variance, standard deviation, max, min, and sum along 
            both axes and for the flattened matrix.
    '''
    return calc_matrix_info(create_matrix(list))


def create_matrix(list):
    ''' 
        Converts the list into a 3 x 3 Numpy array
      
        Args:
            list (list, int or float): 9 digits to be used to create a 3 x 3 
            matrix.

        Returns:
            matrix : square matrix.
    '''
    # Check correct number of values are contained in the input
    len_of_input = len(list)
    if len_of_input != 9:
        raise ValueError("List must contain nine numbers.")
    int_size_of_square_matrix = 3
        
    # Alternative to the first check, checks to ensure the correct number of 
    # valueues are contained in the input, ie a square number
    # Also used to define the size of the matrix
    size_of_square_matrix = len_of_input**0.5
    int_size_of_square_matrix = int(size_of_square_matrix)
    if size_of_square_matrix != int_size_of_square_matrix:
        raise ValueError(
            'List must contain enough numbers to make a square matrix')

    # Check all values in the list are numerical values
    for value in list:
        try:
            value = float(value)
        except:
            raise TypeError('List must only contain numbers')
    
    # Initialise a blank matrix
    np_matrix = np.empty((int_size_of_square_matrix,int_size_of_square_matrix))
    
    # Initialise counters for the list, row and column position
    value_n= 0
    row = 0
    colomn = 0
    
    # Cycle through the columns to and the values populating the matrix
    while row < int_size_of_square_matrix:
        np_matrix[row, colomn] = list[value_n]
        colomn += 1
        value_n +=1
        
        # When all the columns are satisfied for that row, switch to the next
        # row  
        if colomn == int_size_of_square_matrix:
            colomn = 0
            row += 1
    return np_matrix

def calc_matrix_info(np_matrix):
    ''' 
        Calculates the mean, variance, standard deviation, max, min, and sum 
        along both axis and for the flattened matrix.
      
        Args:
            matrix : square matrix that we want to investigate

        Returns:
            dict : matrix_mean, matrix_variance, standard deviation, max, min, and sum along 
            both axes and for the flattened matrix.
    '''
    
    # Create a flat matrix to make the calculation methods the same
    flat_matrix = np.reshape(np_matrix, (1,-1))
    
    # intialise the lists of information
    matrix_mean = []
    matrix_variance = []
    matrix_standard_deviation = []
    matrix_max = []
    matrix_min = []
    matrix_sum = []

    # Define the sequence of iteration
    matrix_list = [np_matrix, np_matrix, flat_matrix] 
    ax_number = [0, 1, None]
    
    # Cycle through the axis and matricies calculating the information required
    # and appending them to the intialised lists as lists 
    for ax_no, matrix_n in zip(ax_number, matrix_list):
        matrix_mean.append(matrix_n.mean(axis = ax_no).tolist())
        matrix_variance.append(matrix_n.var(axis = ax_no).tolist())
        matrix_standard_deviation.append(matrix_n.std(axis = ax_no).tolist())
        matrix_max.append(matrix_n.max(axis = ax_no).tolist())
        matrix_min.append(matrix_n.min(axis = ax_no).tolist())
        matrix_sum.append(matrix_n.sum(axis = ax_no).tolist())

    # Define the dictionary to return using the variables created
    calculations = {'mean': matrix_mean,
    'variance': matrix_variance,
    'standard deviation': matrix_standard_deviation,
    'max': matrix_max,
    'min': matrix_min,
    'sum': matrix_sum}
    
    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))