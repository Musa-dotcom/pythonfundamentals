def linear_search_dictionary(dictionary, target_value):
    for key,value in dictionary.items(): 
        if value == target_value:
            print("Found at key", key)  
            return key
    print("Target is not in the dictionary")  
    return None

# Testing
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)