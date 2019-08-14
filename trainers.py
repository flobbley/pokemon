from pokedex import *
from moves import *


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
            self.playerDex[pokemon.pokeNum] = [pokemon.name, pokemon.entry, pokemon.pokedexSprite]
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
                        print(self.playerDex[poke][2])
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
                items.append(item[0]+' '+str(item[1]))
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
            poke.status = []
            
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
"""
viridian Forest
"""

caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle,stringShot],1.5)
weedle1 = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot],1.5)
kakuna1 = pokemonGenerator(pokedex.kakuna,5,[harden],1.5)
metapod1 = pokemonGenerator(pokedex.metapod,5,[harden],1.5)
metapod2 = pokemonGenerator(pokedex.metapod,5,[harden],1.5)
metapod3 = pokemonGenerator(pokedex.metapod,7,[harden, tackle],1.5)
ratata1 = pokemonGenerator(pokedex.ratata,6,[quickAttack, tackle, tailWhip],1.5)
ratata2 = pokemonGenerator(pokedex.ratata,4,[tackle, tailWhip],1.5)
weedle2 = pokemonGenerator(pokedex.weedle,5,[poisonSting, stringShot],1.5)
weedle3 = pokemonGenerator(pokedex.weedle,6,[poisonSting, stringShot],1.5)
weedle4 = pokemonGenerator(pokedex.weedle,8,[poisonSting, stringShot, harden],1.5)
caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot],1.5)
pidgey1 = pokemonGenerator(pokedex.pidgey,5,[tackle, gust],1.5)
weedle5 = pokemonGenerator(pokedex.weedle,5,[poisonSting, stringShot],1.5)
ratata3 = pokemonGenerator(pokedex.ratata,5,[quickAttack, tailWhip],1.5)




class viridianTrainersClass:
    def __init__(self):
        self.bugCatcherDoug = trainer('Bug Catcher Doug',[caterpie1, weedle1, kakuna1],[],275)
        self.bugCatcherLouis = trainer('Bug Catcher Louis',[metapod1, metapod2, metapod3],[],300)
        self.youngsterJoey = trainer('Youngster Joey',[ratata2, ratata1],[],150)
        self.bugCatcherKim = trainer('Bug Trainer Kim',[weedle2, weedle3, weedle4],[],250)
        self.youngsterLiz = trainer('Youngster Liz', [caterpie2, pidgey1, weedle5, ratata3],[],400)

viridianTrainers = viridianTrainersClass()


"""
Pewter City
"""

diglett1 = pokemonGenerator(pokedex.diglett,11,[scratch, leer],1.5)
sandshrew1 = pokemonGenerator(pokedex.sandshrew, 11, [scratch, tackle, defenseCurl],1.5)
geodude1 = pokemonGenerator(pokedex.geodude, 12, [tackle, defenseCurl], 1.5)
onix1 = pokemonGenerator(pokedex.onix, 14, [tackle, screech, defenseCurl], 1.5)

class pewterTrainersClass:
    def __init__(self):
        self.juniorTrainerRodney = trainer('Junior Trainer Rodney',[diglett1, sandshrew1],[],400)
        self.brock = trainer('Gym Leader Brock',[geodude1, onix1],[],1000)

pewterTrainers = pewterTrainersClass()

class rivalClass:
    def __init__(self):
        self.gary = trainer('Gary',[],['victoryRoad'],0)

rival = rivalClass()

"""
Gyro
"""

friendDiglett1 = pokemonGenerator(pokedex.diglett,5,[scratch, tailWhip],1.5)

class gyroTrainersClass:
    def __init__(self):
        self.firstEncounterOscar = trainer('Oscar',[friendDiglett1],[],200)

gyroTrainers = gyroTrainersClass()

class trainers:
    def __init__(self):
        self.viridianTrainers = viridianTrainers
        self.pewterTrainers = pewterTrainers
        self.rival = rival
        self.gyroTrainers = gyroTrainers

allTrainers = trainers()
