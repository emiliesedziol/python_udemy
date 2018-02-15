from movie5 import Movie5
import json


class Users5:
    def __init__(self, name):
        self.name = name
        self.movies = []
        self.watched = False


    def __repr__(self):
        return "<User {}>".format(self.name)


    def add_movie(self, name, genre):
        movie = Movie5(name, genre, False)
        # self.movies.append(Movie(name, genre, False))  or
        self.movies.append(movie)
        # print(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        # filter method take a list of movies and lambda function returns if watched or not
        return movies_watched

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }


    @classmethod
    def from_json(cls, json_data):
        user = Users5(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie5.from_json(movie_data))
        user.movies = movies
        return user
