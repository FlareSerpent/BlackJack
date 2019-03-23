import math
import turtle


suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]



def cards():
    deck = []
    for x in suit:
        for y in rank:
            deck.append(y + " of " + x)
    return deck

#print(cards())


def assign_value():
    value = {}
    for card in cards():
        for i in range(2, 11):
            if str(i) in card:
                value[card] = i
            elif 'Jack' in card:
                value[card] = 10
            elif 'Queen' in card:
                value[card] = 10
            elif 'King' in card:
                value[card] = 10
            elif 'Ace' in card:
                value[card] = 1

    return(value)
print(assign_value())
