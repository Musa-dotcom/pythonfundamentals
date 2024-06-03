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

# Function to initialize empty piles
def initialize_piles():
    piles = {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}
    return piles

# Function to check if all cards are sorted
def all_cards_sorted(piles):
    return all(len(pile) == 13 for pile in piles.values())

# Main game loop
def play_game():
    deck = initialize_deck() 
    piles = initialize_piles()

    print("Initial deck:", deck)
    print("Initial piles:", piles) 

    # Game loop
    while not all_cards_sorted(piles):
        # Player's turn
        print("It's your turn!")

        # Prompt the player to pick a card from the deck
        picked_card = deck.pop(0)  # Remove the top card from the deck

        # Display the picked card to the player
        print("You picked:", picked_card['rank'], "of", picked_card['suit'])

        # Prompt the player to choose a pile to place the card on
        print("Choose a pile to place the card on:")
        for suit, pile_cards in piles.items():
            print(suit + ": ", pile_cards)
        chosen_pile = input("Enter the suit of the pile: ")

        # Check if the chosen pile is valid
        if chosen_pile in piles and (not piles[chosen_pile] or piles[chosen_pile][-1]['rank'] == picked_card['rank']):
            piles[chosen_pile].append(picked_card)
            print("Placed", picked_card['rank'], "of", picked_card['suit'], "on", chosen_pile)
        else:
            print("Invalid choice. Try again.")

    print("Congratulations! You have successfully sorted all the cards.")

# Start the game
play_game()
