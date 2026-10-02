#Write a Python function to count how many times each customer ID appears.
customer_ids = [101, 102, 101, 103, 102, 104, 103] 

def counts(lists):        # define function
    result={}             # declare the empty dic 
    for i in lists:        # loop over list
        if i in result:    # check if current i is present in result or not
            result[i]=result[i]+1    # if i present in result then increase counter by 1
        else:                        # if i is not present in result then initilize the i to 1
            result[i]=1
    return result                    # return the result
print(counts(customer_ids))           # call function and print the returned result


'''
Another approach using counter function 

from collections import Counter

result = Counter(customer_ids)
print(result)
'''
