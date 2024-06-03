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

# Function to update piles and check if a pile is sorted
def update_piles(piles, picked_card):
    suit = picked_card['suit']
    piles[suit].append(picked_card)
    piles[suit].sort(key=lambda x: x['rank'])  # Sort the pile after adding the card
    return len(piles[suit]) == 13  # Return True if the pile is sorted

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

        # Update piles and check if a pile is sorted
        if update_piles(piles, picked_card):
            print("Congratulations! You have sorted the", picked_card['suit'], "pile.")
        
        # Check if the player wants to continue
        choice = input("Do you want to pick another card? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Final piles:", piles)
    print("Congratulations! You have finished sorting all the cards.")

# Start the game
play_game()

