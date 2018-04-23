# Create a movie class with name, genre and watched
# Change the representation of the class
# Define a csv and json method to store and read details

class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "watched": self. watched
        }
    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data)
