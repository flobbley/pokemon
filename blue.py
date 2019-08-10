
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
                        print('Scientist: "Well hello there',player.name+'!',' Looking for Professor Oak? We haven\'t seen him all morning."')
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

def viridianWild(player, patches):
    wild = trainer('Wild', [], {}, 10)
    caterpie1 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie2 = pokemonGenerator(pokedex.caterpie,3,[tackle, stringShot])
    caterpie3 = pokemonGenerator(pokedex.caterpie,4,[tackle, stringShot])
    caterpie4 = pokemonGenerator(pokedex.caterpie,2,[tackle, stringShot])
    weedle1 = pokemonGenerator(pokedex.weedle,3,[poisonSting, stringShot])
    weedle2 = pokemonGenerator(pokedex.weedle,2,[poisonSting, stringShot])
    weedle3 = pokemonGenerator(pokedex.weedle,4,[poisonSting, stringShot])
    kakuna1 = pokemonGenerator(pokedex.kakuna,5,[tackle, harden])
    pikachu1 = pokemonGenerator(pokedex.pikachu,4,[tackle, tailWhip])
    encounters = [caterpie1, caterpie2, caterpie3, caterpie4, weedle1, weedle2, weedle3, kakuna1, pikachu1]
    chance = [True, False]
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
        else:
            print('No pokemon this time!')
            input()
    return True

def viridianArea1(player):
    while True:
        os.system(clearVar)
        print('AREA 1')
        print('You find yourself at the entrance of the Veridian Forest, it\'s dark, and kinda scary') 
        print('you see a man who looks like he\'s itching for a fight, as well as a patch of tall grass')
        print('to the north you see the path continue into the forest')
        action = menuSelect('What do you want to do?',['Talk to man','Enter the grass','Continue into the forest (AREA 2)','Go back to Veridian City','Menu'])
        if action == 1: 
            won = trainerEncounter(player,gameState.trainers.viridianTrainers.bugCatcherDoug, "I\'m here to catch all kinds of bugs!","But all I can find are caterpies and weedles")
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            print('You enter the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
        elif action == 3:
            return 'viridianArea2north'
        elif action == 4:
            return 'viridianCity'
        else:
            menu(player)
            
def viridianArea2north(player):
    while True:
        os.system(clearVar)
        print('AREA 2')
        print('Moving north up the path you see two what seem to be two trainers on either side of the path,')
        print('one is wearing shorts, the other has a bug net.')
        print('It looks like you can\'t get by without fighting one, but you won\'t have to fight both')
        print('Either way, you\'ll have to pass through some tall grass to get to them')
        action = menuSelect('What would you like to do?',['Fight the one in shorts (AREA 3)','Fight the one with the net (AREA 3)','Go back (AREA 1)','Menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterJoey,\
                                   '"I like shorts, they\'re comfy and easy to wear!"',\
                                   '"Maybe not the best idea in the forest though..."')
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea3'
        elif action == 2:
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherLouis,\
                                   '"Help! I got lost and can\'t find my way out!"',\
                                   '"Why did you do that?? How am I supposed to get out now??"')
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea3'
                                   
        elif action == 3:
            return 'viridianArea1'
        else:
            menu(player)

def viridianArea2south(player):
    while True:
        os.system(clearVar)
        print('AREA 2')
        print('Moving south down the path you see two what seem to be two trainers on either side of the path,')
        print('one is wearing shorts, the other has a bug net.')
        print('It looks like you can\'t get by without fighting one, but you won\'t have to fight both')
        print('Either way, you\'ll have to pass through some tall grass to get to them')
        action = menuSelect('What would you like to do?',['Fight the one in shorts (AREA 1)','Fight the one with the net (AREA 1)','Go back (AREA 3)','Menu'])#enter question here, along with the list of possible answers
        if action == 1: #the number of actions will equal the number of possible answers in the last line
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterJoey,\
                                   '"I like shorts, they\'re comfy and easy to wear!"',\
                                   '"Maybe not the best idea in the forest though..."')
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea1'
        elif action == 2:
            print('you start to move through the tall grass...')
            input()
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherLouis,\
                                   '"Help! I got lost and can\'t find my way out!"',\
                                   '"Why did you do that?? How am I supposed to get out now??"')
            if won == False:
                return gameState.lastPokecenter
            else:
                return 'viridianArea1'
                                   
        elif action == 3:
            return 'viridianArea3'
        else:
            menu(player)

def viridianArea3(player):
    while True:
        os.system(clearVar)
        print('AREA 3')
        print('You find yourself standing in a small clearing in the forest')
        print('Across the clearing you see a girl, to the west you see a small opening in the trees,')
        print('to the south you see the path towards Virdian City, to the north you see the path toward Pewter City')
        action = menuSelect('What would you like to do?',['Talk to the girl','Go into the opening','Go down the south path','Go down the north path','Menu'])
        if action == 1:
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.youngsterLiz,\
                                   '"I\'m itching for a fight! I\'ve put together a diverse team that can\'t lose!"',\
                                   '"hmm, maybe I\'ll need something better than pidgeys and ratatas..."')
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            print('you enter into the opening')
            input()
            print('It\'s filled with wild pokemon! you may have to fight your way out!')
            passed = viridianWild(player, 3)
            if passed == False:
                return gameState.lastPokecenter
            return 'viridianArea3'
                                   
        elif action == 3:
            return 'viridianArea2south'
        elif action == 4:
            return 'viridianArea4north'
        else:
            menu(player)

def viridianArea4north(player):
    while True:
        os.system(clearVar)
        print('AREA 4')
        print('There is a long dark path ahead of you, filled with tall grass.')
        print('down th way there is a girl blocking the whole path, if she wants to battle there\'s no way to avoid her')
        action = menuSelect('What would you like to do?',['Go down the path','Go back','Menu'])
        if action == 1:
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherKim,\
                                   '"Where do you think yer going pip squeak?"',\
                                   '"Eek! my bugs!"')
            if won == False:
                return gameState.lastPokecenter
            passed = viridianWild(player, 2)
            if passed == False:
                return gameState.lastPokecenter
            return 'pewterCity'
        
        elif action == 2:
            return 'viridianArea3'
        else:
            menu(player)

def viridianArea4south(player):
    while True:
        os.system(clearVar)
        print('AREA 4')
        print('There is a long dark path ahead of you, filled with tall grass.')
        print('down th way there is a girl blocking the whole path, if she wants to battle there\'s no way to avoid her')
        action = menuSelect('What would you like to do?',['Go down the path','Go back','Menu'])
        if action == 1:
            passed = viridianWild(player, 1)
            if passed == False:
                return gameState.lastPokecenter
            won = trainerEncounter(player, gameState.trainers.viridianTrainers.bugCatcherKim,\
                                   '"Where do you think yer going pip squeak?"',\
                                   '"Eek! my bugs!"')
            if won == False:
                return gameState.lastPokecenter
            passed = viridianWild(player, 2)
            if passed == False:
                return gameState.lastPokecenter
            return 'viridianArea3'
        
        elif action == 2:
            return 'pewterCity'
        else:
            menu(player)

"""
Pewter City
"""

def pewterCity(player):
    while True:
        os.system(clearVar)
        print('Pewter City! home to Brock\'s famous Rock Type Gym. If you think you\'re strong enough, maybe you can challenge him!')
        print('To the south there is a road that leads in to the Viridian Forest.')
        action = menuSelect('Where would your like to go?',['Pokecenter','Pokemart','Pokemon Gym','Into the Viridian Forest','Menu'])
        if action == 1:
            gameState.lastPokecenter = 'pewterCity'
            pokeCenter(player)
        elif action == 2:
            itemShop(player)
        elif action == 3:
            return 'rockGym'
        elif action == 4:
            return 'viridianArea4south'
        else:
            menu(player)

def rockGym(player):
    while True:
        os.system(clearVar)
        print('You enter the Rock Gym, it\'s dark, you can hardly see a thing.')
        input()
        print('Ahead you see another trainer, they could be looking for a fight, but you could probably sneak past')
        print('past them you can see Brock, he seems to be just waiting for a challenger')
        action = menuSelect('What would you like to do?',['Fight the trainer','Sneak past and go to brock','Leave','Menu'])
        if action == 1:
            won = trainerEncounter(player, gameState.trainers.pewterTrainers.juniorTrainerRodney,\
                                   '"Did you come to challenge Brock? don\'t bother! I\'ll make short work of you"',\
                                   '"Still, you\'re no match for brock"')
            if won == False:
                return gameState.lastPokecenter
        elif action == 2:
            won = trainerEncounter(player, gameState.trainers.pewterTrainers.brock,\
                                   '"So you want to learn about rock type pokemon eh? Our superior defense will grind you down!"',\
                                   '"Well done! it\'s not often that I\'m beaten. Now I present you with the Boulder Badge!"')
            if won == False:
                return gameState.lastPokecenter
            if 'Boulder Badge' not in player.badges:
                player.badges.append('Boulder Badge')
        elif action == 3:
            return 'pewterCity'
        else:
            menu(player)

ashPidgey = pokemonGenerator(pokedex.pidgey, 4, [tackle, gust])
garyPidgey = pokemonGenerator(pokedex.pidgey,4,[tackle, gust])
ashBulbasaur = pokemonGenerator(pokedex.bulbasaur,30,[tackle,bide,thunderWave])
garyBulbasaur = pokemonGenerator(pokedex.bulbasaur, 5, [tackle, leer])
ashSquirtle = pokemonGenerator(pokedex.squirtle, 15, [tackle, tailWhip, bubble])
garyCharmander = pokemonGenerator(pokedex.charmander, 30, [tackle])
garySquirtle = pokemonGenerator(pokedex.squirtle, 30, [tailWhip])
ashCharmander = pokemonGenerator(pokedex.charmander, 5, [scratch, tailWhip])
ashBeedrill = pokemonGenerator(pokedex.beedrill,15,[twinNeedle,poisonSting],1.5)
ashPikachu = pokemonGenerator(pokedex.pikachu, 7, [thundershock])
ashBulbasaur.status.append('sleep')
garyCharmander.status.append('confusion')

ash = trainer('ash', [ashBulbasaur], [['Pokeball',5],['Potion',5]], 500)
gary = trainer('gary', [garyCharmander], [], 10)

"""
main game area
"""

modules = {'bedroom':bedroom, 'momsHouse':momsHouse, 'lab':lab, 'garysHouse':garysHouse, 'route29north':route29north, 'palletTown':palletTown, 'viridianCity':viridianCity,\
            'route29south':route29south, 'viridianArea1':viridianArea1, 'viridianArea2north':viridianArea2north, 'viridianArea2south':viridianArea2south, 'viridianArea3':viridianArea3,\
           'viridianArea4north':viridianArea4north,'viridianArea4south':viridianArea4south, 'pewterCity':pewterCity, 'rockGym':rockGym}

print(battle(ash, gary, False))
#print(main(bedroom,modules)) #runs the game
