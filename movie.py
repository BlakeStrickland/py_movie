import csv
class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title

    def __str__(self):
        return str(self.movie_id + " " + self.title)

with open("u.item", encoding="latin_1") as item_file:
    movie_obj_list = []
    reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    for row in reader:
        movie_obj_list.append(Movie(row['movie_id'], row['title']))

print(movie_obj_list)
