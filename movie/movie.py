class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched   # boolean
         # self.director = "Wachowski"


    def __repr__(self):
        return "Movie name {} gengre {}.".format(self.name, self.genre)