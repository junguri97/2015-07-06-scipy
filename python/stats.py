def calculate_variance(heights):
    '''
    Calculate Variance of Sample
    sample --> list, result --> variance
    '''

    mean = calculate_mean(heights)
    
    sum_diffsq = 0
    for idx in heights:
        diff = idx - mean
        diffsq = diff ** 2
        sum_diffsq = sum_diffsq + diffsq 
    variance = sum_diffsq / (len(heights)-1)    
#    print("Variance : ", variance)
    return variance

def calculate_mean(heights):
    '''
    Calculate Sample Mean
    input : list --> mean
    '''
    total = 0
    for idx in heights:
        total = total + idx
    mean = total/len(heights)    
#    print("Mean : ", total/len(heights))
    return mean
    