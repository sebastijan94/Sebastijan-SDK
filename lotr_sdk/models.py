class Movie:
    def __init__(self, _id, name, runtime_in_minutes, budget_in_millions, box_office_revenue_in_millions,
                 academy_award_nominations, academy_award_wins, rotten_tomatoes_score):
        self.id = _id
        self.name = name
        self.runtime_in_minutes = runtime_in_minutes
        self.budget_in_millions = budget_in_millions
        self.box_office_revenue_in_millions = box_office_revenue_in_millions
        self.academy_award_nominations = academy_award_nominations
        self.academy_award_wins = academy_award_wins
        self.rotten_tomatoes_score = rotten_tomatoes_score

    @classmethod
    def from_json(cls, data):
        return cls(
            _id=data.get("_id"),
            name=data.get("name"),
            runtime_in_minutes=data.get("runtimeInMinutes"),
            budget_in_millions=data.get("budgetInMillions"),
            box_office_revenue_in_millions=data.get("boxOfficeRevenueInMillions"),
            academy_award_nominations=data.get("academyAwardNominations"),
            academy_award_wins=data.get("academyAwardWins"),
            rotten_tomatoes_score=data.get("rottenTomatoesScore")
        )


class Quote:
    def __init__(self, _id, dialog, movie, character):
        self.id = _id
        self.dialog = dialog
        self.movie = movie
        self.character = character

    @classmethod
    def from_json(cls, data):
        return cls(
            _id=data.get("_id"),
            dialog=data.get("dialog"),
            movie=data.get("movie"),
            character=data.get("character")
        )
