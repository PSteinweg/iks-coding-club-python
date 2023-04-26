from attr import dataclass
from pypoker.enums import Rank, Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit

    @staticmethod
    def from_string(card_string: str) -> "Card":
        raise NotImplementedError()


class PokerHand:
    def __init__(self) -> None:
        pass

    @staticmethod
    def from_string(hand_string: str) -> "PokerHand":
        raise NotImplementedError()
