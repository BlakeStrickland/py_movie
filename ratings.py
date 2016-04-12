import csv
import re
from users import *


class Rating:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def __str__(self):
        return str(self.user_id + " " + self.movie_id + " " + self.rating)

    def __repr__(self):
        return str(self)



with open("u.data") as item_file:
    ratings = {}
    reader = csv.DictReader(item_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating'])
    for row in reader:
        rating = Rating(row['user_id'], row['movie_id'], row['rating'])
        ratings[rating.movie_id] = rating
# print(ratings)
hash_of_ratings = {}
list_of_ratings = []
for the_movie_id, the_rating_object in ratings.items():
# if movie_id in
    if the_movie_id == the_rating_object.movie_id:
        hash_of_ratings[the_rating_object.movie_id] = list_of_ratings.append(int(the_rating_object.rating))

# print(sum(list_of_ratings))
