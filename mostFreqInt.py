def mostFreqInt(my_list):
    d = dict()
    for val in my_list:
        key = str(val)
        if key in d:
            d[str(val)] += 1
        else:
            d[str(val)] = 1
    max_val = -1
    max_key = None
    for key,freq in d.items():
        if freq>max_val:
            max_val = freq
            max_key = key
    return int(key)

        
    
print(mostFreqInt([1,2,3,2,2,2,1,1,3,2,2,2]))