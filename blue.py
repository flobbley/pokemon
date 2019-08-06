#to do: Add move pool

from mechanics import *

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
                    gameState.lastPokecenter = 'palletTown'
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
            return gameState.lastPokecenter

def route29south(player):
    os.system(clearVar)
    print('You head south on Route 29 toward Pallet Town, there are three patches of tall grass you have to pass through on your way there. You may encounter wild pokemon...')
    passed = route29(player)
    if passed:
        return 'palletTown'
    else:
        return gameState.lastPokecenter

def viridianCity(player):
    while True:
        os.system(clearVar)
        print('you find yourself in Viridian City. There is a Pokecenter here, as well as a Pokemart.')
        print('To the north there is a road that leads in to the Viridian Forest. Then off to the side of town you see the local Pokemon Gym!')#LEFT OFF HERE
        action = menuSelect('Where would your like to go?',['Pokecenter','Pokemart','Into the Viridian Forest','Pokemon Gym','Head back on Route 29 toward Pallet Town','Menu'])
        if action == 1:
            gameState.lastPokecenter = 'viridianCity'
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
        squirtle = pokemonGenerator(pokedex.squirtle, 5, [tackle,tailWhip], 1.5)
        charmander = pokemonGenerator(pokedex.charmander, 5, [scratch,tailWhip], 1.5)
        bulbasaur = pokemonGenerator(pokedex.bulbasaur,5,[tackle,leer], 1.5)
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
ashRatata = pokemonGenerator(pokedex.ratata,2,[tackle,quickAttack],1.5)
caterpie = pokemonGenerator(pokedex.caterpie,3,[tackle,stringShot],1.5)
weedle = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot],1.5)
kakuna = pokemonGenerator(pokedex.kakuna,5,[harden])

ash = trainer('ash', [ashRatata, ashPidgey, ashBulbasaur], [['Pokeball',5],['Potion',5]], 500)
gary = trainer('gary', [garyBulbasaur, garySquirtle, garyCharmander], [], 10)

class viridianTrainer:
    def __init__(self):
        self.bugCatcher = trainer('Bug Catcher',[caterpie, weedle, kakuna],[],275)
viridianTrainer = viridianTrainer()
#print(battle(ash, gary, False))

"""
main game area
"""

modules = {'bedroom':bedroom, 'momsHouse':momsHouse, 'lab':lab, 'garysHouse':garysHouse, 'route29north':route29north, 'palletTown':palletTown, 'viridianCity':viridianCity,\
            'route29south':route29south, 'viridianArea1':viridianArea1}

print(main(bedroom,modules)) #runs the game
