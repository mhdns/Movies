from user import *
import json
import os

# Anas = User("Anas")
# print(Anas)
#
#
# Avatar = Movie("Avatar", "Sci-Fi", False)
# print(Avatar)
# B_panther = Movie("Black Panther", "Sci-Fi", False)
# Anas.add_movie(Avatar)
# Anas.add_movie(B_panther)
# print(Anas.movies)
# Anas.add_movie(B_panther)

def menu():
    name = input("Enter your name: ")
    filename = "{}.json".format(name)
    if file_exists(filename):
        with open(filename, "r") as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter\n 'a' to add a movie,\n 's' to see the list of movies,\n "
                       "'w' to set a movie as watched,\n 'd' to delete a movie,\n 'l' to see the list of watched movies"
                       ",\n 'f' to save or 'q' to quit: \n")

    while user_input != "q":
        if user_input == "a":
            movie_name = input("Enter Movie Title: ")
            movie_genre = input("Enter Movie Genre: ")
            movie = Movie(movie_name, movie_genre, False)
            user.add_movie(movie)
        elif user_input == "s":
            print(list(map(lambda movie: movie.name, user.movies)))
        elif user_input == "w":
            watched_movie = input("Enter Movie Title: ")
            for movie in user.movies:
                if movie.name == watched_movie:
                    user.set_watched(movie)
                    print("You watched {}!".format(watched_movie))
                    break
        elif user_input == "d":
            delete_movie = input("Enter Movie Title: ")
            for movie in user.movies:
                if movie.name == delete_movie:
                    user.remove_movie(movie)
                    print("You deleted {}!".format(delete_movie))
                    break
        elif user_input == "l":
            watched_movies = []
            for movie in user.watched_movies():
                watched_movies.append(movie.name)
            print("Your Movies: {}".format(watched_movies))
        elif user_input == "f":
            with open(filename, "w") as f:
                json.dump(user.json(), f)
        user_input = input("Enter\n 'a' to add a movie,\n 's' to see the list of movies,\n "
                       "'w' to set a movie as watched,\n 'd' to delete a movie,\n 'l' to see the list of watched movies"
                       ",\n 'f' to save or 'q' to quit: \n")
    return None

def file_exists(filename):
    return os.path.isfile(filename)

menu()