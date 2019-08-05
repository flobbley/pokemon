#to do: Add move pool

from random import *
import os
import copy
import pickle
from moves import *
from pokedex import *
from items import *
global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"
    
class trainer:
    """
    creates a pokemon trainer
    """
    def __init__(self,name,pokeList, itemList, money): #gives the trainer a name and a list of pokemon
        self.name = name
        self.pokeList = pokeList
        self.itemList = itemList
        self.money = money
        self.playerDex = {}
        self.badges = []
        self.boxList = []

    def getName(self): #gets the name of the trainer
        print(self.name)

    def getFirstPoke(self): #returns the pokemon at the front of the lineup
        for poke in self.pokeList:
            if poke.HP > 0:
                return poke
                break

    def addPoke(self, pokemon): #adds a new pokemon to the roster
        if len(self.pokeList) <6:
            self.pokeList.append(pokemon)
        else:
            print('No room left in the party,',pokemon.name,'was sent to the PC!')
            self.boxList.append(pokemon)
        if pokemon.pokeNum not in self.playerDex:
            print(pokemon.name+'\'s information was added to your pokedex!')
            self.playerDex[pokemon.pokeNum] = [pokemon.name, pokemon.entry]
            print(pokemon.entry)
            input()
            

    def showPoke(self, currentList): #prints all the pokemon in the roster
        if currentList == 0:
            currentList = self.pokeList
        i = 1
        for poke in currentList:
            print(str(i)+'.'+str(poke.name))
            i+=1

    def removePoke(self): #removes a pokemon from the roster
        if len(self.pokeList) == 1:
            print('You can\'t release your last pokemon!')
        else:
            options = len(self.pokeList)+1
            while True:
                print('Which pokemon would you like to remove?')
                self.showPoke(self.pokeList)
                print(str(options)+'.Cancel')
                index = input()
                if menuValid(index, options):
                    index = int(index)
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
            self.showPoke(self.pokeList)
            index = int(input())
            if index <= options:
                break
        if index != 1:
            oldFirstCopy = self.pokeList[0]
            newFirstCopy = self.pokeList[index-1]
            self.pokeList.remove(oldFirstCopy)
            self.pokeList.remove(newFirstCopy)
            self.pokeList.insert(0, newFirstCopy)
            self.pokeList.append(oldFirstCopy)
            self.showPoke(self.pokeList)
        else:
            print('No changes made')

    def choosePoke(self, currentList):
        options = len(currentList)
        while True:
            self.showPoke(currentList)
            index = input()
            if menuValid(index, options):
                index = int(index)
                break
        poke = currentList[index-1]
        return poke

    def checkDex(self):
        while True:
            while True:
                os.system(clearVar)
                print('Which entry would you like to check?')
                for pokeNum in self.playerDex:  
                    print(str(pokeNum)+'.', self.playerDex[pokeNum][0])
                print('0. cancel')
                poke = input()
                try:
                    poke = int(poke)
                    if poke != 0 and poke in self.playerDex:
                        print(self.playerDex[poke][1])
                        input()
                        break
                    else:
                        break
                except ValueError:
                    print('Invalid entry')
            if poke == 0:
                break
            
    def getItem(self, item, number):
        if item in itemList:
            itemList[item] += number
        else:
            itemList[item] = number

    def catchPoke(self, opponentPoke):
        catchRate = (opponentPoke.maxHP/opponentPoke.HP)*18
        didCatch = randint(1,100)
        if didCatch <= catchRate:
            print(opponentPoke.name,'was caught!')
            self.addPoke(opponentPoke)
            return True
        else:
            print('it broke free!')
            input()
            return False

    def useItem(self):
        if len(self.itemList)==0:
            print('You don\'t have any items!')
            input()
        else:
            items = []
            for item in self.itemList:
                items.append(item[0])
            items.append('cancel')
            while True:
                action = menuSelect('Which item would you like to use?', items)
                if action == len(items):
                    print('Canceled')
                    input()
                    return None
                else:
                    return self.itemList[action-1][0]

    def partyHeal(self):
        for poke in self.pokeList:
            poke.heal(1000)
            
    def usePC(self):
        while True:
            os.system(clearVar)
            print('Accessed the pokemon PC!')
            action = menuSelect('What would you like to do?', ['Deposit pokemon','Withdraw pokemon','Cancel'])
            if action == 1:
                if len(self.pokeList)==1:
                    print('Can\'t deposit your last pokemon!')
                    input()
                else:
                    pokes = []
                    for poke in self.pokeList:
                        pokes.append(poke.name+' '+str(poke.level))
                    pokes.append('Cancel')
                    deposit = menuSelect('Which pokemon would you like to deposit?', pokes)
                    if deposit !=  len(pokes):
                        print(self.pokeList[deposit-1].name, 'was deposited!')
                        input()
                        self.boxList.append(self.pokeList[deposit-1])
                        self.pokeList.remove(self.pokeList[deposit-1])
            elif action == 2:
                if len(self.pokeList) == 6:
                    print('Can\'t withdraw more than 6 pokemon, deposit pokemon first')
                    input()
                else:
                    pokes = []
                    for poke in self.boxList:
                        pokes.append(poke.name)
                    pokes.append('Cancel')
                    withdraw = menuSelect('Which pokemon would you like to withdraw?', pokes)
                    if withdraw != len(pokes):
                        print(self.boxList[withdraw-1].name,'was withdrawn!')
                        input()
                        self.pokeList.append(self.boxList[withdraw-1])
                        self.boxList.remove(self.boxList[withdraw-1])
            else:
                break

class summary:
    """
    summary class for save/load
    """
    def __init__(self):
        self.playerSave = 0
        self.lastPokecenter = 0

gameState = summary() #creates the save/load info
        
def main(startModule, modules):
    """
    runs the game
    """
    os.system(clearVar)
    action = menuSelect('Pokemon!',['New Game','Load'])
    if action == 1: #Start new game
        playerName = input('Welcome to the world of Pokemon! First, What is your name?\n')
        player = trainer(playerName, [], [], 500) #creates player
        gameState.playerSave = player #adds player to save/load game state
        print('Welcome', player.name+'! your pokemon adventure begins today!')
        input()
        module = startModule(player) #starts the game
    else:
        oldGameState = saveLoad('load','')
        gameState.playerSave = oldGameState.playerSave
        gameState.lastPokecenter = oldGameState.lastPokecenter
        player = gameState.playerSave #loads player save into the game player
        module = modules[gameState.lastPokecenter] #finds the saved in game location
        module = module(player) #runs the in game location
    while True:
        module = modules[module] #finds the next module to run
        module = module(player) #runs the next module
        
def test():
    action = int(input('enter action\n'))
    if action == 1:
        print(gameState.playerSave)
    elif action == 2:
        print(gameState.lastPokecenter)
    else:
        gameState.playerSave = 'ash'
        gameState.lastPokecenter = 'palletTown'

def saveLoad(which, summary):
    if which == 'save':
        with open('savefile','wb') as f:
            pickle.dump(summary,f,protocol = 2)
    else:
        with open('savefile','rb') as f:
            summary = pickle.load(f)
            return summary
    
def menu(player):
    while True:
        os.system(clearVar)
        print('MENU')
        print('1. Pokemon\n2. Pokedex\n3. Items\n4. Save\n5. Exit')
        action = input()
        if menuValid(action, 5):
            action = int(action)
            if action == 1:
                for poke in player.pokeList:
                    print(poke.name, poke.level)
                    print(poke.HPBar())
                while True:
                    action2 = menuSelect('What would you like to do?',['Check pokemon','Change order','Cancel'])
                    if action2 == 1:
                        checkPoke = []
                        for poke in player.pokeList:
                            checkPoke.append(poke.name)
                        checkPoke.append('Cancel')
                        action3  = menuSelect('Which pokemon?',checkPoke)
                        poke = player.pokeList[action3-1]
                        print(poke.name,poke.level)
                        print(poke.stats)
                        print(str(poke.gainedXP)+'/'+str(poke.needXP))
                        input()
                        break
                    elif action2 == 2:
                        player.changeOrder()
                    else:
                        break
            elif action == 2:
                player.checkDex()
            elif action == 3:
                item = player.useItem()
                print(item)
                if item == 'Pokeball':
                    print('can\'t use that outside of battle!')
                    input()
                elif item == 'Potion':
                    print('Who do you want to use it on?')
                    poke = player.choosePoke(player.pokeList)
                    potion(player, poke)
                else:
                    print()                       
            elif action == 4:
                saveLoad('save',gameState)
                print('Game saved!')
                input()
            else:
                break

def menuSelect(ask, options):
    while True:
        print(ask)
        i = 1
        for option in options:
            print(str(i)+'.',option)
            i+=1
        action = input()
        if menuValid(action, len(options)):
            action = int(action)
            return action

def pokeCenter(player):
    os.system(clearVar)
    while True: 
        print('Welcome to the pokemon center!')
        act = menuSelect('What would you like to do?',['Heal pokemon', 'Use PC', 'Cancel'])   
        if act == 1:
            player.partyHeal()
            print('Your pokemon are all at full health, we hope to see you again!')
            input()
            break
        elif act == 2:
            player.usePC()
            break
        else:
            print('Have a great day!')
            break


def menuValid(number, maxNum):
    noGood = 'invalid input'
    try:
        number = int(number)
        if number <= maxNum and number >0:
            return True
        else:
            print(noGood)
            return False
    except ValueError:
        print(noGood)

def battleDisplay(playerPoke, opponentPoke):
    """
    Will display sprites and HP bars
    """
    print(str(opponentPoke.name),str(opponentPoke.level), 'HP:'+opponentPoke.HPBar(),str(opponentPoke.HP)+'/'+str(opponentPoke.maxHP))
    print(str(playerPoke.name),str(playerPoke.level), 'HP:'+playerPoke.HPBar(),str(playerPoke.HP)+'/'+str(playerPoke.maxHP))

def battleRestore(player):
    for poke in player.pokeList:
        poke.statRestore()

def battleMenu():
    while True:
        print('What would you like to do?')
        print('1. Attack  2. Change Poke')
        print('3. Item    4. Run Away')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            return action
        
def playerTurn(playerPoke, opponentPoke):
    """
    defines the players turn
    """
    act = playerPoke.statusAction(opponentPoke, 'during')
    if act:
        while True:
            playerPoke.getMoves()
            move = input()
            noMoves = len(playerPoke.moves)+1
            if menuValid(move, noMoves):
                move = int(move)
                break
        if move == noMoves:
            return False
        else:
            return playerPoke.moves[move]
        
    
def computerTurn(playerPoke, opponentPoke, opponentName):
    """
    defines the computers turn
    """
    act = opponentPoke.statusAction(playerPoke, 'during')
    if act:
        noMoves = len(opponentPoke.moves)
        move = randint(1,noMoves)
        return opponentPoke.moves[move]        

def battle(player, opponent, wild= True):
    """
    Main pokemon battle loop
    """
    playerPokesCopy = player.pokeList[:]
    for poke in playerPokesCopy:
        if poke.HP == 0:
            playerPokesCopy.remove(poke)
    opponentPokesCopy = opponent.pokeList[:]
    start = 0
    won = 5
    if wild == False:
        print(opponent.name,'wants to battle!')
    else:
        print('A wild',opponent.pokeList[0].name,'appeared!')
    input()
    while True: #change pokemon if one faints
        if won == True or won == False:
            break
        if start == 0:
            playerPoke = player.getFirstPoke()
            print(str(player.name),'sent out',str(playerPoke.name))
            opponentPoke = opponent.getFirstPoke()
            if wild == False:
                print(str(opponent.name),'sent out',str(opponentPoke.name))
            start = 1
            battleDisplay(playerPoke, opponentPoke)
            input()
            while True: #Current match up          
                os.system(clearVar)
                battleDisplay(playerPoke, opponentPoke)
                notUsed = playerPoke.statusAction(opponentPoke, 'before')
                while True:
                    """
                    player selects their action for the turn
                    """
                    action = battleMenu()
                    if action == 1:
                        playerMove = playerTurn(playerPoke, opponentPoke)
                        if playerMove != False:
                            break
                    elif action == 2:
                        print('Who do you want to send out?')
                        oldPlayerPoke = playerPoke
                        playerPoke = player.choosePoke(playerPokesCopy)
                        playerMove = False
                        if oldPlayerPoke == playerPoke:
                            print(playerPoke.name,'is already out!')
                        else:
                            break
                    elif action == 3:
                        item = player.useItem()
                        playerMove = False
                        if item == 'Potion':
                            print(player.name,'used a potion on',playerPoke.name+'!')
                            potion(player, playerPoke)
                            break
                        elif item == 'Pokeball':
                            if wild == True:
                                catch = pokeball(player, opponentPoke)
                                if catch == True:
                                    opponentPokesCopy = []
                                    won = True
                                break
                            else:
                                print('You can\'t try to catch an opposing trainer\'s pokemon!')
                        
                    else:
                        if wild == False:
                            print('can\'t run from a trainer battle!')
                        else:
                            succeed = randint(0,1)
                            if succeed == 0:
                                print('You got away safely!')
                                opponentPokesCopy = []
                                won = True
                                break
                            else:
                                print('You couldn\'t get away!')
                                playerMove = False
                                break
                if won == True:
                    break
                    
                """
                Computer selects their action for the turn
                """
                notUsed = opponentPoke.statusAction(playerPoke, 'before')
                computerMove = computerTurn(playerPoke, opponentPoke, str(opponent.name))

                """
                resolve turn order
                """
                compskip = False
                playerskip = False
                turn = 0
                if playerMove != False:
                    turn = playerMove.priority - computerMove.priority
                else:
                    playerskip = True
                if turn == 0:
                    turn = playerPoke.tempStats['speed'] - opponentPoke.tempStats['speed']
                if turn >= 0:
                    """
                    player goes first
                    """
                    if playerskip == False:
                        playerMove.useMove(playerPoke, opponentPoke)
                        input()
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                    if opponentPoke.HP <= 0: #checks if a pokemon fainted
                        opponentPokesCopy.remove(opponentPoke)
                        opponentPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print(str(opponent.name)+'\'s', opponentPoke.name, 'fainted!')
                        playerPoke.XPGain(opponentPoke)
                        input()
                        if len(opponentPokesCopy) == 0:
                            won = True
                            break
                        else:
                            opponentPoke = choice(opponentPokesCopy)
                            print(str(opponent.name),'sent out',str(opponentPoke.name))
                            compskip = True
                            input()

                        
                    notUsed = playerPoke.statusAction(opponentPoke, 'after')
                    if playerPoke.HP<=0: #checks if a pokemon fainted
                        playerPokesCopy.remove(playerPoke)
                        playerPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print('your', playerPoke.name, 'fainted!')
                        input()
                        if len(playerPokesCopy)==0:
                            won = False
                            break
                        else:
                            print('Who do you want to send out?')
                            playerPoke = player.choosePoke(playerPokesCopy)
                            print(str(player.name),'sent out',str(playerPoke.name))
                            input()

                    if compskip != True:    
                        computerMove.useMove(opponentPoke, playerPoke)
                        input()
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                    if playerPoke.HP<=0: #checks if a pokemon fainted
                        playerPokesCopy.remove(playerPoke)
                        playerPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print('your', playerPoke.name, 'fainted!')
                        input()
                        if len(playerPokesCopy)==0:
                            won = False
                            break
                        else:
                            print('Who do you want to send out?')
                            playerPoke = player.choosePoke(playerPokesCopy)
                            print(str(player.name),'sent out',str(playerPoke.name))
                            input()

                    notUsed = opponentPoke.statusAction(playerPoke, 'after')
                    if opponentPoke.HP <= 0: #checks if a pokemon fainted
                        opponentPokesCopy.remove(opponentPoke)
                        opponentPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print(str(opponent.name)+'\'s', opponentPoke.name, 'fainted!')
                        playerPoke.XPGain(opponentPoke)
                        input()
                        if len(opponentPokesCopy) == 0:
                            won = True
                            break
                        else:
                            opponentPoke = choice(opponentPokesCopy)
                            print(str(opponent.name),'sent out',str(opponentPoke.name))
                            input()
                            
                else:
                    """
                    computer goes first
                    """
                    computerMove.useMove(opponentPoke, playerPoke)
                    input()
                    os.system(clearVar)
                    battleDisplay(playerPoke, opponentPoke)
                    if playerPoke.HP<=0: #checks if a pokemon fainted
                        playerPokesCopy.remove(playerPoke)
                        playerPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print('your', playerPoke.name, 'fainted!')
                        input()
                        if len(playerPokesCopy)==0:
                            won = False
                            break
                        else:
                            print('Who do you want to send out?')
                            playerPoke = player.choosePoke(playerPokesCopy)
                            print(str(player.name),'sent out',str(playerPoke.name))
                            input()
                            playerskip = True
                            
                    notUsed = opponentPoke.statusAction(playerPoke, 'after')
                    if opponentPoke.HP <= 0: #checks if a pokemon fainted
                        opponentPokesCopy.remove(opponentPoke)
                        opponentPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print(str(opponent.name)+'\'s', opponentPoke.name, 'fainted!')
                        playerPoke.XPGain(opponentPoke)
                        input()
                        if len(opponentPokesCopy) == 0:
                            won = True
                            break
                        else:
                            opponentPoke = choice(opponentPokesCopy)
                            print(str(opponent.name),'sent out',str(opponentPoke.name))
                            input()
                            
                    if playerskip != True:    
                        playerMove.useMove(playerPoke, opponentPoke)
                        input()
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                    if opponentPoke.HP <= 0: #checks if a pokemon fainted
                        opponentPokesCopy.remove(opponentPoke)
                        opponentPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print(str(opponent.name)+'\'s', opponentPoke.name, 'fainted!')
                        playerPoke.XPGain(opponentPoke)
                        input()
                        if len(opponentPokesCopy) == 0:
                            won = True
                            break
                        else:
                            opponentPoke = choice(opponentPokesCopy)
                            print(str(opponent.name),'sent out',str(opponentPoke.name))
                            input()
                            
                        
                    notUsed = playerPoke.statusAction(opponentPoke, 'after')
                    if playerPoke.HP<=0: #checks if a pokemon fainted
                        playerPokesCopy.remove(playerPoke)
                        playerPoke.HP = 0
                        os.system(clearVar)
                        battleDisplay(playerPoke, opponentPoke)
                        print('your', playerPoke.name, 'fainted!')
                        input()
                        if len(playerPokesCopy)==0:
                            won = False
                            break
                        else:
                            print('Who do you want to send out?')
                            playerPoke = player.choosePoke(playerPokesCopy)
                            print(str(player.name),'sent out',str(playerPoke.name))
                            input()
                                
                            
                        

            
    if won == True:
        if wild == False:
            print(opponent.name,'was defeated!')
            if opponent.money > 0:
                print(player.name, 'got', opponent.money,'credits')
                player.money+=opponent.money
                input()
    else:
        print(player.name,'is out of usable pokemon')
        print(player.name,'blacked out!')
        player.partyHeal()
        input()
    battleRestore(player)
    return won
