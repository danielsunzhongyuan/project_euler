'''
suit: Spades, Hearts, Clubs, Diamonds

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

import math
import time
import profile


class Card(object):
    def __init__(self, value):
        self._suit = value[-1]
        if self._suit not in ["H", "C", "S", "D"]:
            print "Error suit: %s" % self._suit
        if value[0] == "T":
            self._number = 10
        elif value[0] == "J":
            self._number = 11
        elif value[0] == "Q":
            self._number = 12
        elif value[0] == "K":
            self._number = 13
        elif value[0] == "A":
            self._number = 14
        else:
            self._number = int(value[0])

    @property
    def number(self):
        return self._number

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return str(self._number) + self._suit

    def __cmp__(self, card):
        if self.number > card.number:
            return 1
        elif self.number < card.number:
            return -1
        else:
            return 0


class Hand(object):
    def __init__(self):
        self._rank = 0
        self._highest_values = []
        self._cards = []

    @property
    def rank(self):
        self.rank_hand()
        return self._rank

    @property
    def highestValues(self):
        self.rank_hand()
        return self._highest_values

    def add_card(self, *args):
        for card in args:
            self._cards.append(card)

    def sort_card(self):
        self._cards.sort(reverse=True)

    def rank_hand(self):
        self.sort_card()
        if len(set([card.suit for card in self._cards])) == 1:
            self._rank = 6
            if self._cards[0].number - self._cards[-1].number == 4:
                if self._cards[0].number == 14:
                    self._rank = 10
                else:
                    self._rank = 9
                self._highest_values.append(self._cards[0].number)
            else:
                self._highest_values = [card.number for card in self._cards]
        elif len(set([card.number for card in self._cards])) == 2:
            if self._cards[1].number == self._cards[3].number:
                self._rank = 8
            else:
                self._rank = 7
            self._highest_values.append(self._cards[2].number)
        elif len(set([card.number for card in self._cards])) == 3:
            if (self._cards[0].number == self._cards[1].number == self._cards[2].number)\
                or (self._cards[1].number == self._cards[2].number == self._cards[3].number)\
                or (self._cards[2].number == self._cards[3].number == self._cards[4].number):
                self._rank = 4
                self._highest_values.append(self._cards[2].number)
            else:
                self._rank = 3
                self._highest_values.append(self._cards[1].number)
                self._highest_values.append(self._cards[3].number)
                if self._cards[0].number > self._cards[1].number:
                    self._highest_values.append(self._cards[0].number)
                elif self._cards[2].number > self._cards[3].number:
                    self._highest_values.append(self._cards[2].number)
                else:
                    self._highest_values.append(self._cards[4].number)
        elif len(set([card.number for card in self._cards])) == 4:
            self._rank = 2
            #self._highest_values = reduce(lambda x, y: x if y in x else x + [y], [[], ] + [card.number for card in self._cards])
            if self._cards[0].number == self._cards[1].number:
                self._highest_values.append(self._cards[0].number)
                self._highest_values.append(self._cards[2].number)
                self._highest_values.append(self._cards[3].number)
                self._highest_values.append(self._cards[4].number)
            if self._cards[2].number == self._cards[1].number:
                self._highest_values.append(self._cards[1].number)
                self._highest_values.append(self._cards[0].number)
                self._highest_values.append(self._cards[3].number)
                self._highest_values.append(self._cards[4].number)
            if self._cards[2].number == self._cards[3].number:
                self._highest_values.append(self._cards[3].number)
                self._highest_values.append(self._cards[0].number)
                self._highest_values.append(self._cards[1].number)
                self._highest_values.append(self._cards[4].number)
            if self._cards[4].number == self._cards[3].number:
                self._highest_values.append(self._cards[3].number)
                self._highest_values.append(self._cards[0].number)
                self._highest_values.append(self._cards[1].number)
                self._highest_values.append(self._cards[2].number)
        else:
            if self._cards[0].number - self._cards[4].number == 4:
                self._rank = 5
            else:
                self._rank = 1
            self._highest_values = [card.number for card in self._cards]

    def doesWin(self, anotherHand):
        if self.rank > anotherHand.rank:
            return 1
        elif self.rank < anotherHand.rank:
            return -1
        else:
            ret = 0
            for i in range(len(self.highestValues)):
                if self.highestValues[i] > anotherHand.highestValues[i]:
                    ret = 1
                    break
                elif self.highestValues[i] < anotherHand.highestValues[i]:
                    ret = -1
                    break
            return ret

    def __str__(self):
        return " ".join([str(card) for card in self._cards])
    def __repr__(self):
        return " ".join([str(card) for card in self._cards])


def main():
    '''sss'''
    start = time.time()
    print __doc__

    with open("p054_poker.txt", "rU") as file_handler:
        hands = file_handler.readlines()
    ret = 0
    for hand in hands:
        hand = hand.strip()
        cards = hand.split()
        player1 = Hand()
        player2 = Hand()
        for i in range(5):
            player1.add_card(Card(cards[i]))
            player2.add_card(Card(cards[i+5]))
        if player1.doesWin(player2) == 1:
            ret += 1

    print ret
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
