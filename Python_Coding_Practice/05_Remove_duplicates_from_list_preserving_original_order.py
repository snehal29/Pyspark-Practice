
# Write a Python program to remove duplicate customer IDs while preserving the original order.
customer_ids = [101, 102, 103, 101, 104, 102, 105, 103]
def remove_dup(lists):
    result =[]
    seen=set()
    
    for i in lists:
        if i not in seen:
            result.append(i)
            seen.add(i) 
    return result
    
print(remove_dup(customer_ids))
                
