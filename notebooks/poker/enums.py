from functools import total_ordering
import enum

@total_ordering
class Rank(enum.Enum):
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

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def to_str(self):
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


@total_ordering
class Suit(enum.Enum):

    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

    @staticmethod
    def list():
        return list(map(lambda c: c.value, Suit))
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def to_str(self):
        match self:
            case Suit.HEARTS:
                return "h"
            case Suit.DIAMONDS:
                return "d"
            case Suit.CLUBS:
                return "c"
            case Suit.SPADES:
                return "s"

@total_ordering
class HoldemRank(enum.Enum):
    HIGH_CARD: 1
    SINGLE_PAIR: 2
    TWO_PAIR: 3
    TRIPS: 4
    STRAIGHT: 5
    FLUSH: 6
    FULL_HOUSE: 7
    QUADS: 8
    STRAIGHT_FLUSH: 9
    ROYAL_FLUSH: 10

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value == other.value
    
    