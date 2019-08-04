from pokemon import *

def mainTest(startModule, player):
    os.system(clearVar)
    modules = {'myHouseNoQuiz':myHouseNoQuiz, 'quiz':quiz, 'getFirstPoke':getFirstPoke}
    module = startModule(player)
    while True:
        module = modules[module]
        module = module(player)

def myBedroomFirst(player):
    """
    WIP
    """
    while True:
        os.system(clearVar)
        print('You awake to the sound of your alarm, your Mom is shouting that you\'ll be late to school. It\'s time to get up!') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        print('A cold realization washes over you, you didn\'t finish your homework and it\'s due today!')
        action = menuSelect('What would you like to do?',['Get dressed, head downstairs','Check what\'s on T.V.','Hit snooze, try and catch a few more ZZZ','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            return 'myHouseNoQuiz' #---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            print('It\'s a weather report for Gyarapolis, looks like clear skies with a chance of thunderstorms in the afternoon')
            input()
            #return 'newModule'
        elif action == 3:
            print('...Mom:"',player.name,'GET UP! YOU ARE GOING TO BE LATE! DON\'T MAKE ME COME UP THERE!"')
            input()
            #return 'newModule
            #return 'newModule
        else:
            menu(player) #the last option is usually menu, but doesn't have to be
            
def myHouseNoQuiz(player):
    """
    WIP
    """
    while True:
        os.system(clearVar)
        print('Mom:"Good Morning! Big Day today, did you finish your homework?') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        action = menuSelect('What would you like to do?',['"Yeah of course, who do you think I am?"','Go back upstairs without a word','Try to run out of the house without her noticing','"Oh yeah, I forgot it upstairs!','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('Mom: A liar apparently, go back up there and get it done!')
            input()
            return 'quiz'
        elif action == 2:
            print('Mom: I thought so, I\'ll have breakfast waiting for you when you are done.')
            input()
            return 'quiz'
        elif action == 3:
            print('Dad: Where do you think you\'re going?!')
            input()
        elif action == 4:
            print('Mom: Uh, huh, sure you did.')
            input()
            return 'quiz'
        else:
            menu(player) #the last option is usually menu, but doesn't have to be

def quiz(player):
    quizAnswers =[]
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    while True:
        os.system(clearVar)
        print('You go upstairs, and find your homework is still on your computer from the night before') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        action = menuSelect('What is your favorite color?',['A cool Cerulean','A fiery Vermillion','A vibrant Viridian','A fun Fuschia','A subtle Saffron'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
            
        print('Answer 1 recorded')
        input()
        
        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 2 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 3 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 4 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 5 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 6 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 7 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 8 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 9 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 10 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 11 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 12 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 13 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 14 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 15 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 16 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 17 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 18 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 19 recorded')
        input()

        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            quizAnswers.append(a)
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            quizAnswers.append(b)
            #return 'newModule'
        elif action == 3:
            quizAnswers.append(c)
            #return 'newModule'
        elif action == 4:
            quizAnswers.append(d)
            #return 'newModule'
        else:
            quizAnswers.append(e)
        print('Answer 20 recorded')
        input()


        bulb = quizAnswers.count('a')
        char = quizAnswers.count('b')
        squirt = quizAnswers.count('c')
        mach = quizAnswers.count('d')
        ralts = quizAnswers.count('e')

        poke = {'Bulbasaur':bulb,'Charmander':char,'Squirtle':squirt,'Machop':mach, 'Ralts':ralts}
        highest = 0
        newPokeList = []
        for potential in poke:
            if poke[potential] >highest:
                highest = poke[potential]
                newPoke = potential
                newPokeList = [potential]
            elif poke[potential] == highest:
                newPokeList.append(potential)
        if len(newPokeList) > 1:
            print('That\'s interesting, you fell between',len(newPokeList),'pokemon')
            action = menuSelect('Which would you prefer?',newPokeList)
            newPoke = newPokeList[action-1]
        global playerPoke
        playerPoke = newPoke
        return 'getFirstPoke'

def getFirstPoke(player):
    while True:
        os.system(clearVar)
        print('example') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        player.pokeList.append(potentialPokes[playerPoke])
        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('enter dialogue here, or if pokecenter/item shop, copy pokecenter/item code')
            input()
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            print('enter dialogue here etc')
            input()
            #return 'newModule'
        elif action == 3:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        elif action == 4:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        else:
            menu(player) #the last option is usually menu, but doesn't have to be
        
def moduleName(player):
    while True:
        os.system(clearVar)
        print('example') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
        action = menuSelect('Question',['list','of','possible','answers','menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('enter dialogue here, or if pokecenter/item shop, copy pokecenter/item code')
            input()
            #return 'newModule' ---- if this option leads to a new module, uncomment this line and put the name of the new module in the quotes
        elif action == 2:
            print('enter dialogue here etc')
            input()
            #return 'newModule'
        elif action == 3:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        elif action == 4:
            print('enter dialogue here, etc')
            input()
            #return 'newModule
        else:
            menu(player) #the last option is usually menu, but doesn't have to be


def wildEncounter(player):
    wild = trainer('Wild', [], {}, 10)
    caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle])
    caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle])
    caterpie3 = pokemonGenerator(pokedex.caterpie,4,[tackle])
    caterpie4 = pokemonGenerator(pokedex.caterpie,2,[tackle])
    weedle1 = pokemonGenerator(pokedex.weedle,3,[tackle, leer])
    weedle2 = pokemonGenerator(pokedex.weedle,2,[tackle, leer])
    weedle3 = pokemonGenerator(pokedex.weedle,4,[tackle, leer])
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

bulb = copy.deepcopy(pokedex.bulbasaur)
char = copy.deepcopy(pokedex.charmander)
squirt = copy.deepcopy(pokedex.squirtle)
bulb.addLevel(5)
char.addLevel(5)
squirt.addLevel(5)
#ralts = copy.deepcopy(pokedex.ralts)
#machop = copy.deepcopy(pokedex.machop)

potentialPokes = {'Bulbasaur':bulb,'Charmander':char,'Squirtle':squirt} #'Ralts':ralts,'Machop':machop}
##global lastPokecenter
##lastPokecenter = 'moduleName'
##pokeCenter(player)
##
##itemShop(player)
