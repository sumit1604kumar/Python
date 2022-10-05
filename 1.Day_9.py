# Dictionaries TASK 1 to create new dictionary from the blank one

# student_scores = {
#     "Harry": 81,
#      "Ron": 78,
#     "Hermione": 99,
#      "Draco": 74,
#      "Neville":62,
# }
#
# student_grades = {}
#
# for item in student_scores:
#     if student_scores[item] > 90 and student_scores[item] <= 100:
#         student_grades[item] =  "Outstanding"
#     elif student_scores[item] > 80 and student_scores[item] <= 90:
#         student_grades[item] = "Exceeds Expectations"
#     elif student_scores[item] > 70 and student_scores[item] <= 80:
#         student_grades[item] = "Acceptable"
#     else:
#         student_grades[item] = "Fail"
#
# print(student_grades)

#TASK 2 Travel log
# travel_log =[
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# }
# ]
# def add_new_country(a,b,c):
#     travel_log.append({"country":a, "visits":b,"cities":c, })
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# print(travel_log[2])
#Action_game_Project
# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# print(logo)
#
# print("Welcome to the secret auction Program")
# flow = True
#
# dict = {}
#
# while flow == True:
#     name = input("What is your name ?")
#     bid = int(input("What yours Bid ? $"))
#     more_user = input("Are there any more bidder 'Yes' or 'No'")
#     dict.update({name:bid})
#     if more_user == 'no':
#         flow = False
# print(dict)
# bid_max = max(dict, key=dict.get)
# print(f"The Winner is {bid_max} with a bid of ${dict[bid_max]}")

