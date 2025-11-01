def find_max_number(num1, num2, num3):
    if (num1>=num2) and (num2>=num3):
     return (num1)
    elif (num1>=num3) and (num3>=num2):
      return (num1)
    elif (num2>=num3) and (num3>=num2):
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
    mean = find_mean(num1, num2, num3)
    mean = find_mean(num1, num2, num3)
    element = (num1,num2,num3)
    n_o_e = len(element)
    phase1 = ((((num1 - mean)**2) + ((num2 - mean)**2) + ((num3 - mean)**2))/n_o_e)**0.5
    return (phase1,mean)

