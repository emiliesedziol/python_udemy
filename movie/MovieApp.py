from movie import Movie
from user import User

user = User("me")

print(user)  # --> <user.User object at 0x10441e358>  memory address
# added to class user.py __repr__(self) and the output changed to <User me>

my_movie = Movie("The Matrix", "Sci-Fi", True)  # if False [] display if True the movie name and genre displays
# from class movie.py __repr__(self)

user.movies.append(my_movie)

print(user.watched_movies())


# print(my_movie.name)


# print(my_movie.director)
#  director has be added to the class movie.py before this will work

