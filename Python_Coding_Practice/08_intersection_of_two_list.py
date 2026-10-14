'''
Write a function to get the intersection of two lists.
For example, if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3].
'''
#Solution :
def intersection(a, b):    
  result=[]        #list for result storage
  for i in a:      # loop over a list
    if i in b:      # check if the value in a is present in b or not
      result.append(i)      # if value present in b then append that value to result list
  return result

#Another solution using list comprehension 
def intersection(a, b):
    intersection_list = [value for value in a if value in b]
    return intersection_list
