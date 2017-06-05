import json
from . import statistics


class Recomendacao:
    def __init__(self, base):
        self._load_file(base)

    def _load_file(self, base):
        with open(base, "r") as base_file:
            self.base = json.loads(base_file.read())

    def get_similares(self, user):
        return [(other_user, statistics.degree_of_similarity(self.base[user], self.base[other_user]))
                    for other_user in self.base if other_user != user]

    def more_similar(self, user):
        return max(self.get_similares(user), key=lambda x: x[1])

    def get_all_movieis_available(self):
        return {movie
                for user in self.base
                for movie in self.base[user]}

    def movies_not_seen(self, user):
        return list(self.get_all_movieis_available() - set(list(self.base[user].keys())))
