#Write a Python function to count how many times each customer ID appears.
customer_ids = [101, 102, 101, 103, 102, 104, 103] 

def counts(lists):
    result={} 
    for i in lists:
        if i in result:
            result[i]=result[i]+1
        else:
            result[i]=1
    return result
print(counts(customer_ids))
