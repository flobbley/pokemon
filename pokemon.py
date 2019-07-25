#to do: Add move pool/move learning/dynamic stats to pokemon
#to do: Add pallet town
#to do: Add items

from random import *
import os
import copy
from moves import *
from pokedex import *

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

    def getName(self): #gets the name of the trainer
        print(self.name)

    def getFirstPoke(self): #returns the pokemon at the front of the lineup
        return self.pokeList[0]

    def addPoke(self, pokemon): #adds a new pokemon to the roster
        self.pokeList.append(pokemon)
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
            index = input()
            if menuValid(index, options):
                index = int(index)
                break
        poke = currentList[index-1]
        return poke

    def checkDex(self):
        while True:
            while True:
                os.system("clear")
                print('Which entry would you like to check?')
                i = 1
                option = len(self.playerDex)+1
                for pokeNum in self.playerDex:
                    print(str(pokeNum)+'.', self.playerDex[pokeNum][0])
                print(option,'cancel')
                poke = input()
                if menuValid(poke,option):
                    poke = int(poke)
                    break
            if poke < option:
                os.system("clear")
                print(self.playerDex[poke][1])
                input()
            else:
                break
    def getItem(self, item, number):
        if item in itemList:
            itemList[item] += number
        else:
            itemList[item] = number
def main():
    modules = {'bedroom':bedroom, 'momsHouse':momsHouse, 'lab':lab, 'garysHouse':garysHouse, 'route29':route29, 'palletTown':palletTown}
    playerName = input('Welcome to the world of Pokemon! First, What is your name?\n') #setup
    player = trainer(playerName, [], {}, 500)
    print('Welcome', player.name+'! your pokemon adventure begins today!')
    input()
    module = bedroom(player)
    while True:
        module = modules[module]
        module = module(player)
    
def menu(player):
    while True:
        os.system("clear")
        print('MENU')
        print('1. Pokemon\n2. Pokedex\n3. Items\n4. Exit')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            if action == 1:
                for poke in player.pokeList:
                    print(poke.name)
                    print(poke.HPBar())
                input()
            elif action == 2:
                print('Which pokemon would you like to see?')
                i = 1
                for number in player.playerDex:
                    print(str(number)+'.', player.playerDex[number][0])
                    i+=1
                while True:
                    poke = input()
                    if menuValid(poke, i):
                        poke = int(poke)
                        print(player.playerDex[poke][1])
                        input()
                        break
            elif action == 3:
                i = 1
                for item in player.itemList:
                    print(str(i)+'.', item)
            else:
                break
                    

def bedroom(player):
    while True:
        os.system("clear")
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
            os.system("clear")
            print('You find yourself in the main room, your mom is brushing her pokemon on the couch, there are stairs that go up to your room')
            print('What would you like to do?')
            print('1. Talk to mom\n2. Go upstairs\n3. Leave\n4. Menu')
            action = input()
            if menuValid(action, 4):
                action = int(action)
                if action == 1:
                    if len(player.pokeList) == 0:
                        print('Mom: "Today is the big day! if you find Professor Oak he will give you a pokemon!')
                        input()
                    else:
                        print('Mom: "I can\'t believe my child is all grown up and going on their own pokemon adventure!')
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
            os.system("clear")
            
def garysHouse(player):
    while True:
        os.system("clear")
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
                os.system("clear")
                return 'palletTown'
            else:
                if len(player.pokeList)==0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                    input()
                else:
                    menu(player)

def route29(player):
    os.system("clear")
    if len(player.pokeList)==0:
        print('You decide it\'s time to start your journey, and take your first steps out into the long grass of Route 29 toward Viridian City')
        input()
        print('"Wait!" you hear a shout behind you, it\'s Professor Oak!')
        input()
        print('Professor Oak: "Don\'t go into the long grass without a pokemon of you\'re own to defend yourself!')
        print('"Follow me to my lab, I\'ll give you a pokemon of your own!"')
        input()
        lab(player, False)
        return 'palletTown'
    else:
        print('Route 29')

def palletTown(player):
    while True:
        os.system("clear")
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
                return 'route29'
            else:
                if len(player.pokeList) == 0:
                    print('You don\'t have any pokemon! there is no menu yet!')
                else:
                    menu(player)
        os.system("clear")
            
def lab(player, pokeGot = True):
    os.system("clear")
    """
    Main game loop
    """
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
        os.system("clear")
        print('Professor Oak: "Now now Gary, you\'ll get your turn, now which pokemon would you like',player.name+'?"')
        
        gary = trainer('Gary',[],{},10)
        while True: #first Pokemon selection
            poke = input('\n1.Squirtle\n2.Charmander\n3.Bulbasaur\n')
            if menuValid(poke, 3):
                poke = int(poke)
                break
        if poke == 1:
            print('Great choice! Squirtle is a great defensive pokemon, cute too!')
            input()
            ashSquirtle = copy.deepcopy(pokedex.squirtle)
            playerChar.addPoke(ashSquirtle)
            garyBulbasaur = copy.deepcopy(pokedex.bulbasaur)
            gary.pokeList = [garyBulbasaur]
            
        elif poke == 2:
            print('Great choice! Charmander is a fiery attacker! loves to play fetch too!')
            input()
            ashCharmander = copy.deepcopy(pokedex.charmander)
            player.addPoke(ashCharmander)
            garySquirtle = copy.deepcopy(pokedex.squirtle)
            gary.pokeList = [garySquirtle]
            
        else:
            print('Great choice! Bulbasaur is a sturdy blocker! loves to bask in the sun!')
            input()
            ashBulbasaur = copy.deepcopy(pokedex.bulbasaur)
            player.addPoke(ashBulbasaur)
            garyCharmander = copy.deepcopy(pokedex.charmander)
            gary.pokeList = [garyCharmander]
                
        os.system("clear")
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
            
        os.system("clear")
        won = battle(player, gary) #starts the battle
        os.system("clear")
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
                os.system("clear")
                
        else:
            while True:
                os.system("clear")
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

def whoGoesFirst(playerPoke, opponentPoke):
    if playerPoke.stats['speed']>=opponentPoke.stats['speed']:
        return 0
    else:
        return 1

def playerTurn(playerPoke, opponentPoke):
    """
    defines the players turn
    """
    act = playerPoke.statusAction(opponentPoke, 'during')
    if act:
        while True:
            playerPoke.getMoves()
            move = input()
            noMoves = len(playerPoke.moves)
            if menuValid(move, noMoves):
                move = int(move)
                break
        print(playerPoke.name, 'used', playerPoke.moves[move][1])
        playerPoke.useMove(move, opponentPoke)
        
    
def computerTurn(playerPoke, opponentPoke, opponentName):
    """
    defines the computers turn
    """
    act = opponentPoke.statusAction(playerPoke, 'during')
    if act:
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

def battleMenu():
    while True:
        print('What would you like to do?')
        print('1. Attack  2. Change Poke')
        print('3. Item    4. Run Away')
        action = input()
        if menuValid(action, 4):
            action = int(action)
            return action
        
def battle(player, opponent):
    """
    Main pokemon battle loop
    """
    playerPokesCopy = player.pokeList[:]
    opponentPokesCopy = opponent.pokeList[:]
    start = 0
    won = 5
    print(opponent.name,'wants to battle!')
    input()
    while True: #change pokemon if one faints
        if won == True or won == False:
            break
        if start == 0:
            playerPoke = player.getFirstPoke()
            print(str(player.name),'sent out',str(playerPoke.name))
            opponentPoke = opponent.getFirstPoke()
            print(str(opponent.name),'sent out',str(opponentPoke.name))
            start = 1
            battleDisplay(playerPoke, opponentPoke)
            input()
            os.system("clear")
            turn = whoGoesFirst(playerPoke, opponentPoke)
        else:
            turn = whoGoesFirst(playerPoke, opponentPoke)
        while True: #Current match up          
            os.system("clear")
            if turn == 0: #when turn is 0 it is the player's turn
                battleDisplay(playerPoke, opponentPoke)
                notUsed = playerPoke.statusAction(opponentPoke, 'before')
                while True: #continues player menu until valid action is taken
                    action = battleMenu()
                    if action == 1:
                        playerTurn(playerPoke, opponentPoke)
                        input()
                        break
                    elif action == 2:
                        oldPlayerPoke = playerPoke
                        playerPoke = player.choosePoke(playerPokesCopy)
                        if oldPlayerPoke == playerPoke:
                            print(playerPoke.name,'is already out!')
                        else:
                            break
                    elif action == 3:
                        print('test')
                    else:
                        print('can\'t run from a trainer battle!')
                    input()
                if opponentPoke.HP <= 0: #checks if a pokemon fainted
                    opponentPokesCopy.remove(opponentPoke)
                    opponentPoke.HP = 0
                    os.system("clear")
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
                        turn = 1-whoGoesFirst(playerPoke, opponentPoke)
                        
                notUsed = playerPoke.statusAction(opponentPoke, 'after')
                if playerPoke.HP<=0: #checks if a pokemon fainted
                    playerPokesCopy.remove(playerPoke)
                    playerPoke.HP = 0
                    os.system("clear")
                    battleDisplay(playerPoke, opponentPoke)
                    print('your', playerPoke.name, 'fainted!')
                    input()
                    if len(playerPokesCopy)==0:
                        won = False
                        break
                    else:
                        playerPoke = player.choosePoke(playerPokesCopy)
                        print(str(player.name),'sent out',str(playerPoke.name))
                        turn = 1-whoGoesFirst(playerPoke, opponentPoke)
                        
                
            else: #when turn is not 0 it is the computer's turn
                battleDisplay(playerPoke, opponentPoke)
                notUsed = opponentPoke.statusAction(playerPoke, 'before')
                computerTurn(playerPoke, opponentPoke, str(opponent.name))
                input()
                if playerPoke.HP<=0: #checks if a pokemon fainted
                    playerPokesCopy.remove(playerPoke)
                    playerPoke.HP = 0
                    os.system("clear")
                    battleDisplay(playerPoke, opponentPoke)
                    print('your', playerPoke.name, 'fainted!')
                    input()
                    if len(playerPokesCopy)==0:
                        won = False
                        break
                    else:
                        playerPoke = player.choosePoke(playerPokesCopy)
                        print(str(player.name),'sent out',str(playerPoke.name))
                        turn = 1-whoGoesFirst(playerPoke, opponentPoke)
                        
                notUsed = opponentPoke.statusAction(playerPoke, 'after')
                if opponentPoke.HP <= 0: #checks if a pokemon fainted
                    opponentPokesCopy.remove(opponentPoke)
                    opponentPoke.HP = 0
                    os.system("clear")
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
                        turn = 1-whoGoesFirst(playerPoke, opponentPoke)
                        
            turn = 1-turn
            
    if won == True:
        print('You won!')
    else:
        print('You lose!')
    battleRestore(player)
    return won

print(main()) #runs the game

ashPidgey = copy.deepcopy(pokedex.pidgey)
garyPidgey = copy.deepcopy(pokedex.pidgey)
ashBulbasaur = copy.deepcopy(pokedex.bulbasaur)
garyBulbasaur = copy.deepcopy(pokedex.bulbasaur)
ashSquirtle = copy.deepcopy(pokedex.squirtle)
garyCharmander = copy.deepcopy(pokedex.charmander)
garySquirtle = copy.deepcopy(pokedex.squirtle)
ashCharmander = copy.deepcopy(pokedex.charmander)

ash = trainer('ash', [], {}, 10)
gary = trainer('gary', [], {}, 10)

#print(battle(ash, gary))
