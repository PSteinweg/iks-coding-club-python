from typing import List
import treys
from treys import Card, Deck
import copy


# Deck initialisieren
# 2 Spieler mit jeweils 2 Startkarten


def produce_tv_display(hand_1: [Card, Card], hand_2: [Card, Card], community_cards: List[Card]):
    # Keine Gemeinschaftskarten: [] // Keine Gemeinschaftskarten ausgeteilt
    # 3 Gemeinschaftskarten: [4c, 4d, 8h] // Nur Flop
    # 4 Gemeinschaftskarten: [5d, 6s, Kh, Js] // Flop & Turn ausgeteilt
    # Deck initialisieren
    deck = treys.Deck()
    # Starthände & Gemeinschaftskarten aus dem Deck entfernen
    # remove_cards_from_deck(deck, cards)
    remove_cards_from_deck(deck, [*hand_1, *hand_2, *community_cards])
    # Monte-Carlo-Simulation
    # teile die restlichen Karten aus
    # bestimme den Gewinner nachdem alle Gemeinschaftskarten ausgeteilt wurden
    # Halt den Gewinner in einer Datenstruktur fest {player_a_wins: 23223, player_b_wins: 133235, ties: ?}
    # Bestimme die Gewinnwahrscheinlichkeiten: (player_a_wins / anzahl_durchläufe)*100 bzw. (player_b_wins / anzahl_durchläufe)* 100
    # Textdarstellung produzieren
    produce_text_display(hand_1, hand_2)

    # Bestimme die Outs / exhaustive => deck - ausgeteilte Karten, für jede Möglichkeit gucken, ob schlechterer Spieler gewinnt


def do_n_monte_carlo(state, iterations=1000):
    for i in range(iterations):
        pass
        # monte_carlo_simulation(state)
        # if a_wins:
        #    a_wins++
        # if b_wins:
        #    b_wins++
    return {'hand_a_wins': 5, 'hand_b_wins': 10, 'tie': 2, 'total_iterations': iterations}


def monte_carlo_simulation(
    hand_1: [Card, Card], hand_2: [Card, Card], community_cards: List[Card], deck: Deck
):
    evaluator = Evaluator()
    new_deck = copy.deepcopy(deck)

    number_of_cards_to_draw = 5 - len(community_cards)
    final_board = community_cards + [
        Card(card_int) for card_int in new_deck.draw(number_of_cards_to_draw)
    ]

    # Teile Karten aus bis Community-Cards = 5
    # Werte den Gewinner aus
    # Gib Gewinner zurück


def remove_cards_from_deck(deck, cards: List[Card]):
    for card in cards:
        if card in deck.cards:
            deck.cards.remove(card)
    return deck


def produce_text_display(
    hand_1: [Card, Card] = ["Ac", "Js"],
    hand_2: [Card, Card] = ["Ks", "Kh"],
    hand_1_equity: int = 0,
    hand_2_equity: int = 100,
    board: List[Card] = ["Ad", "Ks", "Qd"],
    outs: List[Card] = [],
) -> None:
    """Erzeugt die eigentliche Textanzeige.

    Example:

    Hand 1: AcJs (9,..%)
    Hand 2: KsKh (91, ..%)
    Board: Tc4hJd Jc
    Outs: [KdKcJhJc]
    """

    template = f"""
    Hand 1: {hand_1[0]} {hand_1[1]} ({hand_1_equity} %)
    Hand 2: {hand_2[0]} {hand_2[1]} ({hand_2_equity} %)
    Board: {" ".join(board)}
    Outs: {outs}
    """

    print(template)


if __name__ == '__main__':
    # produce_text_display()
    # deck = treys.Deck()
    ace_of_hearts = treys.Card.new("Ah")  # Karte erzeugen als int
    two_of_spades = treys.Card.new("2s")
    ace_of_spades = treys.Card.new("As")
    six_of_clubs = treys.Card.new("6c")

    queen_of_diamonds = treys.Card.new("Qd")
    produce_tv_display(
        hand_1=[ace_of_hearts, two_of_spades],
        hand_2=[ace_of_spades, six_of_clubs],
        community_cards=[queen_of_diamonds],
    )
    # remove_cards_from_deck(deck, [ace_of_hearts, two_of_spades])
    # print(len(deck.cards))
    # print(deck)

    # print(Card.int_to_str(ace_of_hearts))  # aus int wieder string produzieren
    # print(deck.cards.remove(<Kartenwert>))
