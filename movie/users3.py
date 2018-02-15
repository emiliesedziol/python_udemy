from movie3 import Movie3
import json


class Users3:
    def __init__(self, name):
        self.name = name
        self.movies = []


    def __repr__(self):
        return "<User {}>".format(self.name)


    def add_movie(self, name, genre):
        movie = Movie3(name, genre, False)
        # self.movies.append(Movie(name, genre, False))  or
        self.movies.append(movie)
        # print(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        # filter method take a list of movies and lambda function returns if watched or not
        return movies_watched

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }