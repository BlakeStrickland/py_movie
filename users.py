import csv
import re
from ratings import *

class User:
    def __init__(self, user_id, age, gender, occupation, zip_code):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zip_code = zip_code

    def __str__(self):
        return str(self.user_id + " " + self.age + " " + self.gender + " " + self.occupation + " " + self.zip_code )

    def __repr__(self):
        return str(self)

    def read_users(filename):
        with open(file_name) as users_file:
            users = {}
            reader = csv.DictReader(users_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
            for row in reader:
                user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
                users[user.user_id] = user
        # print(users)
