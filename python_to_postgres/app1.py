from database import Database
from user import User


Database.initialize(database="learning", host="localhost", user="postgres", password="a4600oldjob")

my_user = User('feeb@bjeb.com', 'mfeb', 'jeeb', None)  # None is the id, postgres should increment this

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('me@be.com')

print(user_from_db)