# Functions with Output
# def format(fname, lname):
#     format_fname = fname.title()
#     format_lname = lname.title()
#     return f"{format_fname}  {format_lname}"
# print(format("sumIt", "ANJU"))
# # print(a)
# Days in Month

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(abc,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(abc) == True:
#         if month == 2 :
#             days = 29
#             return days
#         days = month_days[month - 1 ]
#         return days
#     else:
#         days = month_days[month -1 ]
#         return days
#
#
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Project - Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations  = {
    "+" : add,
    "-": sub,
    "*" : mul,
    "/" : div
}

def calculator():
    should_continue = True
    num1 = float(input("What's the first number ?:"))
    for key in operations:
        print(key)
    while should_continue:

        operation_symbol = input("Pick an operation :")
        num2 = float(input("What's the Next number ?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")
        user_input = input(f"Type 'Y' to continue calculating with {answer}: or type 'n' to start again")
        if user_input == 'y':
            num1 = answer
        elif user_input == 'n':
            should_continue = False
            calculator()
        else:
            print("Program finished")
            should_continue = False

calculator()