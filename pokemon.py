#to do: Add move pool/move learning/dynamic stats to pokemon
#to do: Add pallet town
#to do: Add battle options

from random import *
import os
import copy
from moves import *
from pokedex import *

class trainer:
    """
    creates a pokemon trainer
    """
    def __init__(self,name,pokeList): #gives the trainer a name and a list of pokemon
        self.name = name
        self.pokeList = pokeList

    def getName(self): #gets the name of the trainer
        print(self.name)

    def getFirstPoke(self): #returns the pokemon at the front of the lineup
        return self.pokeList[0]

    def addPoke(self, pokemon): #adds a new pokemon to the roster
        self.pokeList.append(pokemon)

    def showPoke(self, currentList): #prints all the pokemon in the roster
        if currentList == 0:
            currentList = self.pokeList
        i = 1
        for poke in currentList:
            print(str(i)+'.'+str(poke.name))
            i+=1

    def removePoke(self): #removes a pokemon from the roster
        print('You will have to remove a Pokemon from your party')
        options = len(self.pokeList)+1
        while True:
            print('Which pokemon would you like to remove?')
            self.showPoke()
            print(str(options)+'.Cancel')
            index = int(input())
            if index <=options:
                break
        if index == options:
            print('canceled')
        else:
            removed = self.pokeList[index-1]
            print(str(removed.name), 'will be removed from your party')
            while True:
                print('Are you sure? y/n')
                confirm = input()
                if confirm == 'y':
                    print(str(removed.name), 'was released, bye',str(removed.name)+'!')
                    removed = self.pokeList[index-1]
                    self.pokeList.remove(removed)
                    break
                elif confirm == 'n':
                    print('canceled')
                    break
                else:
                    print('Please enter \'y\' or \'n\'')
                    
    def changeOrder(self): #changes which pokemon goes first
        pokeCopy = self.pokeList[:]
        options = len(self.pokeList)
        while True:
            print('Who would you like to go first?')
            self.showPoke()
            index = int(input())
            if index <= options:
                break
        oldFirstCopy = self.pokeList[0]
        newFirstCopy = self.pokeList[index-1]
        self.pokeList.remove(oldFirstCopy)
        self.pokeList.remove(newFirstCopy)
        self.pokeList.insert(0, newFirstCopy)
        self.pokeList.append(oldFirstCopy)
        self.showPoke()

    def choosePoke(self, currentList):
        print('Who do you want to send out?')
        options = len(currentList)
        while True:
            self.showPoke(currentList)
            index = int(input())
            if index <= options:
                break
        poke = currentList[index-1]
        return poke
    
def lab():
    """
    Main game loop
    """
    playerName = input('Welcome to the world of Pokemon! First, What is your name?\n') #setup
    playerChar = trainer(playerName, [])
    gary = trainer('Gary',[])
    os.system("clear")
    print('Nice to meet you', str(playerChar.name)+'! I\'m Professor Oak, and to help you out I\'ll give you your first Pokemon!')
    while True: #first Pokemon selection
        poke = int(input('Which pokemon would you like?\n1.Squirtle\n2.Charmander\n3.Bulbasaur\n'))
        if poke == 1:
            ashSquirtle = copy.deepcopy(pokedex.squirtle)
            playerChar.addPoke(ashSquirtle)
            garyBulbasaur = copy.deepcopy(pokedex.bulbasaur)
            gary.addPoke(garyBulbasaur)
            break
        elif poke == 2:
            ashCharmander = copy.deepcopy(pokedex.charmander)
            playerChar.addPoke(ashCharmander)
            garySquirtle = copy.deepcopy(pokedex.squirtle)
            gary.addPoke(garySquirtle)
            break
        elif poke == 3:
            ashBulbasaur = copy.deepcopy(pokedex.bulbasaur)
            playerChar.addPoke(ashBulbasaur)
            garyCharmander = copy.deepcopy(pokedex.charmander)
            gary.addPoke(garyCharmander)
            break
        else:
            print('invalid choice, please enter 1 or 2')
    os.system("clear")
    if str(playerChar.pokeList[0].name) == 'Squirtle':
        print('Great choice! Squirtle is a great defensive pokemon, cute too!')
        input()
    elif str(playerChar.pokeList[0].name) == 'Bulbasaur':
        print('Great choice! Bulbasaur is a sturdy blocker! loves to bask in the sun!')
        input()
    else:
        print('Great choice! Charmander is a fiery attacker! loves to play fetch too!')
        input()
    print('Gary: Fine, then I\'ll take',str(gary.pokeList[0].name)+'!')
    input()
    print('You turn to leave the lab, but suddenly you feel Gary grab your arm')
    input()
    print('Gary: Where are you going',str(playerChar.name)+'? Dontcha wanna have your first battle?') #gary initiates first battle
    while True:
        print('1. YES!')
        print('2. No!')
        react = int(input())
        if react == 1:
            print('Gary: Alright! that\'s the spirit!, don\'t worry I won\'t gloat too much when I beat you!')
            input()
            break
        elif react == 2:
            print('Gary: Too bad!')
            print('Before you have time to react Gary throws his pokeball and gets ready to battle')
            input()
            break
        print('Please enter 1 or 2')
    os.system("clear")
    won = battle(playerChar, gary) #starts the battle
    os.system("clear")
    if won == 0:
        print('Gary: Aw shucks, you were just lucky this time! I\'m off to battle some real trainers, smell ya later!')
        input()
    else:
        print('Gary: Haha I knew it! you don\'t have what it takes! I\'m off to battle some real trainers, smell ya later!')
        input()
    for i in range(0,len(playerChar.pokeList)):
        print(playerChar.pokeList[i].level, playerChar.pokeList[i].stats)

def whoGoesFirst(playerPoke, opponentPoke):
    if playerPoke.stats['speed']>=opponentPoke.stats['speed']:
        return 0
    else:
        return 1

def playerTurn(playerPoke, opponentPoke):
    """
    defines the players turn
    """
    while True:
        print('What do you do??')
        playerPoke.getMoves()
        move = int(input())
        noMoves = len(playerPoke.moves)
        if move <= noMoves:
            break
    print(playerPoke.name, 'used', playerPoke.moves[move][1])
    playerPoke.useMove(move, opponentPoke)

def computerTurn(playerPoke, opponentPoke, opponentName):
    """
    defines the computers turn
    """
    noMoves = len(opponentPoke.moves)
    move = randint(1,noMoves)
    print(opponentName+'\'s',opponentPoke.name, 'used',opponentPoke.moves[move][1])        
    opponentPoke.useMove(move, playerPoke)

def battleDisplay(playerPoke, opponentPoke):
    """
    Will display sprites and HP bars
    """
    print(str(opponentPoke.name), 'HP:'+opponentPoke.HPBar(),str(opponentPoke.HP)+'/'+str(opponentPoke.maxHP))
    print(str(playerPoke.name),'HP:'+playerPoke.HPBar(),str(playerPoke.HP)+'/'+str(playerPoke.maxHP))

def battleRestore(player):
    for poke in player.pokeList:
        poke.statRestore()

def battle(player, opponent):
    """
    Main pokemon battle loop
    """
    playerPokesCopy = player.pokeList[:]
    opponentPokesCopy = opponent.pokeList[:]
    start = 0
    while True: #change pokemon if one faints
        if start == 0:
            playerPoke = player.getFirstPoke()
            print(str(player.name),'sent out',str(playerPoke.name))
            opponentPoke = opponent.getFirstPoke()
            print(str(opponent.name),'sent out',str(opponentPoke.name))
            start = 1
            battleDisplay(playerPoke, opponentPoke)
            input()
            os.system("clear")
        else:
            if pokeChange == 0:
                if len(playerPokesCopy) == 0:
                    won = 1
                    break
                else:
                    playerPoke = player.choosePoke(playerPokesCopy)
                    print(str(player.name),'sent out',str(playerPoke.name))
            if pokeChange == 1:
                if len(opponentPokesCopy) == 0:
                    won = 0
                    break
                else:
                    choice = randint(0, len(opponentPokesCopy)-1)
                    opponentPoke = opponentPokesCopy[choice]
                    print(str(opponent.name),'sent out',str(opponentPoke.name))
        turn = whoGoesFirst(playerPoke, opponentPoke)
        
        while True: #Current match up
            os.system("clear")
            if turn == 0: #when turn is 0 it is the player's turn
                battleDisplay(playerPoke, opponentPoke)
                playerTurn(playerPoke, opponentPoke)
                input()
                if opponentPoke.HP <= 0: #checks if a pokemon fainted
                    opponentPokesCopy.remove(opponentPoke)
                    opponentPoke.HP = 0
                    os.system("clear")
                    battleDisplay(playerPoke, opponentPoke)
                    print(str(opponent.name)+'\'s', opponentPoke.name, 'fainted!')
                    playerPoke.XPGain(opponentPoke)
                    pokeChange = 1
                    input()
                    break
            else: #when turn is not 0 it is the computer's turn
                battleDisplay(playerPoke, opponentPoke)
                computerTurn(playerPoke, opponentPoke, str(opponent.name))
                input()
                if playerPoke.HP<=0: #checks if a pokemon fainted
                    playerPokesCopy.remove(playerPoke)
                    playerPoke.HP = 0
                    os.system("clear")
                    battleDisplay(playerPoke, opponentPoke)
                    print('your', playerPoke.name, 'fainted!')
                    pokeChange = 0
                    input()
                    break
            turn = 1-turn # chane
    if won == 0:
        print('You won!')
    else:
        print('You lose!')
    battleRestore(player)
    return won

#print(lab()) #runs the game

ashPidgey = copy.deepcopy(pokedex.pidgey)
garyPidgey = copy.deepcopy(pokedex.pidgey)
ashBulbasaur = copy.deepcopy(pokedex.bulbasaur)
garyBulbasaur = copy.deepcopy(pokedex.bulbasaur)
ashSquirtle = copy.deepcopy(pokedex.squirtle)
garyCharmander = copy.deepcopy(pokedex.charmander)

ash = trainer('ash', [ashSquirtle, ashPidgey, ashBulbasaur])
gary = trainer('gary', [garyBulbasaur, garyCharmander, garyPidgey])

print(battle(ash, gary))
