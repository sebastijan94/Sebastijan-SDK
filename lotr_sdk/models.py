from dataclasses import dataclass

@dataclass
class Movie:
    """Represents a movie with its details."""
    id: str
    name: str
    runtime_in_minutes: int
    budget_in_millions: int
    box_office_revenue_in_millions: int
    academy_award_nominations: int
    academy_award_wins: int
    rotten_tomatoes_score: int

    @classmethod
    def from_json(cls, data: dict) -> 'Movie':
        """Create a Movie instance from a JSON-like dictionary.

        Args:
            data (dict): A dictionary containing movie data.

        Returns:
            Movie: An instance of the Movie class.
        """
        return cls(
            id=data.get("_id"),
            name=data.get("name"),
            runtime_in_minutes=data.get("runtimeInMinutes"),
            budget_in_millions=data.get("budgetInMillions"),
            box_office_revenue_in_millions=data.get("boxOfficeRevenueInMillions"),
            academy_award_nominations=data.get("academyAwardNominations"),
            academy_award_wins=data.get("academyAwardWins"),
            rotten_tomatoes_score=data.get("rottenTomatoesScore")
        )


@dataclass
class Quote:
    """Represents a quote from a movie."""
    id: str
    dialog: str
    movie: str  # The ID of the movie the quote is from
    character: str 

    @classmethod
    def from_json(cls, data: dict) -> 'Quote':
        """Create a Quote instance from a JSON-like dictionary.

        Args:
            data (dict): A dictionary containing quote data.

        Returns:
            Quote: An instance of the Quote class.
        """
        return cls(
            id=data.get("_id"),
            dialog=data.get("dialog"),
            movie=data.get("movie"),
            character=data.get("character")
        )
