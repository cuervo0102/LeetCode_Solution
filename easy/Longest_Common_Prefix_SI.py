#Amazon

my_list = ["flower", "flow", "flight"]

def find_longest_common_prefix(my_list):
    if not my_list:
        return ""  

    shortest_string = min(my_list, key=len)
    
    for i, char in enumerate(shortest_string):
        for word in my_list:
            if word[i] != char:
                return shortest_string[:i]

    return shortest_string  
result = find_longest_common_prefix(my_list)
print(result)
