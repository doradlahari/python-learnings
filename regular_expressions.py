import re

# ^ - strating of re
# $ - ending of re
# \d - digits
# \w - alphanumeric
# {} - specifying the length.

# format

# 646 748-8484

format_str = r'\d{3} \d{3}-\d{4}' # if string starts with r then only it will consider as regular expression..

str_data = " Please use 733 738-8383 number to contact me."

# str_data = "you can contact me at 764 848-8494"

# str_data = "339 848-8484 this is my mobile number."

# match -- match will search for the format only at the starting of the string only..
# search -- search will perform the operation at any location inside the string..
# findall

# match1 = re.match(format_str,str_data)

# print(match1)


# str_data = " Please use 733 738-8383 number646 474-7484 to contact me."

# match1 = re.search(format_str,str_data)

# print(match1)


# str_data = " Please use 733 738-8383 number646 474-7484 to contact me."

# match1 = re.findall(format_str,str_data)

# print(match1)