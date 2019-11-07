
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Jack', 'Queen', 'King', 'Ace')
values =  {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


# In[2]:


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[3]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# In[4]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21:
            if self.aces > 0:
                self.value -= 10
                self.aces -= 1


# In[5]:


class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# In[6]:


def  take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except ValueError:
            print("Error! Please enter a number!")
        else:
            if chips.bet > chips.total:
                while chips.bet > chips.total:
                    chips.bet = int(input("You only have " + str(chips.total) + " chips available. Please try again: "))
            else:
                break


# In[7]:


def hit(deck,hand):
    draw = deck.deal()
    print("---------------")
    print("Drew " + str(draw))
    hand.add_card(draw)
    hand.adjust_for_ace()
    print(hand.value)


# In[8]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        b = input("What would you like to do? 'H' to hit or 'S' to Stand.")
        while b.lower() != 'h' and b.lower() != 's':
            b = input("Error! Please enter 'H' to hit or 'S' to Stand.")
        
        if b == 'h':
            hit(deck, hand)
        else:
            print("Player stands. Dealer plays.")
            playing = False
        break


# In[9]:


from IPython.display import clear_output

def show_some(player,dealer):
    print("---------------")
    print("Dealer's Hand:")
    print(dealer.cards[0]) 
    print('??? of ???\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)
    
    
def show_all(player,dealer):
    print("Dealer's Hand:")
    for dcard in dealer.cards:
        print(dcard)    
    print("Player's Hand:")
    for pcard in player.cards:
        print(pcard)
    print("")


# In[10]:


def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Player and Dealer Tie! It's a push!")


# In[ ]:


from IPython.display import clear_output

# Print an opening statement# Print 
print("Welcome to GAO Casino! You have been given $100 in chips to play!")
print("Dealer plays to 17.")

playing = True

while True:
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())    
            
    # Set up the Player's chips
    chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            print("bust")
            player_busts(chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value <= 17:
            hit(deck, dealer)
        
        print("Dealer Done")
        print()
        
        # Show all cards
        show_all(player, dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(chips)

        elif dealer.value > player.value:
            dealer_wins(chips)

        elif dealer.value < player.value:
            player_wins(chips)

        else:
            push()  
    
    # Inform Player of their chips total 
    print("---------------")
    print("You have " + str(chips.total) + " chips remaining.")
    
    # Ask to play again
    again = input("Would you like to play again? 'Y' for Yes or 'N' for No.")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Error! Please enter 'Y' for Yes or 'N' for No.")
    
    if again == 'n':
        playing = False
        print("Bye!")
        break

