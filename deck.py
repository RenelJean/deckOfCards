import random


class Card:

    # initalize A single card

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


card = Card("Card", 6)

card.show()


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Diamonds", "Spades", "Club", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


# calls shuffle and display deck

    def drawCard(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.show()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []


    def draw(self, deck):
        self.hand.append(deck.drawCard())

        return self


    def showHand(self):
        for card in self.hand:
            card.show()
            deck = Deck()
            deck.shuffle()


def main():
    renel = Player("Renel")
    renel.draw(deck)
    renel.showHand


main()
