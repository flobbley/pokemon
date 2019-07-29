import os
global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"
    
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

def potion(player, pokemon):
    if pokemon.HP == pokemon.maxHP:
        print('It won\'t have any effect!')
    else:
        print('used a potion on',pokemon.name+'!')
        pokemon.heal(20)
        player.itemList[2][1]-=1

def pokeball(player, opponentPoke):
    player.itemList[1][1]-=1
    print('Threw a pokeball!')
    player.catchPoke(opponentPoke)
    
def itemShop(player):
    while True:
        os.system(clearVar)
        print('Welcome to the Pokemart!')
        print('You have',player.money,'credits')
        items = {1:['Pokeball',100],2:['Potion',50]}
        print('What would you like to buy?')
        options = len(items)+1
        for item in items:
            
            print(str(item)+'.',items[item][0])
        print(str(options)+'. Cancel')
        action = input()
        if menuValid(action, options):
            action = int(action)
            if action == options:
                print('Come back and see us again!')
                input()
                break
            elif player.money >= items[action][1]:
                player.money -= items[action][1]
                if action in player.itemList:
                    player.itemList[action][1] += 1
                else:
                    player.itemList[action] = [items[action][0],1]
                print('one',items[action][0],'has been added to your inventory!')
                print('You now have',player.itemList[action][1],player.itemList[action][0]+'s')
                input()
            else:
                print('You don\'t have enough money!')
                input()
        

    
