
from movie import *

while True:
    user_input = input("Please enter a movie title (partials included): ")
    list_of_titles = []
    user_output = []

    for movie in movies:
        to_be_reg = movies[movie].title
        list_of_titles.append(re.sub(r'\([^)]*\)', '', to_be_reg, flags=re.IGNORECASE))
        matching = [title for title in list_of_titles if user_input in title]
    print(matching)
    break

# print(ratings['56'].user_id) #str movie id

#
# print(users[ratings['56'].user_id])
#
# for key, value in ratings.items():
#     if users[ratings['56'].user_id] in ratings:
#         print("bingo")
