#to do: Add move pool

from random import *
import copy
import pickle
from moves import *
from pokedex import *
from items import *
from trainers import *

class summary:
    """
    summary class for save/load
    """
    def __init__(self):
        self.playerSave = 0
        self.lastPokecenter = 0
        self.trainers = 0

    def saveLoad(self, save):
        if save == 'save':
            while True:
                os.system(clearVar)
                action = menuSelect('Which Slot?',['Slot1','Slot2','Slot3'])
                slot = 'Slot'+str(action)
                try:
                    with open(slot,'rb') as f:
                        oldGameState = pickle.load(f)
                        
                    print(slot,'contains',oldGameState.playerSave.name,'Are you sure? y/n')
                    willSave = input()
                    if willSave == 'y':
                        with open(slot,'wb') as f:
                            pickle.dump(self,f,protocol = 2)
                        break
                except FileNotFoundError:
                    with open(slot,'wb') as f:
                        pickle.dump(self,f,protocol = 2)
                    break
        else:
            while True:
                os.system(clearVar)
                action = menuSelect('Which Slot?',['Slot1','Slot2','Slot3'])
                slot = 'Slot'+str(action)
                try:
                    with open(slot,'rb') as f:
                        oldGameState = pickle.load(f)
                    print(oldGameState.playerSave.name,'is this correct? y/n')
                    load = input()
                    if load == 'y':
                        self.playerSave = oldGameState.playerSave
                        self.lastPokecenter = oldGameState.lastPokecenter
                        self.trainers = oldGameState.trainers
                        break
                except FileNotFoundError:
                    print('No game data!')
                    input()
        

gameState = summary() #creates the save/load info
        
def main(startModule, modules):
    """
    runs the game
    """
    os.system(clearVar)
    action = menuSelect('Pokemon!',['New Game','Load'])
    if action == 1: #Start new game
        gameState.trainers = allTrainers
        gameState.lastPokecenter = 'palletTown'
        os.system(clearVar)
        playerName = input('Welcome to the world of Pokemon! First, What is your name?\n')
        player = trainer(playerName, [], [], 500) #creates player
        gameState.playerSave = player #adds player to save/load game state
        print('Welcome', player.name+'! your pokemon adventure begins today!')
        input()
        module = startModule(player) #starts the game
    else:
        gameState.saveLoad('load')
        os.system(clearVar)
        player = gameState.playerSave #loads player save into the game player
        module = modules[gameState.lastPokecenter] #finds the saved in game location
        module = module(player) #runs the in game location
    while True:
        module = modules[module] #finds the next module to run
        module = module(player) #runs the next module
    
def menu(player):
    while True:
        os.system(clearVar)
        print('MENU')
        print('1. Pokemon\n2. Pokedex\n3. Items\n4.',player.name,'\n5. Save\n6. Exit')
        action = input()
        if menuValid(action, 6):
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
                print(player.name, '$'+str(player.money))
                print(len(player.playerDex),'Pokemon caught')
                print(player.badges)
                input()
                
            elif action == 5:
                gameState.saveLoad('save')
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
    noMoves = len(opponentPoke.moves)
    move = randint(1,noMoves)
    return opponentPoke.moves[move]
    

def battle(player, opponent, wild= True):
    os.system(clearVar)
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
                        act = playerPoke.statusAction(opponentPoke, 'during')
                        if act == False:
                            playerskip = True
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
                    act = opponentPoke.statusAction(playerPoke, 'during')
                    if act == False:
                        compskip = True
                    if compskip != True:    
                        computerMove.useMove(opponentPoke, playerPoke, True)
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
                    act = opponentPoke.statusAction(playerPoke, 'during')
                    if act == False:
                        compskip = True
                    if compskip != True:
                        computerMove.useMove(opponentPoke, playerPoke, True)
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
                    if playerskip == False:
                        act = playerPoke.statusAction(opponentPoke, 'during')
                        if act == False:
                            playerskip = True
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

def trainerEncounter(player, trainer, phrase1, phrase2):
    if len(trainer.pokeList)>0:
        print(trainer.name+':',phrase1)
        input()
        won = battle(player, trainer, False)
        if won == True:
            trainer.pokeList = []
            print(trainer.name+':',phrase2)
            input()
        return won
    else:
        print(trainer.name+':',phrase2)
        input()
