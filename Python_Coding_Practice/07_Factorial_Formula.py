'''
Given a number n, write a formula that returns n!.
For example, 5!=5∗4∗3∗2∗1=120
5!=5∗4∗3∗2∗1=120 so we'd return 120.
'''
n =5
def fact(n):
    result =1
    for i in range(1,n+1):
        result = result*i
    return result
    
print(f'fact:',fact(n))
