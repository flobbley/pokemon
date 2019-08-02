from pokemon import *
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

##global lastPokecenter
##lastPokecenter = 'moduleName'
##pokeCenter(player)
##
##itemShop(player)
