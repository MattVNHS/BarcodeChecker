# Program to ask user for user's name, and 2 barcodes. Program will check if these barcode match.

from datetime import datetime

user_name = input("Enter your name: ")
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
str_value1 = input("Enter First barcode to check: ")
str_value2 = input("Enter Second barcode to check: ")

if str_value1 == str_value2:
    comparison_match = "MATCH"
else:
    comparison_match = "MISMATCH"

# Future audit log required, printing variables for the time being.
print(user_name)
print(current_datetime)
print(str_value1, ", ", str_value2)
print(comparison_match)

#Test change