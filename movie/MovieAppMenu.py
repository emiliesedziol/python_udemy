import json
import os
from users5 import Users5


def menu ():

    name = input("Enter your name ")
    filename = "{}.txt".format(name)
    print(filename)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = Users5.from_json(json_data)
    else:
        user = Users5(name)

    user_input = input("Enter 'a' to add movie, 's' to see list of movies, "
          "'w' to set movie as watched, 'd' to delete a movie, "
          "'l' to see a list of watched movies, 'f' save or 'q' to quit")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter movie name ")
            movie_genre = input("Enter movie genre ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre {} Watched {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched ")
            user.set_watch(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: () Genre {} Watched {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)


        user_input = input("Enter 'a' to add movie, 's' to see list of movies, "
                           "'w' to set movie as watched, 'd' to delete a movie, "
                           "'l' to see a list of watched movies, 'f' save or 'q' to quit")


def file_exists(filename):
    return os.path.isfile(filename)


menu()