from users4 import Users4
import json


users3 = Users4("me")


users3.add_movie("The Matrix", "Sci-Fi")
users3.add_movie("The Interview", "Comedy")

# print(users3.json())


with open("me.txt", 'r') as f:
    json_data = json.load(f)
    user = Users4.from_json(json_data)
    print(user.json())
