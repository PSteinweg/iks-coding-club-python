from functools import (
    total_ordering,
)  # Implementiert fehlende Vergleichsoperatoren , falls mindestens einer von (>,<) und == implementiert ist
import enum
from typing import Any, Literal


@total_ordering
class Rank(enum.Enum):
    """Enum for card ranks."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self: "Rank", other: object) -> Any:
        if not isinstance(other, Rank):
            raise NotImplementedError()
        return self.value == other.value

    def __lt__(self: "Rank", other: object) -> Any:
        if not isinstance(other, Rank):
            raise NotImplementedError()
        return self.value < other.value

    def to_str(self) -> str:
        """Converts a Rank into string notation of the rank.

        Returns:
            str: The string notation of the rank, e.g. Rank.ACE -> A
        """
        match self:
            case Rank.ACE:
                return "A"
            case Rank.KING:
                return "K"
            case Rank.QUEEN:
                return "Q"
            case Rank.JACK:
                return "J"
            case Rank.TEN:
                return "T"
            case _:
                return str(self.value)

    @staticmethod
    def from_string(
        rank_string: Literal["A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2]
    ) -> "Rank":
        """Converts Rank as `str` in poker notation into rank enum

        Args:
            rank_string (Literal[&quot;A&quot;, &quot;K&quot;, &quot;Q&quot;, &quot;J&quot;, &quot;T&quot;, 9, 8, 7, 6, 5, 4, 3, 2]): _description_

        Raises:
            ValueError: Raised if rank_string not in (Literal[&quot;A&quot;, &quot;K&quot;, &quot;Q&quot;, &quot;J&quot;, &quot;T&quot;, 9, 8, 7, 6, 5, 4, 3, 2])

        Returns:
            Rank: converted rank_string as enum.
        """
        match rank_string:
            case "A":
                return Rank.ACE
            case "K":
                return Rank.KING
            case "Q":
                return Rank.QUEEN
            case "J":
                return Rank.JACK
            case "T":
                return Rank.TEN
            case _:
                if int(rank_string) in [2, 3, 4, 5, 6, 7, 8, 9]:
                    return Rank(int(rank_string))
                else:
                    raise ValueError("passed value {rank_string} is not supported.")


@total_ordering
class Suit(enum.Enum):
    """Enum for card suits (i.e. SPADE, CLUBS, HEARTS, DIAMONDS)

    Args:
        enum (_type_): _description_
    """

    pass


@total_ordering
class HandRank(enum.Enum):
    """Enum for poker hand ranks, see: https://www.onlinepoker.de/hand-rankings.php"""

    pass
