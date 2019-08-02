from pokemon import *
def moduleName(player):
    while True:
        os.system(clearVar)
        print('You wake up in your bedroom to the sound of your Mom\'s voice','"'+player.name,'It\'s time to get up or you\'ll be late for school!"') #Enter descriptor info here, hashtags indicate comments, they are ignored by the code
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
print(moduleName(ash))
##global lastPokecenter
##lastPokecenter = 'moduleName'
##pokeCenter(player)
##
##itemShop(player)
