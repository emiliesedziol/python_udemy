from user import User

# my_user = User.load_from_db_by_email('me@be.com')
my_user = User('feeb@bjeb.com', 'mfeb', 'jeeb', None)  # None is the id, postgres should increment this

# print(my_user.email)  if def __repr__(self): isn't set in the class  import user is needed on this line and next
# print(my_user)
my_user.save_to_db()
#print(my_user)