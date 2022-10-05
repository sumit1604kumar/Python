"""print("  20 days are " +str(50)  + " minutes") # int and string story
#print(f" 20 days are {50} minutes")
#print(f" 30 days are {30*24*60*60} in seconds")  # f stands for string format
#variables
to_seconds = 5
name_to = "in seconds"
#print(f" 30 days are {30*to_seconds} {name_to}")
# functions
def days_to_units(days): #arguments is passed
    if days >0:
        print(f" 1. sumit {days} days are {days * to_seconds} {name_to}")
        return f" sumit {days} days are {days * to_seconds} {name_to}"
    else:
        print("enter the positive number")
sumit = days_to_units(10)
print(f" 2. This is the value from the functions returning the value .{sumit}")
#user input
User_input =input("enter the number\n")
a = int(User_input)
anju = days_to_units(a)
print(anju)
#print(User_input)
#functions with return output and followed by If else below data from the file class_demo """

from class_demo import User
from post import Post

app_user_one = User("skumar2@tnsi.com", "sumit", "psd", "network")
app_user_one.get_user_info()

app_user_one.change_job_title("automation engg")
app_user_one.get_user_info()

print("User two")

app_user_two = User("anju@tnsi.com", "anju", "psd", "DevOps")
app_user_two.get_user_info()

app_user_two.change_job_title("Developer")
app_user_two.get_user_info()

new_post = Post("on a secret mission", app_user_two.name)
new_post.get_post_info()
