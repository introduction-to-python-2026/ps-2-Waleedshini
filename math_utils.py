def find_max_number(num1, num2, num3):
    if (num1>=num2) and (num2>=num3):
     return (num1)
    elif (num1>=num3) and (num3>=num2):
      return (num1)
    elif (num2>=num3) and (num3>=num1):
      return(num2)
    elif (num2>=num1) and (num1>=num3):
      return(num2)
    else:
      return(num3)

def find_mean(num1, num2, num3):
    elements = (num1,num2,num3)
    phase1 = (num1+num2+num3)
    phase2 = len(elements)
    result = (phase1/phase2)
    return result

def find_mean_std(num1, num2, num3):
    # Calculate the mean once
    mean = find_mean(num1, num2, num3)
    
    # Define n directly (n=3)
    n = 3 
    
    # Calculate the sum of squared differences (numerator)
    sum_sq_diff = ((num1 - mean)**2) + ((num2 - mean)**2) + ((num3 - mean)**2)
    
    # Calculate the Standard Deviation (std_dev)
    std_dev = (sum_sq_diff / n)**0.5
    
    # Return both std_dev and mean
    return (std_dev, mean)

