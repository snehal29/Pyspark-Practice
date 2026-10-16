'''
Find the duplicates items in the list and return the list with those
'''
lists=[1,2,1,2,4,3]

def find(lists):
    seen=set()
    duplicate=set()
    for i in lists:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    return (list(duplicate))
    
print(find(lists))
