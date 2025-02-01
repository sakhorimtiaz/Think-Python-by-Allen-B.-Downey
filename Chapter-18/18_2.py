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
    def pop_card(self):
        return self.cards.pop()
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,no_of_hands, cards_per_hand):
        if 52 // no_of_hands >= cards_per_hand:
            self.shuffle()
            hands=[]
            for i in range(no_of_hands):
                h = Hand(f"{i + 1}th hand")
                self.move_cards(h, cards_per_hand)
                hands.append(h)
            return hands
        else:
            print("not enough cards to deal: check again")
            return []
class Hand(Deck):
    def __init__(self,label=""):
        self.cards=[]
        self.label=label

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

deck = Deck()
hands=deck.deal_hands(5,13)

for hand in hands:
    print(hand)
    print("..........")
