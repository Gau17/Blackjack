import random


def randomCardsGenerator():

    '''returns random card generated in form of tuple'''

    suits = ['Heart', 'Spade', 'Club', 'Diamond']
    num = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'King', 'Queen', 'Jack']
    return (random.choice(suits), random.choice(num))


def sumCards(a):

    '''list of cards is passed as arguments and returns sum of values on cards'''

    sum = 0
    flag = 0
    for i in a:
        if i[1] == 'King' or i[1] == 'Jack' or i[1] == 'Queen':
            sum += 10
        elif i[1] == 'Ace':
            flag = 1
            sum += 1
        else:
            sum += i[1]
    if sum < 12 and flag == 1:
        sum += 10
    return sum

def checksplit(arr):

    '''list of cards is passed as arguments and it checks whether the player can split or not'''

    global ace_flag
    if arr[0][1] == arr[1][1] and len(arr) == 2:
        if arr[0][1] == 'Ace':
            ace_flag = 1
            return 1
        else:
            return 1
    else:
        return 0

def gamePlay(p,arr):
    global ace_flag
    while (1):
        print("Your cards - " + str(arr))
        sum = sumCards(arr)
        print('Sum = ' + str(sum))
        print("Dealer's cards - [" + str(players['Dealer'][0]) + ", (X,X)]")
        if sum == 21 and len(arr) == 2 and ace_flag == 0:
            print('Blackjack. You Won!')
            bets[p] *= 2.5
            _ = input('Press Enter to continue')
            break
        elif sum == 21:
            _ = input('Press Enter to continue')
            break
        elif sum > 21:
            print('You Bust and lost the bet')
            bets[p] = 0
            _ = input('Press Enter to continue')
            break
        if checksplit(arr):
            j = input('What would you like to do:\n1.Hit\n2.Stand\n3.Doubledown\n4.Split\nEnter your choice: ')
        elif len(arr) == 2:
            j = input('What would you like to do:\n1.Hit\n2.Stand\n3.Doubledown\nEnter your choice: ')
        else:
            j = input('What would you like to do:\n1.Hit\n2.Stand\nEnter your choice: ')
        if j == '1':
            c = randomCardsGenerator()
            arr.append(c)
            print('\nYou got a', c)
            continue
        elif j == '2':
            playerSums[p] = sumCards(arr)
            break
        elif j == '3':
            bets[p] *= 2
            c = randomCardsGenerator()
            arr.append(c)
            print('\nYour bet has been doubled\nYou got a', c)
            print("Your cards - " + str(arr))
            sum = sumCards(arr)
            print('Sum = ' + str(sum))
            print("Dealer's cards - [" + str(players['Dealer'][0]) + ", (X,X)]")
            if sum == 21 and len(arr) == 2 :
                print('Blackjack. You Won!')
                bets[p] *= 2.5
            elif sum > 21:
                print('You Bust and lost the bet')
                bets[p] = 0
            else:
                playerSums[p] = sumCards(arr)
            _ = input('Press Enter to continue')
            break
        elif j == '4' and ace_flag == 0:                            
            arr1 = [arr[0],randomCardsGenerator()]
            bets[p + " Hand1"] = int(input("Place your bet for the split hand: "))
            print("\n" + p + " Hand1" + "'s turn")
            gamePlay(p + ' Hand1',arr1)
            arr2 = [arr[1],randomCardsGenerator()]
            bets[p + " Hand2"] = bets[p]
            print("\n" + p + " Hand2" + "'s turn")
            gamePlay(p + ' Hand2',arr2)
            bets.pop(p)
            break
        elif j == '4' and ace_flag == 1:            # both the cards are 'Ace' and player split
            arr1 = [arr[0], randomCardsGenerator()]
            bets[p + " Hand1"] = int(input("Place your bet for the split hand: "))
            print("\n" + p + " Hand1" + "'s turn")
            print("Your cards - " + str(arr1))
            sum = sumCards(arr1)
            print('Sum = ' + str(sum))
            print("Dealer's cards - [" + str(players['Dealer'][0]) + ", (X,X)]")
            if sum > 21:
                print('You Bust and lost the bet')
                bets[p + " Hand1"] = 0
            else:
                playerSums[p + " Hand1"] = sumCards(arr1)
            _ = input('Press Enter to continue')
            arr2 = [arr[1], randomCardsGenerator()]
            bets[p + " Hand2"] = bets[p]
            print("\n" + p + " Hand2" + "'s turn")
            print("Your cards - " + str(arr2))
            sum = sumCards(arr2)
            print('Sum = ' + str(sum))
            print("Dealer's cards - [" + str(players['Dealer'][0]) + ", (X,X)]")
            if sum > 21:
                print('You Bust and lost the bet')
                bets[p + " Hand2"] = 0
            else:
                playerSums[p + " Hand2"] = sumCards(arr2)
            ace_flag = 0
            _ = input('Press Enter to continue')
            bets.pop(p)
            break
        else:
            print('\nError. Please enter your choice again\n')


players = {'Dealer': [randomCardsGenerator(), randomCardsGenerator()]}
bets = {}
playerSums = {}
ace_flag = 0

n = int(input('Enter number of players: '))
for i in range(1, n + 1):
    players['Player' + str(i)] = [randomCardsGenerator(),randomCardsGenerator()]
print("Welcome to the game of Blackjack!")

for i in range(n):
    print("\nPlayer{}'s turn:".format(i + 1))
    bets['Player' + str(i + 1)] = float(input("Please place your bet: "))

for i in players:
    if i == 'Dealer':
        print("\n" + i + "'s cards - [" + str(players[i][0]) + ", (X,X)]")
    else:
        print(i + "'s cards - " + str(players[i]))
_ = input('Press Enter to continue')

for p in players:
    if p == 'Dealer':
        continue
    print("\n" + p + "'s turn")
    gamePlay(p,players[p])

print()
while (1):

    '''check the final sum of all cards and compares with sum of dealer's card'''

    print("Dealer's cards - " + str(players['Dealer']))
    if ((sumCards(players['Dealer'])) >= 17 and (sumCards(players['Dealer'])) <= 21):
        print('Dealer Stands')
        print('Sum =',sumCards(players['Dealer']),'\n')
        playerSums['Dealer'] = sumCards(players['Dealer'])
        for p in playerSums:
            if p == 'Dealer':
                continue
            if playerSums['Dealer'] > playerSums[p]:
                print(p + " lost the bet")
                bets[p] = 0
            elif playerSums['Dealer'] == playerSums[p]:
                print("Push for " + p)
            elif playerSums['Dealer'] < playerSums[p]:
                print(p + " wins!")
                bets[p] *= 2
        break
    elif (sumCards(players['Dealer'])) < 17:
        print('Dealer Hits')
        _ = input('Press Enter to continue')
        c = randomCardsGenerator()
        players['Dealer'].append(c)
        print('\nDealer got a', c)
        continue
    elif (sumCards(players['Dealer'])) > 21:
        print("Its a Bust!")
        for p in playerSums:
            bets[p] *= 2
        break

print('\nPlayer\t-\tFinal Amounts')
for p in bets:
    print(p,"\t-\t",bets[p])
