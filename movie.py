import csv
class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title

    def __str__(self):
        return str(self.movie_id + " " + self.title)

class Rating:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def __str__(self):
        return str(self.user_id + " " + self.movie_id + " " + self.rating)

    def __repr__(self):
        return str(self)

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



with open("u.item", encoding="latin_1") as item_file:
    movies = {}
    reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    for row in reader:
        movie = Movie(row['movie_id'], row['title'])
        movies[movie.movie_id] = movie
# print(movies)


with open("u.data", encoding="latin_1") as item_file:
    ratings = {}
    reader = csv.DictReader(item_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating'])
    for row in reader:
        rating = Rating(row['user_id'], row['movie_id'], row['rating'])
        ratings[rating.movie_id] = rating
# print(ratings)


with open("u.user", encoding="latin_1") as item_file:
    users = {}
    reader = csv.DictReader(item_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    for row in reader:
        user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
        users[user.user_id] = user
# print(users)
