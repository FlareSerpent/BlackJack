import random
class Deck:

    def __init__(self):
        self.suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = []
        self.value = {}
        self.player_hand = []
        self.dealer_hand = []
        self.total_value = 0

    #Add and shuffle cards to deck
    def load_deck(self):
        for x in self.suit:
            for y in self.rank:
                self.deck.append(y + " of " + x)
        random.shuffle(self.deck)
        return self.deck

    #Assign point values to cards
    def assign_value(self):
        for card in self.deck:
            for i in range(2, 11):
                if str(i) in card:
                    self.value[card] = i
                elif 'Jack' in card:
                    self.value[card] = 10
                elif 'Queen' in card:
                    self.value[card] = 10
                elif 'King' in card:
                    self.value[card] = 10
                elif 'Ace' in card:
                    if self.player_points < 21:
                        self.value[card] = 1
        return self.value

    #Add cards to dealer and player's hand
    def deal_hand(self):
        player


def deal_cards(cards):
    deck = cards.load_deck()
    card_points = cards.assign_value()
    player_points = 0
    dealer_points = 0
    player_starting_hand = deck[:2]
    dealer_starting_hand = deck[2:4]
    for key, value in card_points.items():
        for card in player_starting_hand:
            if card in key:
                player_points += card_points[key]
        for card in dealer_starting_hand:
            if card in key:
                dealer_points += card_points[key]
    print(player_starting_hand)
    print(dealer_starting_hand)
    print(player_points)
    print(dealer_points)

def rules():

def main():
    game = Deck()
    deal_cards(game)

if __name__ == "__main__":
    main()