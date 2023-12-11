# Program to ask user for user's name, and 3 LAB NUMBERS.
# Program will take the first 9 characters of these lab numbers and check if these LAB NUMBERS MATCH.

from datetime import datetime

user_name = input("Enter your name: ")
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
str_value1 = input("Enter First barcode to check: ")
str_value2 = input("Enter Second barcode to check: ")
str_value3 = input("Enter Third barcode to check: ")

str_value1_char9 = str_value1[0:9]
str_value2_char9 = str_value2[0:9]
str_value3_char9 = str_value3[0:9]

if str_value1_char9 == str_value2_char9 and\
        str_value1_char9 == str_value3_char9 and\
        str_value2_char9 == str_value3_char9:
    comparison_match = "MATCH"
else:
    comparison_match = "MISMATCH"

# Future audit log required, printing variables for the time being.
print(user_name)
print(current_datetime)
print(str_value1_char9, ", ", str_value2_char9, ", ", str_value3_char9)
print(comparison_match)
