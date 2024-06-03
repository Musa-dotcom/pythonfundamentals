import random

# Function to initialize and shuffle the deck of cards
def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    # Create a list to hold the deck of cards
    deck = []
    
    # Populate the deck with all 52 cards
    for suit in suits:
        for rank in ranks:
            card = {'rank': rank, 'suit': suit}
            deck.append(card)
    
    # Shuffle the deck randomly
    random.shuffle(deck)
    
    return deck

"""# Example usage:
deck = initialize_deck()
print(deck)  # Print the shuffled deck""" 

# Function to initialize empty piles
def initialize_piles():
    piles = {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}
    return piles

deck = initialize_deck() 
piles = initialize_piles()

""" print("Initial deck: \n", deck)
print("Initial pile: \n", piles)  """

# Assuming 'deck' is the shuffled deck of cards and 'piles' is the dictionary representing the piles

# Game loop
while True:
    # Player's turn
    print("It's your turn!\n")

    # Prompt the player to pick a card from the deck
    picked_card = deck.pop(0)  # Remove the top card from the deck

    # Display the picked card to the player
    print("You picked:", picked_card['rank'], "of", picked_card['suit'])

    # Function to handle the player's action of placing the picked card onto the piles
    def place_card_on_pile(picked_card, piles):
        suit = picked_card['suit']
        rank = picked_card['rank']

        # Iterate through each pile
        for pile_suit, pile_cards in piles.items():
            # Check if the picked card's suit matches the current pile's suit
            if suit == pile_suit:
                if len(pile_cards) == 0:
                    # If the pile is empty, add the picked card to it
                    pile_cards.append(rank)
                    print("Placed", rank, "of", suit, "on", pile_suit) 
                    # Sort the cards in the pile
                    pile_cards.sort()
                    return True
                else:
                    if rank == 'A':
                        # If the picked card is an Ace, place it on the pile regardless of other cards
                        pile_cards.append(rank)
                        print("Placed", rank, "of", suit, "on", pile_suit)
                        # Sort the cards in the pile
                        pile_cards.sort()
                        return True
                    else:
                        # Check if there are other cards in the pile
                        if pile_cards:
                            top_card_rank = pile_cards[-1]
                            if rank == 'K' and top_card_rank == 'A':
                                pile_cards.append(rank)
                                print("Placed", rank, "of", suit, "on", pile_suit)
                                # Sort the cards in the pile
                                pile_cards.sort()
                                return True
                            elif rank == str(int(top_card_rank) + 1):
                            # If the picked card's rank is one higher than the top card of the pile, add it to the pile
                                pile_cards.append(rank)
                                print("Placed", rank, "of", suit, "on", pile_suit)
                                # Sort the cards in the pile
                                pile_cards.sort()
                                return True
                            else:
                                # If the picked card cannot be placed on this pile, continue to the next pile
                                continue
                        else:
                            # If the pile is empty and the picked card is not an Ace, it cannot be placed on this pile
                            print("Cannot place", rank, "of", suit, "on", pile_suit + ". The pile is empty.\n")
                            return False

        # If the picked card cannot be placed on any pile, return False
        print("Cannot place", rank, "of", suit, "on any pile.\n")
        return False
    
    #usage:
    print("You picked:", picked_card['rank'], "of", picked_card['suit'])
    place_card_on_pile(picked_card, piles)

    play_again = input("Do you want to continue playing? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break  # Exit the game loop if the player chooses not to continue.
     