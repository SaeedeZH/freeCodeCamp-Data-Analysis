import numpy as np

def calculate(num_list):

    if len(num_list) != 9:
        raise ValueError("List must contain 9 numbers!")
    
    # index 0: axis=0, index 1: axis=1, index 2: all elements
    stat_dic = {'mean':[],
                'variance':[],
                'standard deviation':[],
                'max':[],
                'min':[],
                'sum':[]}
    num_list = np.array(num_list)
    num_list = num_list.reshape((3,3))

    # Calculate mean
    stat_dic['mean'] = [list(num_list.mean(axis=0)), list(num_list.mean(axis=1)), num_list.mean()]   # ...mean().round(2)
    
    # Calculate variance
    stat_dic['variance'] = [list(num_list.var(axis=0)), list(num_list.var(axis=1)), num_list.var()]
    
    # Calculate standard deviation
    stat_dic['standard deviation'] = [list(num_list.std(axis=0)), list(num_list.std(axis=1)), num_list.std()]
    
    # Calculate max
    stat_dic['max']  = [list(num_list.max(axis=0)), list(num_list.max(axis=1)), num_list.max()]
    
    # Calculate min
    stat_dic['min'] = [list(num_list.min(axis=0)), list(num_list.min(axis=1)), num_list.min()]
    
    # Calculate sum
    stat_dic['sum'] = [list(num_list.sum(axis=0)), list(num_list.sum(axis=1)), num_list.sum()]
    
    ## another way:
    # calculations = {
    #     "mean": [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), float(np.mean(matrix))],
    #     "variance": [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), float(np.var(matrix))],
    #     "standard deviation": [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), float(np.std(matrix))],
    #     "max": [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), float(np.max(matrix))],
    #     "min": [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), float(np.min(matrix))],
    #     "sum": [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), float(np.sum(matrix))],
    # }
    return stat_dic

print(calculate([2,6,2,8,4,0,1,5,7]))