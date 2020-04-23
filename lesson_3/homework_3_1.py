# Input two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = 7
second_number = 5
result_1 = None
if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
print(result_1)


# Input a number that is under 20 in number_1 variable. If this number is 20 or
# # higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = 17
result_2 = None
if number_1 >= 20:
    result_2 = "Too high"
else:
    result_2 = "Thank you"
print(result_2)


# Input your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = "Alexey"
last_name = "Lapkouski"
result_3 = None
if len(first_name) < 5:
    result_3 = (first_name + last_name).upper()
else:
    result_3 = first_name.lower()
print(result_3)


# Input a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = 25
result_4 = None
if number_2 >= 10 and number_2 <= 20:
    result_4 = "Thank you"
else:
    result_4 = "Incorrect answer"
print(result_4)


# Input your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 15
result_5 = None
if age >= 18:
    result_5 = "You can vote"
if age == 17:
    result_5 = "You can learn to drive"
if age == 16:
    result_5 = "You can buy a lottery ticket"
if age < 16:
    result_5 = "You can go Trick-or-Treating"
print(result_5)

# Input a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_decade in lower case

month = 9
result_month = None
if month == 1:
    result_month = "January".lower()
if month == 2:
    result_month = "February".lower()
if month == 3:
    result_month = "March".lower()
if month == 4:
    result_month = "April".lower()
if month == 5:
    result_month = "May".lower()
if month == 6:
    result_month = "June".lower()
if month == 7:
    result_month = "July".lower()
if month == 8:
    result_month = "August".lower()
if month == 9:
    result_month = "September".lower()
if month == 10:
    result_month = "October".lower()
if month == 11:
    result_month = "November".lower()
if month == 12:
    result_month = "December".lower()
print(result_month)
