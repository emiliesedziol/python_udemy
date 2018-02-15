from users3 import Users3
import json


users3 = Users3("me")


users3.add_movie("The Matrix", "Sci-Fi")
users3.add_movie("The Interview", "Comedy")

print(users3.json())


with open("me.txt", 'w') as f:
    json.dump(users3.json(), f)
