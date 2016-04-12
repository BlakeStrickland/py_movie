import csv
import re
from ratings import *
from users import *

class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title

    def __str__(self):
        return str(self.movie_id + " " + self.title)

    # def movie_by_id(self, user_input, movies):
    # # user_input = int(input("Please enter a movie id: "))
    #     if str(user_input) in movies.keys():
    #         return movies[str(user_input)]
    #         # print("the movie id is: {}, the title is : {}".format(user_input, movies[str(user_input)]))

    def read_movies(file_name):

        with open(file_name, encoding="latin_1") as item_file:
            movies = {}
            reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
            for row in reader:
                movie = Movie(row['movie_id'], row['title'])
                movies[movie.movie_id] = movie
# print(movies)



'''
# Get movie by id -

user_input = int(input("Please enter a movie id: "))
if str(user_input) in movies.keys():
    print("id: {}".format( movies[str(user_input)]))

'''

'''
Get movie by title -

user_input = input("Please enter a movie title (partials included): ")

list_of_titles = []
user_output = []

for movie in movies:
    to_be_reg = movies[movie].title.lower()
    list_of_titles.append(re.sub(r'\([^)]*\)', '', to_be_reg))
    matching = [title.title() for title in list_of_titles if user_input in title]



# if any(user_input in list_of_titles for ext in extensionsToCheck):
#     print(url_string)

# if user_input in list_of_titles:
#
#     user_output.append(user_input)
'''





####
