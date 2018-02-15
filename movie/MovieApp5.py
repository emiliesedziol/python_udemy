from users5 import Users5
import json


users5 = Users5("me")


users5.add_movie("The Matrix", "Sci-Fi")
users5                                                                                                                                                                              .add_movie("The Interview", "Comedy")

# print(users3.json())


with open("me.txt", 'r') as f:
    json_data = json.load(f)
    user = Users5.from_json(json_data)
    print(user.json())
