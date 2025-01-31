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
card1=Card(2,11)
card2=Card(3,12)
#print(type(Card))
#print(type(card1))
#print(card1<card2)
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
class Hand(Deck):
    def __init__(self,label=""):
        self.cards=[]
        self.label=label
hand=Hand("new hand")
#print(hand)
#print(hand.cards)
#print(hand.label)

deck=Deck()
deck.shuffle()
deck.move_cards(hand,5)
"""print("Deck cards")
print(deck)
print("Cards in hand")
print(hand)"""
"""print(len(Deck.mro()))
print(len(Hand.mro()))
print(len(Card.mro()))"""
def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
hand=Hand()
p=find_defining_class(deck,"move_cards")
print(p)
#card=deck.pop_card()
#print(card)
#hand.add_card(card)
#print(hand)
#print(deck)
deck.sort()
#print("\n sorted",deck)

class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return f"Time is {self.hour:02}:{self.minute:02}:{self.second:02}"
    def __lt__(self, other):
        t1=self.hour,self.minute,self.second
        t2=other.hour,other.minute,other.second
        return t1<t2
time1=Time(1,30,42)
time2=Time(2,30,42)
#print(time1<time2)

p=["Dear,","Scarlett","i love u"]
#print("\n".join(p))
#print(p.pop())
#print(p)
