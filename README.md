# Introduction:
This is a simple blackjack program built using Python. The game can be played by any number of players.
# How to use:
- Run the blackjack.py file. The program will first prompt the user to enter the number of players. 
- It will then prompt each player to enter his/her bet. Then it displays each player’s hand and one of the dealer’s cards. 
- Then it will prompt each user choose to Hit, Stand, Doubledown(in first turn) or Split ( if the user has a pair of cards).
- Enter 1, 2, 3, or 4 to Hit, Stand, Doubledown or Split respectively. After each players’s turn, the program displays dealer’s cards. 
- At the end, it displays the results and each player’s final amount.
# Softwares Used:
- Python 3.7.3
- Pycharm IDE
# Sample Results:

Enter number of players: 3

Welcome to the game of Blackjack!

Player1's turn:

Please place your bet: 100

Player2's turn:

Please place your bet: 150

Player3's turn:

Please place your bet: 80

Dealer's cards - [('Diamond', 2), (X,X)]

Player1's cards - [('Club', 'King'), ('Spade', 'Queen')] 

Player2's cards - [('Spade', 9), ('Spade', 2)] 

Player3's cards - [('Heart', 2), ('Spade', 3)]

Press Enter to continue

Player1's turn

Your cards - [('Club', 'King'), ('Spade', 'Queen')] 

Sum = 20

Dealer's cards - [('Diamond', 2), (X,X)] 

What would you like to do:

1.Hit

2.Stand

3.Doubledown 

Enter your choice: 2

Player2's turn

Your cards - [('Spade', 9), ('Spade', 2)] 

Sum = 11

Dealer's cards - [('Diamond', 2), (X,X)] 

What would you like to do:

1.Hit

2.Stand

3.Doubledown

Enter your choice: 3

Your bet has been doubled

You got a ('Club', 8)

Your cards - [('Spade', 9), ('Spade', 2), ('Club', 8)] 

Sum = 19

Dealer's cards - [('Diamond', 2), (X,X)]

Press Enter to continue

Player3's turn

Your cards - [('Heart', 2), ('Spade', 3)] 

Sum = 5

Dealer's cards - [('Diamond', 2), (X,X)] 

What would you like to do:

1.Hit

2.Stand

3.Doubledown

Enter your choice: 1

You got a ('Heart', 'Ace')

Your cards - [('Heart', 2), ('Spade', 3), ('Heart', 'Ace')] 

Sum = 16

Dealer's cards - [('Diamond', 2), (X,X)]

What would you like to do:

1.Hit

2.Stand

Enter your choice: 1

You got a ('Spade', 9)

Your cards - [('Heart', 2), ('Spade', 3), ('Heart', 'Ace'), ('Spade', 9)] 

Sum = 15

Dealer's cards - [('Diamond', 2), (X,X)]

What would you like to do:

1.Hit

2.Stand

Enter your choice: 1

You got a ('Diamond', 4)

Your cards - [('Heart', 2), ('Spade', 3), ('Heart', 'Ace'), ('Spade', 9), ('Diamond', 4)] 

Sum = 19

Dealer's cards - [('Diamond', 2), (X,X)]

What would you like to do:

1.Hit

2.Stand

Enter your choice: 2

Dealer's cards - [('Diamond', 2), ('Spade', 10)] 

Dealer Hits

Press Enter to continue

Dealer got a ('Diamond', 5)

Dealer's cards - [('Diamond', 2), ('Spade', 10), ('Diamond', 5)] 

Dealer Stands

Sum = 17

Player1 wins! 

Player2 wins! 

Player3 wins!

Player - Final Amounts

Player1 - 200.0

Player2 - 600.0

Player3 - 160.0
