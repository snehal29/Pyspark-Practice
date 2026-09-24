'''
Write the python program for list flattering
input =[1,[2,3,[4,5],6[
output =[1,2,3,4,5,6]
'''
input1=[1,[2,3],[4,5],[6,7]]

def flat(input1): # function defination
    output=[]       # new list for output storage 
    for i in input1: # looping over list 
        if isinstance(i,list): # checking in list is item i presnt and make list output it
            output.extend(flat(i)) # extend the list and add i item to the output list and call flat function again and again 
        else:
            output.append(i) # if not then append the i item at the end of list 
            
    return output # return the output
    
print(flat(input1)) # call flat and print the output
