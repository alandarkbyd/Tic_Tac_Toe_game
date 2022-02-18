values = [" " for x in range(9)]
values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
values_index = []
player1 = []
player2 = []
by = ''
pla1inp = 0
play1Sc = 0
play2Sc = 0
name1 = ''
name2 = ''
aa = 'no'  # already assigned
ndam = 'yes'  # second assignment
ntvld1 = ''
ntvld2 = ''
tempwin = ''
tempPlayer = ''

def form_indicate(vg):
    print()
    print('        |        |')
    print('        |        |')
    print(f'    {vg[0]}   |   {vg[1]}    |   {vg[2]}    ')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {vg[3]}   |   {vg[4]}    |   {vg[5]}    ')
    print('        |        |')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {vg[6]}   |   {vg[7]}    |   {vg[8]}    ')
    print('        |        |')
    print()


def form(gameindex):
    print()
    print('        |        |')
    print('        |        |')
    print(f'    {gameindex[0]}   |   {gameindex[1]}    |   {gameindex[2]}    ')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {gameindex[3]}   |   {gameindex[4]}    |   {gameindex[5]}    ')
    print('        |        |')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {gameindex[6]}   |   {gameindex[7]}    |   {gameindex[8]}    ')
    print('        |        |')
    print()


possibleV = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def beginning():
    if ttp > 1:
        print(f"""{name1.upper()}, Choose your character as Player 1:
            1. X
            2. O""")
    else:
        print(f"""Choose your character as Player 1:
            1. X
            2. O""")
    cinp = input('Your Choice: ')
    while cinp != 1 or cinp != 2:
        try:
            cinp = int(cinp)
            if cinp == 1:
                return 'X'
            elif cinp == 2:
                return 'O'
            else:
                print(f'{cinp} is not a valid input')
                cinp = input('Your Choice: ')
                # raise Exception('Invalid Number!')
        except ValueError:
            print(f'{cinp} is not a valid input!')
            cinp = input('Your Choice: ')


# def scoreboard():
#     global play1Sc, play2Sc, uc
#     nuc = 0
#     npc = 2
#     print('----------------------------------------------')
#     print('SCOREBOARD'.center(46, ' '))
#     print('----------------------------------------------')
#     if uc == 'X':
#         nuc = 1
#         print(f'Player{nuc} \'X\':    {play1Sc}')
#         print(f'Player{npc} \'O\':    {play2Sc}')
#
#     elif uc == 'O':
#         npc = 1
#         nuc = 2
#         print(f'Player{npc} \'O\': ')
#         print(f'Player{nuc} \'X\': ')


def scoreboard():
    print('----------------------------------------------')
    print('SCOREBOARD'.center(46, ' '))
    print('----------------------------------------------')
    print(f'{name1.upper()} :     {play1Sc}')
    print(f'{name2.upper()} :     {play2Sc}')


def updateScore():
    pass


def checkMatchPlay1(ch=2):
    global play1Sc, play2Sc, aa, ttp, tempPlayer
    co = 0
    if ' ' not in values:
        print('It\'s a draw!')
        return False
    for li in possibleV:
        for k in range(3):
            if li[k] in player1:
                co += 1
                if co == 3:
                    tempPlayer = name1.upper()
                    if tempPlayer == name1.upper():
                        play2Sc += 1
                        tempPlayer = name2.upper()
                    # else:
                        # play2Sc += 1
                    if ttpBey == 1:
                        print(f'Player{ch} \'X\' win')
                    else:
                        print(f'{tempPlayer} win')
                        aa = 'no'


                    return False
        else:
            co = 0
    return True


def checkMatchPlay2(ch=1):
    global play1Sc, play2Sc, aa, ttp, tempPlayer
    co = 0
    if ' ' not in values:
        print('It\'s a draw!')
        return False
    for li in possibleV:
        for k in range(3):
            if li[k] in player2:
                co += 1
                if co == 3:
                    tempPlayer = name2.upper()
                    if tempPlayer == name2.upper():
                        play1Sc += 1
                        tempPlayer = name1.upper()
                    # else:
                    #     play1Sc += 1
                    if ttpBey == 1:
                        print(f'Player{ch} \'O\' win')
                    else:
                        print(f'{tempPlayer} win')
                        aa = 'no'



                    return False
        else:
            co = 0
    return True


def gameProcessPlayer1(ch='1'):
    global values_index, by, aa, ttp, ntvld1, pla1inp
    if ttpBey > 1:
        ttp += 1
    if ttp == 1:
        pla1inp = input(f'Player{ch} \'X\': ')
    elif ttp > 1 or ttpBey > 1:
        if aa == 'yes':
            pla1inp = input(f'{name2.upper()} \'X\': ')
            aa = 'no'
            ttp -= 1
            ntvld1 = name2.upper()
        else:
            pla1inp = input(f'{name1.upper()} \'X\': ')
            aa = 'yes'
            ttp -= 1
            ntvld1 = name1.upper()

    try:
        pla1inp = int(pla1inp)
        if ttp == 1:
            if (pla1inp - 1) in values_index:
                if (pla1inp - 1) in player1:
                    by = 'you'
                else:
                    by = 'player2'
                print(f'Sorry, place is already reserved by {by}!')
                pla1inp = int(input(f'Player{ch} \'X\': '))
        elif ttp > 1 or ttpBey > 1:
            if (pla1inp - 1) in values_index:
                if (pla1inp - 1) in player1:
                    by = 'you'
                else:
                    by = ntvld1
                print(f'Sorry, place is already reserved by {by}!')
                pla1inp = int(input(f'Player{ch} \'X\': '))

        while (pla1inp - 1) not in player1:
            if (values[pla1inp - 1] == ' ') and ((pla1inp - 1) not in values_index):
                values.pop(pla1inp - 1)
                values.insert(pla1inp - 1, 'X')
                player1.append(pla1inp - 1)
                values_index.append(pla1inp - 1)

            else:
                if (pla1inp - 1) in player1:
                    by = 'you'
                else:
                    by = ntvld1
                print(f'Sorry, place is already reserved by {by}!')
                pla1inp = int(input(f'Player1 \'X\': '))

        form(values)

    except IndexError:
        print(f'Error: Index {pla1inp} is out of range!')
        gameProcessPlayer1()
    except ValueError:
        print(f'Error: {pla1inp} is not a number!')
        if aa == 'yes':
            aa = 'no'
        elif aa == 'no':
            aa = 'yes'
        gameProcessPlayer1()


def gameProcessPlayer2(ch='2'):
    global values_index, by, aa, ttp, ttpBey
    pla2inp = ''
    if ttpBey > 1:
        ttp += 1
    if ttp > 1 or ttpBey > 1:
        if aa == 'yes':
            pla2inp = input(f'{name2.upper()} \'O\': ')
            aa = 'no'
            ttp -= 1
        else:
            pla2inp = input(f'{name1.upper()} \'O\': ')
            aa = 'yes'
            ttp -= 1

    elif ttp == 1:
        pla2inp = input(f'Player{ch} \'O\': ')
    try:
        pla2inp = int(pla2inp)
        if (pla2inp - 1) in values_index:
            if (pla2inp - 1) in player2:
                by = 'you'
            else:
                by = 'player1'
            print(f'Sorry, place is already reserved by {by}!')
            pla2inp = int(input(f'Player{ch} \'O\': '))
        elif ttp > 1 or ttpBey > 1:
            if (pla2inp - 1) in values_index:
                if (pla2inp - 1) in player2:
                    by = 'you'
                else:
                    by = name1
                print(f'Sorry, place is already reserved by {by}!')
                pla2inp = int(input(f'Player{ch} \'O\': '))

        while (pla2inp - 1) not in player2:
            if (values[pla2inp - 1] == ' ') and ((pla2inp - 1) not in values_index):
                values.pop(pla2inp - 1)
                values.insert(pla2inp - 1, 'O')
                player2.append(pla2inp - 1)
                values_index.append((pla2inp - 1))

            else:
                if (pla2inp - 1) in player2:
                    by = 'you'
                else:
                    by = 'player1'
                print(f'Sorry, place is already reserved by {by}!')
                pla2inp = int(input(f'Player2 \'O\': '))
        form(values)

    except IndexError:
        print(f'Error: Index {pla2inp} is out of range!')
        gameProcessPlayer2()
    except ValueError:
        print(f'Error: {pla2inp} is not a number!')
        if aa == 'yes':
            aa = 'no'
        elif aa == 'no':
            aa = 'yes'
        gameProcessPlayer2()


run = True
ttp = 1 # int(input('Times to play: '))
ttpBey = ttp
# uc = beginning()
uc = ''
if ttp > 1:
    name1 = input('Name of player 1: ')
    tempPlayer = name1
    name2 = input('Name of player 2: ')
    scoreboard()
    uc = beginning()
    form_indicate(values_guide)
elif ttp == 1:
    uc = beginning()
    form_indicate(values_guide)

while ttp > 0:
    if uc == 'X':
        gameProcessPlayer1()
        if not checkMatchPlay1(1):
            # play1Sc += 1
            ttp -= 1
            values = [" " for x in range(9)]
            values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            values_index = []
            player1 = []
            player2 = []
            by = ''
            tempPlayer = 1
            if ttp > 0:
                scoreboard()
                uc = beginning()
                form_indicate(values_guide)
                continue
            else:
                break
            # run = False
            # break

        gameProcessPlayer2()
        if not checkMatchPlay2(2):
            # play2Sc += 1
            ttp -= 1
            values = [" " for x in range(9)]
            values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            values_index = []
            player1 = []
            player2 = []
            by = ''
            tempPlayer = 1
            if ttp > 0:
                scoreboard()
                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False
    elif uc == 'O':
        gameProcessPlayer2('1')
        # play2Sc += 1
        if not checkMatchPlay2():
            ttp -= 1
            values = [" " for x in range(9)]
            values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            values_index = []
            player1 = []
            player2 = []
            by = ''
            tempPlayer = 1
            if ttp > 0:
                scoreboard()
                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False
            # break

        gameProcessPlayer1('2')
        if not checkMatchPlay1():
            # play1Sc += 1
            ttp -= 1
            values = [" " for x in range(9)]
            values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            values_index = []
            player1 = []
            player2 = []
            by = ''
            tempPlayer = ''
            if ttp > 0:
                scoreboard()
                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False
# scoreboard()
							
'''if play1Sc > play2Sc:
    print(f'{name1.upper()} has won this match')
elif play2Sc > play1Sc:
    print(f'{name2.upper()} has won this match')'''
