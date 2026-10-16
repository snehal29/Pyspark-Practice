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

## Another solution
from collections import Counter
lists=[1,2,1,2,4,3,16 , 16 , 30]
def find(lists):
    count = Counter(lists)
    r=[]
    print(count)
    for i , j in count.items():
        if j>1:
            r.append(i)
    return r    
print(find(lists))
