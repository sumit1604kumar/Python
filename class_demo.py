class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"user {self.name} currently works as a {self.current_job_title}. you can contact them at {self.email}")

#creating an object
"""
app_user_one = User("skumar2@tnsi.com", "sumit", "psd", "network")
app_user_one.get_user_info()

app_user_one.change_job_title("automation engg")
app_user_one.get_user_info()

print("User two")

app_user_two = User("anju@tnsi.com", "anju", "psd", "DevOps")
app_user_two.get_user_info()
app_user_two.change_job_title("Developer")
app_user_two.get_user_info()
"""



