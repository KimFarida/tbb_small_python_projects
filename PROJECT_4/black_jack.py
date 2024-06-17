#!/usr/bin/env python3

import random, sys


suits ={
    "HEARTS" : chr(9829),
    "DIAMONDS" : chr(9830),
    "SPADES" : chr(9824),
    "CLUBS": chr(9827)
}

BACKSIDE = 'backside'

def main():

    print(f"""
            Blackjack, by Al Sweigart al@inventwithpython.com

            Rules:
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.

          """)
    
    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        print(f"Money: {money}")
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print(f"Bet: {bet}")

        while True:
            displayHands(playerHand, dealerHand)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Bet increased to {bet}")
                print(f"Bet:{bet}")

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

                if move in ('S', 'D'):
                    break


        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press enter to continue...")
                print("\n\n")

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f"Dealer busts! You win ${bet}")
            money += bet
        elif playerValue > 21:
            print("You lost")
            money -= bet
        elif playerValue > dealerValue:
            print(f"You won ${bet}")
            money+= bet
        elif playerValue == dealerValue:
            print(f"It's a tie, the bet is returned to you")

        input('Press enter to continue...')
        print("\n\n")


def getBet(maxBet):
    '''
        Validates and returns bet input by player
    '''
    while True:
        print(f"How much would you like to bet? (1-{maxBet}, or QUIT)")
        bet = input("> ").upper().strip()

        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    '''
        Generates the list of cards to choose from and shiffles deck on each function call
    '''
    deck = []
    for suit in suits.values():
        for rank in range(2, 11):
            deck.append((str(rank), suit))

        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand=False):
    '''
        Shows player's and dealer's cards, defaultly set to false to hide 
        one of dealer's cards
    '''
    print()
    if showDealerHand:
        print('DEALER', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER:???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def getMove(playerHand, money):
    'Ask player for their move returns H - hit, S - stand, D - double down'
    while True:
        moves = ['(H)it', '(S)tand']

        #Player will have only two cards in deck so can doubledown
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble Down")

        movePrompt = ','.join(moves) + '>'
        move = input(movePrompt).upper()

        if move in ("H", 'S'):
            return move
        
        if move in 'D' and "(D)ouble Down" in moves:
            return move


def getHandValue(cards):
    '''
        Returns the values of players cards. Face cards worth 10, Aces worth 1, 11
    '''
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces

    #Check if you can add an ace of value 10 without busting.
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    """
        Display all cards in card list
    """
    rows = ['' for i in range(5)]

    for i, card in enumerate(cards):
        rows[0] += '___'
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += f'|{rank}  |'
            rows[2] += f'|{suit}  |'
            rows[3] += f'|_ {rank}|'

    for row in rows:
        print(row)

if __name__ == '__main__':
    main()