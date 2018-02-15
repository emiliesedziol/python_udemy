from users1 import User

users1 = User("me")  # removed when self is changed to cls in users1.py

users1 = User.load_from_file('me.txt')


print(users1.name)
print(users1.movies)

# the following writes a file
# users1.add_movie("The Matrix", "Sci-Fi")
# users1.add_movie("The Interview", "Comedy")

# users1.save_to_file()