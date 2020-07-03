

def simple_exp_eval(exp_string):
    """ 
    Calculates and returns expressions in string form that does not have paranthesis but may have +,-,*,/ 
    Parameters:
    exp_string (str): A mathematical expressions 

    Returns:
    float: The result
    """
    try:
        return float(exp_string)
    except:
        pass

    add = exp_string.find('+')
    sub = exp_string.find('-')

    if add!=-1:
        if add < sub or sub==-1:
            return simple_exp_eval( str( simple_exp_eval(exp_string[:add]) + simple_exp_eval(exp_string[add + 1:]) ))
    if sub!=-1:
        if sub < add or sub!=-1:
            return simple_exp_eval( str( simple_exp_eval(exp_string[:sub]) - simple_exp_eval(exp_string[sub + 1:]) ))


    mult = exp_string.find('*')
    div = exp_string.find('/')

    if mult != -1:
        if mult < div or div==-1:
            return simple_exp_eval( str( simple_exp_eval(exp_string[:mult]) * simple_exp_eval(exp_string[mult + 1:]) ))
        
    
    if div != -1:
        if div < mult or mult == -1:
            return simple_exp_eval( str( simple_exp_eval(exp_string[:div]) / simple_exp_eval(exp_string[div + 1:]) ))



def complex_eval(exp_str):
    """
    Calculates expressions which may contain (,),+,-,*,/ . Valid input is assumed.

    Parameters:
    exp_str (str): A mathematical expressions

    Returns:
    float: The result
    """
    try:
        fst_par = exp_str.index('(')
    except ValueError:
        return simple_exp_eval(exp_str)


    count = 0
    for i in range(fst_par,len(exp_str)):
        if exp_str[i] == '(':
            count+=1
        elif exp_str[i] == ')':
            count-=1
        
        if count == 0 :
            break
    return complex_eval(exp_str[:fst_par]  + str(complex_eval(exp_str[fst_par+1:i])) + exp_str[i+1:])



    

if __name__ == '__main__':
    print(type(complex_eval('(1/2)*3+((13+5 *5)/(5+5))')))
