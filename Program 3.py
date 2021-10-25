#Drew Childs, Program 3, 10/13/19

import random


def starting_hand():
    hand = []
    while len(hand) < 3:
        temp = random.randint(1,3)
        if temp in hand:
            continue
        else:
            hand.append(temp)
    return hand


def decision(previous, chooser, other, number = 0):
    if number == 0:
        number = random.randint(1, 3)
    temp = previous[number - 1]
    previous.pop(number - 1)
    chooser.append(temp)
    return previous, chooser, other, number
    

keep_going = "y"
while keep_going == "y" or keep_going == "Y":
    current_round = 1
    print("Welcome to Card game:")
    print("Number of players is 3 and total cards for each player are 3")
    print("Lets shuffle the cards")
    print("We have 2 AI players and 1 Human player")
    hand1 = starting_hand()
    hand2 = starting_hand()
    hand3 = starting_hand()
    print("Player 1 AI Cards:", hand1)
    print("Player 2 AI Cards:", hand2)
    print("Player 3 Human Cards:", hand3)
    while True:
        print("=" * 30)
        print("Round:", current_round)
        print("=" * 30)f
        temp_tuple = decision(hand3, hand1, hand2)
        print("AI decision is:", temp_tuple[3])
        print("Player 3 cards:", temp_tuple[0])
        print("Player 1 cards:", temp_tuple[1])
        print("\nPlayer 2 cards:", temp_tuple[2])
        print("Player 3 turn\nEnter 1 for card 1\nEnter 2 for card 2\nEnter 3 for card 3")
        user_choice = int(input("Enter your choice: "))
        temp_tuple = decision(hand2, hand3, hand1, user_choice)
        print("\nPlayer 3 cards:", temp_tuple[1])
        print("player 2 cards:", temp_tuple[0])
        temp_tuple = decision(hand1, hand2, hand3)
        print("\nAI decision is:", temp_tuple[3])
        print("Player 2 cards:", temp_tuple[1])
        print("Player 1 cards:", temp_tuple[0])
        print()
        current_round += 1
        for x in range(0, 3):
            if temp_tuple[x][0] == temp_tuple[x][1] and temp_tuple[x][1] == temp_tuple[x][2] and temp_tuple[x][2] == temp_tuple[x][0]:
                print("Player%d Won!!" % (x + 1))
                break
        else:
            continue
        break
    print("Thanks for playing")
    keep_going = str(input("Do you want to play again (Y/N):\n"))
    print()
