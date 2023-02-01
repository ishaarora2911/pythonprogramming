class Musicimdb:

    def __init__(self, year, name, rating,vote, rank):
        self.year = year
        self.name = name
        self.rating = rating
        self.vote=vote
        self.rank=rank


    def to_csv(self):
        return "{year},{name},{rating},{vote}, {rank}\n".format_map(vars(self))