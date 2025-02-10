import copy
import random
class Card:
    """Spades=3
    Hearts=2
    Diamonds=1
    Clubs=0
    Jack=11
    Queen=12
    King=13"""
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    suit_names=["Clubs","Diamonds","Hearts","Spades"]
    rank_names=[None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"
    def __eq__(self, other):
        return self.suit==other.suit and self.rank==other.rank
    def __lt__(self, other):
        t1=self.suit,self.rank
        t2=other.suit,other.rank
        return t1<t2
class Deck:
    def __init__(self):
        self.cards=[]
        for s in range(4):
            for r in range(1,14):
                card=Card(s,r)
                self.cards.append(card)
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    def remove_card(self,card):
        return self.cards.remove(card)
    def pop_card(self,i=-1):
        return self.cards.pop(i)
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())
class Hand(Deck):
    def __init__(self,label=""):
        self.cards=[]
        self.label=label
def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

class PokerHand(Hand):
    """Represents a poker hand."""
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits_count = {}
        for card in self.cards:
            self.suits_count[card.suit] = self.suits_count.get(card.suit, 0) + 1
    def rank_hist(self):
        self.rank_count = {}
        for card in self.cards:
            self.rank_count[card.rank] = self.rank_count.get(card.rank, 0) + 1
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    def has_pair(self,i=2):
        self.rank_hist()
        for count in self.rank_count.values():
            if count==i:
                return True
        return False
    def has_two_pair(self):
        self.rank_hist()
        n=0
        for count in self.rank_count.values():
            if count==2:
                n+=1
                if n==2:
                    return True
        return False
    def has_three_of_a_kind(self,i=3):
        return self.has_pair(i=3)
    def has_straight(self):
        self.rank_hist()
        sorted_rank=sorted(self.rank_count.keys())

        count=0
        for i in range(len(sorted_rank)-1):
            if sorted_rank[i]+1==sorted_rank[i+1]:
                count+=1
                if count==4:
                    return True
            else:
                count=0
        if {1,2,3,4,5}.issubset(set(sorted_rank)):
            return True
        return False
    def has_flush(self):
        self.suit_hist()
        for val in self.suits_count.values():
            if val >= 5:
                return True
        return False
    def has_full_house(self):
        return self.has_pair() and self.has_three_of_a_kind()
    def has_four_of_a_kind(self):
        return self.has_pair(i=4)
    def has_straight_flush(self):
        self.dictionary={}
        for card in self.cards:
            if card.suit not in self.dictionary:
                self.dictionary[card.suit]=[]
            self.dictionary[card.suit].append(card.rank)
        for val in self.dictionary.values():
            if len(val)>=5:
                sorted_rank=sorted(val)
                count = 0
                for i in range(len(sorted_rank) - 1):
                    if sorted_rank[i] + 1 == sorted_rank[i + 1]:
                        count += 1
                        if count == 4:
                            return True
                    else:
                        count = 0
                if {1, 2, 3, 4, 5}.issubset(set(sorted_rank)):
                    return True

        return False
    def classify(self):
        self.hand_order=[(self.has_straight_flush(),"straight_flush",8),(self.has_four_of_a_kind(),"four_of_a_kind",7),
                         (self.has_full_house(),"full_house",6),
                         (self.has_flush(),"flush",5),(self.has_straight(),"straight",4),
                         (self.has_three_of_a_kind(),"three_of_a_kind",3),
                         (self.has_two_pair(),"two_pair",2),(self.has_pair(),"has_pair",1)]
        for hand,label,rank in self.hand_order:
            if hand:
                return label,rank
        return "high_card",0
def simulate_hands(deck_obj,no_of_hands,cards_per_hand,simulations=None):
    table={}
    if 52 // no_of_hands >= cards_per_hand:
        for _ in range(simulations):
            fresh_deck=copy.deepcopy(deck_obj) # everytime we need a fresh deck
            fresh_deck.shuffle()
            for i in range(no_of_hands):
                h = PokerHand(f"{i + 1}th hand")
                fresh_deck.move_cards(h, cards_per_hand)
                label, rank = h.classify()
                """print(f"{i + 1}th hand")
                print(h)
                print("classification", label)
                print("_" * 20)"""

                table[label] = table.get(label, 0) + 1
        print(table)
        total_hands=no_of_hands*simulations
        probability={}
        for label,occurrence in table.items():
            probability[label]=occurrence/total_hands
        return probability
    else:
        print("not enough cards to deal: check again")
        return {}




if __name__ == '__main__':
    # make a deck
    deck = Deck()
    """deck.shuffle()
    poker=PokerHand()
    deck.move_cards(poker,10)
    #print(poker.sort())
    print("one pair---",poker.has_pair())
    print("two pairs---",poker.has_two_pair())
    print("three of a kind---", poker.has_three_of_a_kind())
    print("straight----",poker.has_straight())
    print("flush", poker.has_flush())
    print("full house", poker.has_full_house())
    print("four of a kind---",poker.has_four_of_a_kind())
    print("straight flush", poker.has_straight_flush())
    print(poker.classify())"""
    print(simulate_hands(deck,6,7,1000))
