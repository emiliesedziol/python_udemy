class Movie5:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched   # boolean
         # self.director = "Wachowski"


    def __repr__(self):
        return "Movie name {} gengre {}.".format(self.name, self.genre)


    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }


    @classmethod
    def from_json(cls, json_data):
        return Movie5(**json_data)
        # return Movie5(genre=json_data['genre'], watched=json_data['watched'], name=json_data['name'])

