from movie import Movie

with open('my_file.txt', 'w') as f:
    f.write('Hello')


with open('my_file.txt', 'r') as f:
    print(f.readline())


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

  #  def save_to_file(self):
  #      with open("{}.csv".format(self.name), 'w') as f:
  #          for movie in self.movies:
  #              f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))

    @classmethod
    def load_from_file(cls, filename):   # changed self to cls
        with open("me.txt", 'r') as f:
            # print (f.readlines())  --> ['me\n', 'The Matrix,Sci-Fi,False\n', 'The Interview,Comedy,False\n']
            content = f.readline()  # list of lines  hmm it is not handling line break correctly
            print("content " + content)
            username = content[0] + content[1]
            print("username " + username)
            movies = []
            for line in content[1:]:  # [0] is the name, start at [1]
                print(line)
                movie_data = line.split(",")
                print(movie_data)
               # movies.append(movie_data[0], movie_data[1], movie_data[2] == "True")

            user = cls(username)
       #     user.movies = movies
            return user