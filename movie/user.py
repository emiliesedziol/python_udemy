from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    def __repr__(self):
        return "<User {}>".format(self.name)


    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        # self.movies.append(Movie(name, genre, False))  or
        self.movies.append(movie)


    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))



    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        # filter method take a list of movies and lambda function returns if watched or not
        return movies_watched


    # csv format
    def save_to_file(self):
        with open(self.name, 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name + "," + movie.genre + "," + str(movie.watched)))
                # f.write(movie.movies.name + "," + movie.movie.genre + "," + str(movie.movies.watched))





#    def watched_movies(self):
#        watched_movies_list = []


#        for movie in self.movies:
#            if movie.watched:
#                watched_movies_list.append(movie)
#

#            return watched_movies_list