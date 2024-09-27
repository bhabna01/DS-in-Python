import random
class Card:
    suits=['Hearts','Diamonds','Clubs','Spades']
    ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    def __init__(self,rank,suit):
        if rank not in Card.ranks:
            raise ValueError(f"Invalid rank:{rank}")
        if suit not in Card.suits:
            raise ValueError(f"Invalid suit:{suit}")
        self.rank=rank
        self.suit=suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return f"Card(rank={self.rank},suit={self.suit})"

class Deck:
    def __init__(self):
        self.cards=[Card(rank,suit) for suit in Card.suits for rank in Card.ranks]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        if len(self.cards)==0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()
    def deal_hand(self,hand_size):
        if hand_size>len(self.cards):
            raise ValueError("Not enough cards in the deck to deal this hand size")
        hand=[self.deal_card() for _ in range(hand_size)]
        return hand
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
    def __repr__(self):
        return f"Deck(card={self.cards})"
class WarGame:
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        self.player1_hand=self.deck.deal_hand(26)
        self.player2_hand=self.deck.deal_hand(26)
    
    def card_rank(self,card):
        return Card.ranks.index(card.rank)
    
    def play_round(self):
        if len(self.player1_hand)==0 or len(self.player2_hand)==0:
            return None,None
        card1=self.player1_hand.pop(0)
        card2=self.player2_hand.pop(0)

        print(f"Player 1 plays {card1}")
        print(f"Player 2 plays {card2}")

        if self.card_rank(card1)>self.card_rank(card2):
            print("Player 1 wins the round")
            self.player1_hand.extend([card1,card2])
        elif self.card_rank(card2)>self.card_rank(card1):
            print("Player 2 wins the round!")
            self.player2_hand.extend([card2,card1])
        else:
            print("It's a tie! War is declared")
            self.war(card1,card2)
    def war(self,card1,card2):
        if len(self.player1_hand)<4 or len(self.player2_hand)>4:
            return
        
        war_cards1=[card1]+[self.player1_hand.pop(0) for _ in range(3)]
        war_cards2=[card2]+[self.player2_hand.pop(0) for _ in range(3)]

        print(f"Player 1's war cards:{war_cards1[-1]}")
        print(f"Player 2's war cards:{war_cards2[-1]}")

        if self.card_rank(war_cards1[-1])>self.card_rank(war_cards2[-1]):
            print("Player 1 wins the war")
            self.player1_hand.extend(war_cards1+war_cards2)
        elif self.card_rank(war_cards2[-1]>self.card_rank(war_cards1[-1])):
            print("Player 2 wins the war")
            self.player2_hand.extend(war_cards1+war_cards2)
        else:
            print("War again!")
            self.war(war_cards1[-1],war_cards2[-1])
    def play_game(self):
        round_num=1
        while len(self.player1_hand)>0 and len(self.player2_hand)>0:
            print(f"\n----Round {round_num}-----")
            self.play_round()
            round_num+=1
        
        if len(self.player1_hand)>0:
            print("Player 1 wins the game!")
        else:
            print("Player 2 wins the game!")
if __name__=="__main__":
    game=WarGame()
    game.play_game()
