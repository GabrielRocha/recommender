import statistics
from collections import defaultdict
import json
from movielens import database


def from_json(json_file):
    with open(json_file, "r") as base_file:
        return Analysis(json.loads(base_file.read()))


def from_movielens():
    return Analysis(database.get_reviews())


class Analysis:
    def __init__(self, base):
        self.base = base

    def get_similares(self, user):
        return ((user_of_base, statistics.degree_of_similarity(self.base[user], self.base[user_of_base]))
                for user_of_base in self.base if user_of_base != user)

    def more_similar(self, user):
        return max(self.get_similares(user), key=lambda x: x[1])

    def all_users(self):
        return [user for user in self.base]

    def all_movieis_available(self):
        return {movie for user in self.base for movie in self.base[user]}

    def movies_not_seen(self, user):
        return list(self.all_movieis_available() - set(list(self.base[user].keys())))

    def who_saw_movie_not_seen(self, user):
        who_saw = {}
        for user_of_base in self.base:
            if user_of_base == user:
                continue
            similarity = statistics.degree_of_similarity(self.base[user], self.base[user_of_base])
            if similarity <= 0:
                continue
            who_saw[user_of_base] = {"similarity": similarity,
                                     "movies": {movie: self.base[user_of_base][movie]
                                                for movie in self.movies_not_seen(user)
                                                if movie in self.base[user_of_base]}}
        return who_saw

    def total_similarity_with_who_saw_movie_not_seen(self, user):
        who_have_seen = self.who_saw_movie_not_seen(user)
        statics_similarity = {}
        for user_have_seen, statics in who_have_seen.items():
            for movie in statics['movies']:
                if movie not in statics_similarity:
                    statics_similarity[movie] = defaultdict(float)
                statics_similarity[movie]['sum_similarity'] += statics['similarity']
                statics_similarity[movie]['sum_review'] += statics['movies'][movie] * statics['similarity']
        return statics_similarity

    def predict_movie_review(self, user, how_many=3):
        movies = [(movie, round(statics['sum_review']/statics['sum_similarity'], 2))
                  for movie, statics in self.total_similarity_with_who_saw_movie_not_seen(user).items()]
        return sorted(movies, key=lambda x: x[1], reverse=True)[:how_many]
