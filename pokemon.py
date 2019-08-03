#to do: Add move pool

from random import *
import os
import copy
from moves import *
from pokedex import *
from items import *
global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"
global lastPokecenter
lastPokecenter = 'palletTown'
    
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
        
def main():
    os.system(clearVar)
    modules = {'bedroom':bedroom, 'momsHouse':momsHouse, 'lab':lab, 'garysHouse':garysHouse, 'route29north':route29north, 'palletTown':palletTown, 'viridianCity':viridianCity,\
               'route29south':route29south, 'viridianArea1':viridianArea1}
    playerName = input('Welcome to the world of Pokemon! First, What is your name?\n') #setup
    player = trainer(playerName, [], [], 500)
    print('Welcome', player.name+'! your pokemon adventure begins today!')
    input()
    module = bedroom(player)
    while True:
        module = modules[module]
        module = module(player)
    
def menu(player):
    while True:
        os.system(clearVar)
        print('MENU')
        print('1. Pokemon\n2. Pokedex\n3. Items\n4. Exit')
        action = input()
        if menuValid(action, 4):
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


"""
Pallet Town to Viridian City
"""

def bedroom(player):
    while True:
        os.system(clearVar)
        print('You find yourself in your bedroom, there is a TV in the corner, a game system in front of it, and stairs that go down')
        print('what would you like to do?')
        print('1. Watch tv\n2. Play video games\n3. Go downstairs\n4. Menu')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                print('It\'s a weather report! Bright and sunny all day!')
                input()
            elif action == 2:
                print('It\'s an older system, looks like a SNES. Who even has these anymore?')
                input()
            elif action == 3:
                print('You walk downstairs to the rest of the house')
                input()
                return 'momsHouse'
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)

def momsHouse(player):
        while True:
            os.system(clearVar)
            print('You find yourself in the main room, your mom is brushing her pokemon on the couch, there are stairs that go up to your room')
            print('What would you like to do?')
            print('1. Talk to mom\n2. Go upstairs\n3. Leave\n4. Menu')
            action = input()
            if menuValid(action, 4):
                action = int(action)
                if action == 1:
                    if len(player.pokeList) == 0:
                        print('Mom: "Today is the big day! if you find Professor Oak he will give you a pokemon!"')
                        input()
                    else:
                        print('Mom: "I can\'t believe my child is all grown up and going on their own pokemon adventure!"')
                        print('"Why don\'t you take a rest for a bit?" (pokemon are healed)')
                        global lastPokecenter
                        lastPokecenter = 'palletTown'
                        player.partyHeal()
                        input()
                elif action == 2:
                    print('You walk upstairs')
                    input()
                    return 'bedroom'
                elif action == 3:
                    return 'palletTown'
                    input()
                else:
                    if len(player.pokeList)==0:
                        print('You don\'t have any pokemon! there is no menu yet!')
                        input()
                    else:
                        menu(player)
            os.system(clearVar)
            
def garysHouse(player):
    while True:
        os.system(clearVar)
        print('You walk into Gary\'s house and see his sister sitting at the table, and a map of the area on the wall')
        print('What would you like to do?')
        print('1. Talk to Gary\'s sister\n2. Look at the map\n3. Leave\n4. Menu')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                print('Gary\'s sister: "Hiya',player.name+',', 'how have you been? Gary isn\'t home right now, he\'s looking for Grandpa"')
                input()
            elif action == 2:
                print('The big cities sure do look far away...')
                input()
            elif action == 3:
                os.system(clearVar)
                return 'palletTown'
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)

def route29(player):
    wild = trainer('Wild', [], {}, 10)
    pidgey1 = pokemonGenerator(pokedex.pidgey,5,[tackle,gust])
    pidgey2 = pokemonGenerator(pokedex.pidgey,3,[tackle,gust,])
    pidgey3 = pokemonGenerator(pokedex.pidgey,2,[tackle,gust])
    pidgey4 = pokemonGenerator(pokedex.pidgey,3,[tackle,gust])
    ratata1 = pokemonGenerator(pokedex.ratata,4,[tackle,tailWhip])
    ratata2 = pokemonGenerator(pokedex.ratata,3,[tackle,tailWhip])
    ratata3 = pokemonGenerator(pokedex.ratata,2,[tackle,tailWhip])
    encounters = [pidgey1, pidgey2, pidgey3, pidgey4, ratata1, ratata2, ratata3]
    chance = [True, False]
    patches = 3
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
    return True
    
def route29north(player):
    os.system(clearVar)
    if len(player.pokeList)==0:
        print('You decide it\'s time to start your journey, and take your first steps out into the long grass of Route 29 toward Viridian City')
        input()
        print('"Wait!" you hear a shout behind you, it\'s Professor Oak!')
        input()
        print('Professor Oak: "Don\'t go into the long grass without a pokemon of your own to defend yourself!')
        print('"Follow me to my lab, I\'ll give you a pokemon of your own!"')
        input()
        lab(player, False)
        return 'palletTown'
    else:
        print('you head out on Route 29 toward Viridian City, there are three patches of tall grass you have to pass through on your way there. You may encounter wild pokemon...')
        input()
        passed = route29(player)
        if passed:
            return 'viridianCity'
        else:
            return lastPokecenter

def route29south(player):
    os.system(clearVar)
    print('You head south on Route 29 toward Pallet Town, there are three patches of tall grass you have to pass through on your way there. You may encounter wild pokemon...')
    passed = route29(player)
    if passed:
        return 'palletTown'
    else:
        return lastPokecenter

def viridianCity(player):
    while True:
        os.system(clearVar)
        print('you find yourself in Viridian City. There is a Pokecenter here, as well as a Pokemart.')
        print('To the north there is a road that leads in to the Viridian Forest. Then off to the side of town you see the local Pokemon Gym!')#LEFT OFF HERE
        action = menuSelect('Where would your like to go?',['Pokecenter','Pokemart','Into the Viridian Forest','Pokemon Gym','Head back on Route 29 toward Pallet Town','Menu'])
        if action == 1:
            global lastPokecenter
            lastPokecenter = 'viridianCity'
            pokeCenter(player)
        elif action == 2:
            itemShop(player)
        elif action == 4:
            print('As you approach the gym you notice that something feels off, the building looks like it hasn\'t been maintained in quite sometime')
            input()
            print('Old Man: "Looking at the old Pokemon Gym eh? Nobody has been there in quite some time,')
            print("the old gym leader left years ago, just an abandoned old building now")
            input()
        elif action == 3:
            return 'viridianArea1'
        elif action == 5:
            return 'route29south'
        else:
            menu(player)
        
def palletTown(player):
    while True:
        os.system(clearVar)
        print('You find yourself standing in Pallet Town, the sleepy small town you grew up in')
        print('There is not much of note here besides you house, your rival Gary\'s house, and the world famous pokemon lab!')
        print('What would you like to do?')
        print('1. Go to my house\n2. Go to Gary\'s house\n3. Go to the pokemon lab\n4. Go on the north path toward Viridian City\n5. Menu')
        action = input()
        if menuValid(action, 5):
            action = int(action)
            if action == 1:
                return 'momsHouse'
            elif action == 2:
                return 'garysHouse'
            elif action == 3:
                return 'lab'
            elif action == 4:
                return 'route29north'
            else:
                if len(player.pokeList) == 0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)
            
def lab(player, pokeGot = True):
    os.system(clearVar)
    if pokeGot == False:
        print('As you walk into the lab you see Professor Oak\'s grandson, Gary, waiting')
        input()
        print('Gary: "Where ya been gramps? I\'ve been waiting all morning! you said you would give me a pokemon today!"')
        input()
        print('Professor Oak: "Oh? was that today? it must have slipped my mind. Before I forget, both of you take one of these pokedex\'s I made. They\'ll keep track of the different kinds of pokemon you catch!"')
        input()
        print('"But anyway you\'re both here now so it\'s time to pick out your first pokemon!"')
        print('"'+player.name, 'why don\'t you pick first?"')
        input()
        print('Gary: "Aw come on gramps that\'s so unfair!"')
        input()
        os.system(clearVar)
        print('Professor Oak: "Now now Gary, you\'ll get your turn, now which pokemon would you like',player.name+'?"')
        
        gary = trainer('Gary',[],{},10)
        squirtle = pokemonGenerator(pokedex.squirtle, 5, [tackle,tailWhip])
        charmander = pokemonGenerator(pokedex.charmander, 5, [scratch,tailWhip])
        bulbasaur = pokemonGenerator(pokedex.bulbasaur,5,[tackle,leer])
        while True: #first Pokemon selection
            poke = input('\n1.Squirtle\n2.Charmander\n3.Bulbasaur\n')
            if menuValid(poke, 3):
                poke = int(poke)
                break
        if poke == 1:
            print('Great choice! Squirtle is a great defensive pokemon, cute too!')
            input()
            player.addPoke(squirtle)
            gary.pokeList = [bulbasaur]
            
        elif poke == 2:
            print('Great choice! Charmander is a fiery attacker! loves to play fetch too!')
            input()
            player.addPoke(charmander)
            gary.pokeList = [squirtle]
            
        else:
            print('Great choice! Bulbasaur is a sturdy blocker! loves to bask in the sun!')
            input()
            player.addPoke(bulbasaur)
            gary.pokeList = [charmander]
                
        os.system(clearVar)
        player.pokeList[0].gainedXP = 100
        print('Gary: Fine, then I\'ll take',str(gary.pokeList[0].name)+'!')
        input()
        print('You turn to leave the lab, but suddenly you feel Gary grab your arm')
        input()
        print('Gary: Where are you going',str(player.name)+'? Dontcha wanna have your first battle?') #gary initiates first battle

        while True:
            print('1. YES!')
            print('2. No!')
            react = input()
            if menuValid(react, 2):
                react = int(react)
                break
        if react == 1:
            print('Gary: Alright! that\'s the spirit!, don\'t worry I won\'t gloat too much when I beat you!')
            input()
            
        elif react == 2:
            print('Gary: Too bad!')
            print('Before you have time to react Gary throws his pokeball and gets ready to battle')
            input()
            
        os.system(clearVar)
        won = battle(player, gary, False) #starts the battle
        os.system(clearVar)
        player.pokeList[0].HP = player.pokeList[0].maxHP
        if won == True:
            print('Gary: Aw shucks, you were just lucky this time! I\'m off to battle some real trainers, smell ya later!')
            input()
        else:
            print('Gary: Haha I knew it! you don\'t have what it takes! I\'m off to battle some real trainers, smell ya later!')
            input()
        print('And with that, Gary walks out the door, after a while you decide to do the same')
        input()
    else:
        if len(player.pokeList)==0:
            while True:
                print('As you enter the lab you see a couple scientists you\'ve seen around town but there\'s no sign of Professor Oak')
                print('What would you like to do?')
                print('1. Talk to one of the scientists\n2. Leave\n3. Menu')
                action = input()
                if menuValid(action, 3):
                    action = int(action)
                    if action == 1:
                        print('Scientist: "Well hello there young man! Looking for Professor Oak? We haven\'t seen him all morning."')
                        input()
                    elif action == 2:
                        return 'palletTown'
                    else:
                        print('You don\'t have any pokemon! there is no menu yet!')
                        input()
                os.system(clearVar)
                
        else:
            while True:
                os.system(clearVar)
                print('You enter Professor Oak\'s pokemon lab!')
                print('What would you like to do?')
                print('1. Talk to Professor Oak\n2. Talk to one of the scientists\n3. Leave\n4. Menu')
                action = input()
                if menuValid(action, 4):
                    action = int(action)
                    if action == 1:
                        print('Professor Oak: "Oh hello',player.name+'! How is the pokedex coming along?"')
                        input()
                        print('Professor Oak: "Let\'s see....', len(player.playerDex),'pokemon caught, keep it up!"')
                        input()
                    elif action == 2:
                        print('Scientist: "Phew, we work really hard around here, Professor Oak never gives us a break!"')
                        input()
                    elif action == 3:
                        return 'palletTown'
                    else:
                        menu(player)
        
"""
Viridian Forest
"""

def viridianWild(player):
    wild = trainer('Wild', [], {}, 10)
    caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie3 = pokemonGenerator(pokedex.caterpie,4,[tackle, stringShot])
    caterpie4 = pokemonGenerator(pokedex.caterpie,2,[tackle, stringShot])
    weedle1 = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot])
    weedle2 = pokemonGenerator(pokedex.weedle,2,[poisonSting, stringShot])
    weedle3 = pokemonGenerator(pokedex.weedle,4,[poisonSting, stringShot])
    encounters = [caterpie1, caterpie2, caterpie3, caterpie4, weedle1, weedle2, weedle3]
    chance = [True, False]
    patches = 1
    i = 1
    for patch in range(1,patches+1):
        if choice(chance):
            print ('You hear a rustle in patch',i,'a wild pokemon appears!')
            i+=1
            input()
            wildPoke = choice(encounters)
            wild.pokeList.append(wildPoke)
            os.system(clearVar)
            won = battle(player, wild)
            if won == False:
                return False
            wild.pokeList.remove(wildPoke)
            encounters.remove(wildPoke)
            input()
    return True

def viridianArea1(player):
    while True:
        os.system(clearVar)
        print('You find yourself at the entrance of the Veridian Forest, it\'s dark, and kinda scary') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        print('you see a man who looks like he\'s itching for a fight, as well as a patch of tall grass')
        action = menuSelect('What do you want to do?',['Talk to man','Enter the grass','Go back to Veridian City','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            if len(viridianTrainer.bugCatcher.pokeList)>0:
                print('Bug Catcher: "I\'m here to catch all kinds of bugs!"')
                input()
                won = battle(player, viridianTrainer.bugCatcher, False)
                if won == True:
                    viridianTrainer.bugCatcher.pokeList = []
            else:
                print('Bug Catcher: "But all I can find are caterpies and weedles"')
                input()
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            print('You enter the tall grass...')
            input()
            passed = viridianWild(player)
            if passed == False:
                return lastPokecenter                              
            #return 'newModule'
        elif action == 3:
            return 'viridianCity'
            #return 'newModule
        else:
            menu(player) #the last option is usually menu, but doesn't have to be 

ashPidgey = pokemonGenerator(pokedex.pidgey, 4, [tackle, gust])
garyPidgey = pokemonGenerator(pokedex.pidgey,4,[tackle, gust])
ashBulbasaur = pokemonGenerator(pokedex.bulbasaur,5,[tackle,leer])
garyBulbasaur = pokemonGenerator(pokedex.bulbasaur, 5, [tackle, leer])
ashSquirtle = pokemonGenerator(pokedex.squirtle, 5, [tackle, tailWhip])
garyCharmander = pokemonGenerator(pokedex.charmander, 5, [scratch, tailWhip])
garySquirtle = pokemonGenerator(pokedex.squirtle, 5, [tackle, tailWhip])
ashCharmander = pokemonGenerator(pokedex.charmander, 5, [scratch, tailWhip])
ashRatata = pokemonGenerator(pokedex.ratata,2,[tackle,quickAttack])
caterpie = pokemonGenerator(pokedex.caterpie,3,[tackle,stringShot])
weedle = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot])
kakuna = pokemonGenerator(pokedex.kakuna,5,[harden])

bugCatcher = trainer('Bug Catcher',[caterpie, weedle, kakuna],[],275)

ash = trainer('ash', [ashRatata, ashPidgey, ashBulbasaur], [['Pokeball',5],['Potion',5]], 500)
gary = trainer('gary', [garyBulbasaur, garySquirtle, garyCharmander], [], 10)

class viridianTrainer:
    def __init__(self):
        self.bugCatcher = trainer('Bug Catcher',[caterpie, weedle, kakuna],[],275)
viridianTrainer = viridianTrainer()
#print(battle(ash, gary, False))

print(main()) #runs the game
