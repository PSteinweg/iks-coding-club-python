""" Test cases for pypoker.enums
"""

import pytest
from pypoker.enums import Rank


class TestRank:
    """Tests for `Rank` enum."""

    rank_strings = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    ranks = [
        Rank.TWO,
        Rank.THREE,
        Rank.FOUR,
        Rank.FIVE,
        Rank.SIX,
        Rank.SEVEN,
        Rank.EIGHT,
        Rank.NINE,
        Rank.TEN,
        Rank.JACK,
        Rank.QUEEN,
        Rank.KING,
        Rank.ACE,
    ]
    rank_with_rank_string = list(zip(ranks, rank_strings))

    @pytest.mark.skip()
    def test___eq__(self):
        pass

    @pytest.mark.skip()
    def test__lt__(self):
        pass

    @pytest.mark.parametrize("rank, rank_string", rank_with_rank_string)
    def test_to_str(self, rank, rank_string):
        assert Rank.to_str(rank) == rank_string

    @pytest.mark.parametrize("rank, rank_string", rank_with_rank_string)
    def test_rank_from_string(self, rank, rank_string):
        assert Rank.from_string(rank_string) == rank
