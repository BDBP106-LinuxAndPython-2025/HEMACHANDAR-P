#!usr/bin/python3

#(4) Given a dictionary with a values list, extract the key whose value has the most unique
#values.
#Input: test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
#Output:"Best"
#Explanation:3 (max) unique elements, 9,6,5 of "Best"

test_dict= {"Gfg":[5,7,7,7,7],
            "is":[6,7,7,7],
            "Best":[9,9,6,5,5]
            }

max_count = 0
key_with_max_unique =None

for k, v in test_dict.items():
    unique_values = set(v)  # Get unique elements from the list
    unique_count = len(unique_values)
    print (unique_values)
    print(unique_count)

    if unique_count > max_count:
        max_count = unique_count
        print (max_count)
        key_with_max_unique = k

print(f'{key_with_max_unique} : {unique_values}')

