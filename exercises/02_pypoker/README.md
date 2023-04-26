# `pypoker` - Unser erstes kleines Package


Das `package` soll zunächst grob folgende Funktionalitäten bieten:

- Karten & Pokerhände erstellen
- Pokerhände miteinander vergleichen können

Hierfür brauchen wir grob:
- `enum`s für 
  - `Rank` (Kartenrang (Ass, König, Bube, ..), 
  - `Suit` (Kartenfarbe) 
  - `HandRank` ([Stärke der Hand](https://www.onlinepoker.de/hand-rankings.php), etwa ONE_PAIR, TWO_PAIR oder FULL_HOUSE)
- Basisklassen für eine `Card` (z.B. Pik Ass) sowie eine `PokerHand` (5 Karten)

# Klasse `Card`
- Soll einzelne Spielkarte abbilden
- Karte sollen "vergleichbar" sein (\_\_eq\_\_, \_\_lt\_\_ etc.)
- Karte soll auf 2 Arten konstruierbar sein:
    1. Angabe von `Rank` & `Suit`: `Card(rank=Rank.ACE,suit=Suit.SPADE))`
    2. [Poker-Notation](https://boardgames.stackexchange.com/a/40315): `Card('Ah')`

# Klasse `PokerHand`
- Hält eine Pokerhand (bestehend aus 5 Karten) fest
- Hände sollen miteinander "vergleichbar" sein
  - siehe auch: [Poker-Handrankings](https://www.onlinepoker.de/hand-rankings.php)
  - zunächst: nur `HandRank` bestimmen
  - Bonus: Bei gleichem `HandRank` Wertigkeit betrachten, z.B. : AA > KK > QQ ..
  - Bonus Bonus: `Kickerregelung` (Wertigkeit der Beikarten betrachten)
    - z.B. AAK52 > AAQ73 (Beides ein paar Asse, K Kicker schlägt Q Kicker)
- Hände sollen auf 2 Arten konstruierbar sein:
  - Liste von Cards: `PokerHand([c1,c2,c3,c4,c5])`
  - [Poker-Notation](https://boardgames.stackexchange.com/a/40315): `PokerHand("AhAdAsAc7s")`
