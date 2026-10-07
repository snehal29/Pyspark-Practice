'''
Given a number n, write a formula that returns n!.
For example, 5!=5∗4∗3∗2∗1=120
5!=5∗4∗3∗2∗1=120 so we'd return 120.
'''
n =5        # given number
def fact(n):    # function defn
    result =1        # initilization of result variable to 1 because we need to multiple with it so atleast our result will be 1 not 0
    for i in range(1,n+1):    # looping over and range(1, n+1) as range give last number as n-1 
        result = result*i     # here do fact calculation 
    return result
    
print(f'fact:',fact(n))
