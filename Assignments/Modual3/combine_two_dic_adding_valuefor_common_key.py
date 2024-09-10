d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400} 

combine_dict={}

# Add all key-value pairs from the first dictionary

for key in d1:
    combine_dict[key]=d1[key]

# Add all key-value pairs from the second dictionary
# If the key already exists in the combined_dict, add the values

for key in d2:
    if key in combine_dict:
        combine_dict[key] += d2[key]
    else:
        combine_dict[key]=d2[key]

print("Combine two dictionary adding value for common keys : ",combine_dict)