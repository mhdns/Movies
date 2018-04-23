# change the status of movies to watched
# save file as a json

from movie import *


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, movie):
        if movie in self.movies:
            print("You already have the movie, {}".format(movie.name))
        else:
            self.movies.append(movie)

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
        else:
            print("You do not have the movie, {}".format(movie.name))

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def set_watched(self, movie):
        if movie in self.movies:
            movie.watched = True
        else:
            print("You do not have the movie, {}".format(movie.name))

    def json(self):
        return {
            "name": self.name,
            "movies": [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data["name"])
        movie_lst = []

        for movie in json_data["movies"]:
            movie_lst.append(Movie.from_json(movie))

        user.movies = movie_lst
        return user


