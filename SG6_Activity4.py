import re

full_name = str(input("Enter your full name (First, Middle, Last):"))

name_parts = re.split(r'[, ]', full_name)

if len(full_name) >= 3:
    first_name = name_parts[0]
    mid_name = name_parts[1]
    last_name1 = name_parts[2]
    last_name2 = name_parts[3]
    
    capital_first = first_name.capitalize()
    capital_last1 = last_name1.capitalize()
    capital_last2 = last_name2.capitalize()
    
    if mid_name:
        mid_initial = mid_name[0].upper() + '.'
    else:
        mid_initial = ''
        
    formatted_name = f"{capital_last1} {capital_last2}, {capital_first}, {mid_initial}"
    
    print(f"Formatted name:", {formatted_name})