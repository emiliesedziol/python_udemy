from movie4 import Movie4
import json


class Users4:
    def __init__(self, name):
        self.name = name
        self.movies = []


    def __repr__(self):
        return "<User {}>".format(self.name)


    def add_movie(self, name, genre):
        movie = Movie4(name, genre, False)
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


    @classmethod
    def from_json(cls, json_data):
        user = Users4(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie4.from_json(movie_data))
        user.movies = movies
        return user
