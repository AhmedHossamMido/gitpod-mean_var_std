import numpy as np

def calculate(list):

    # If a list containing less than 9 elements is passed into the function, 
    # it should raise a ValueError exception with the message: "List must contain nine numbers."
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    #The function should convert the list into a 3 x 3 Numpy array
    nparr = np.reshape(np.array(list),(3,3))

    mean_axis1 = nparr.mean(axis = 0).tolist()
    mean_axis2 = nparr.mean(axis = 1).tolist()
    mean_flattened = nparr.mean().tolist()
    mean = [mean_axis1, mean_axis2, mean_flattened]

    variance_axis1 = nparr.var(axis = 0).tolist()
    variance_axis2 = nparr.var(axis = 1).tolist()
    variance_flattened = nparr.var().tolist()
    variance = [variance_axis1, variance_axis2, variance_flattened]

    standard_deviation_axis1 = nparr.std(axis = 0).tolist()
    standard_deviation_axis2 = nparr.std(axis = 1).tolist()
    standard_deviation_flattened = nparr.std().tolist()
    standard_deviation = [standard_deviation_axis1, standard_deviation_axis2, standard_deviation_flattened]

    max_axis1 = nparr.max(axis = 0).tolist()
    max_axis2 = nparr.max(axis = 1).tolist()
    max_flattened = nparr.max().tolist()
    maximum = [max_axis1, max_axis2, max_flattened]

    min_axis1 = nparr.min(axis = 0).tolist()
    min_axis2 = nparr.min(axis = 1).tolist()
    min_flattened = nparr.min().tolist()
    minimum = [min_axis1, min_axis2, min_flattened]

    sum_axis1 = nparr.sum(axis = 0).tolist()
    sum_axis2 = nparr.sum(axis = 1).tolist()
    sum_flattened = nparr.sum().tolist()
    summation = [sum_axis1, sum_axis2, sum_flattened]

    """
    The returned dictionary should follow this format:

    {
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
    }
    """

    dictionary = {
                'mean': mean,
                'variance': variance,
                'standard deviation': standard_deviation,
                'max': maximum,
                'min': minimum,
                'sum': summation       
                }

    return dictionary 
