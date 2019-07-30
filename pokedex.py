from moves import *
from random import *
import copy

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
        
class pokemon:
    """
    creates a pokemon

    takes a name as a string
    starting pokemon level; integer
    typ is the pokemon type; list of two entries; ['water', 'fire']
    takes maxHP as an integer
    takes stats as a dictionary formatted as {'attack':30, 'defense':40, 'speed': 40}
    takes moves as a dictionary formatted as {1:[tackle, 'tackle'],etc}
    baseXP is the base amount of XP the pokemon gives if killed; integer
    needXP is amount of XP needed to gain a level; integer
    XPmod is how much the gained XP is adjusted; two digit, single decimel place; 1.6 or 0.8 
    """
    def __init__(self,name, pokeNum, entry, level,typ,maxHP,stats, moves, baseXP,needXP, XPmod):
        self.name = name
        self.pokeNum = pokeNum
        self.entry = entry
        self.level = level
        self.typ = typ
        self.maxHP = maxHP
        self.stats = stats
        self.moves = moves
        self.HP = maxHP #sets current HP equal to max HP at creation
        self.baseXP = baseXP
        self.needXP = needXP
        self.XPmod = XPmod
        self.gainedXP = 0
        self.tempStats = copy.deepcopy(stats)
        self.status = []

    def getName(self): #gives the name of the pokemon
        print(self.name)

    def HPBar(self): #displays the current HP of the pokemon as a bar
        percentage = self.HP/self.maxHP
        remaining = round(20*percentage)
        taken = 20 - remaining
        return '('+'#'*remaining+'-'*taken+')'

    def getMoves(self): #returns the list of available moves
        for i in range(1,len(self.moves)+1):
            print(str(i)+'.', self.moves[i][1])
        print(str(i+1)+'. cancel')

    def learnMove(self, move):
        moveNo = len(self.moves)+1
        if moveNo<=4:
            self.moves[moveNo] = move
            print(self.name, 'learned', move[1]+'!')
            input()
        else:
            while True:
                print(self.name, 'is trying to learn', move[1],'but',self.name,'already knows four moves')
                print('Would you like to replace one of these moves?')
                self.getMoves()
                print('5. No, do not learn move')
                action = input()                
                if menuValid(action, 5):
                    action = int(action)
                    if action == 5:
                        print(self.name, 'did not learn', move[1])
                        break
                    else:
                        print(self.moves[action][1],'will be replaced with',move[1])
                        while True:
                            print('Are you sure? y/n')
                            sure = input()
                            if sure ==  'y' or sure == 'n':
                                break
                        if sure == 'y':
                            self.moves[action] = move
                            print(self.name, 'learned', self.moves[action][1]+'!')
                            break
            input()
                        

    def damageTaken(self, damage): #reduces the HP when damage is taken
        if damage == 0:
            self.HP = self.HP
        else:
            self.HP -= damage

    def useMove(self, index, opponent): #uses the indicated move
        x = self.moves[index][0]
        x(self, opponent)

    def statChange(self, stat, boost): #reduces the appropriate stat when stat damage is taken
        minstat = .131
        maxstat = 4
        ratio = self.tempStats[str(stat)]/self.stats[str(stat)]
        margin = 0.02
        if abs(ratio - minstat)<margin:
            print(str(self.name)+'\'s', stat,'can\'t be reduced anymore!')
        elif abs(ratio-maxstat)<margin:
            print(str(self.name)+'\'s',stat,'can\'t be increased anymore!')
        else:
            if boost:
                change = 'increased!'
                self.tempStats[str(stat)] *= 1.33
            else:
                change = 'decreased!'
                self.tempStats[str(stat)]*= 0.66
            print(self.name+'\'s',stat,change)

    def XPGain(self, opponent):
        gain = opponent.baseXP
        self.gainedXP += gain
        print(self.name,'gained',gain,'experience!')
        if self.gainedXP >= self.needXP:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        print(self.name, 'grew to level', str(self.level)+'!')
        self.gainedXP = 0
        newXP = self.needXP*1.3
        self.needXP = newXP
        self.maxHP += 2
        self.HP += 2
        self.stats['attack'] += 2
        self.stats['defense'] +=2
        self.stats['speed'] += 2
        self.tempStats['attack'] += 2
        self.tempStats['defense'] += 2
        self.tempStats['speed'] += 2
        if self.level in moveTree[self.name]:
            self.learnMove(moveTree[self.name][self.level])

    def statRestore(self):
        self.tempStats = copy.deepcopy(self.stats)

    def heal(self, amount):
        self.HP += amount
        if self.HP > self.maxHP:
            self.HP = self.maxHP
    

    def statusAction(self, opponent, position):
        """
        Performs the relevant status effects
        position is the place in the battle sequence it happens
        'before' = before the turn
        'during' = during the turn
        'after' = after the turn
        """
        act = []

        #non-exclusive statuses
        if 'leech' in self.status:
            if position == 'after':
                damage = self.maxHP//16+1
                self.damageTaken(damage)
                opponent.heal(damage)
                print(opponent.name,'absorbed health from',self.name)
                input()
        if 'burn' in self.status:
            if position == 'before':
                self.tempStats['attack'] = self.stats['attack']/2
            elif position == 'after':
                damage = self.maxHP//8
                self.damageTaken(damage)
                print(self.name, 'was hurt by the burn')

        
        #exclusive statuses
        elif 'paralyzed' in self.status:
            if position == 'before':
                print(self.name,'is paralyzed, it may not attack')
            elif position == 'during':    
                chance = [True,True,False]
                paralyze = choice(chance)
                if paralyze == False:
                    print(self.name, 'is fully paralyzed!')
                act.append(paralyze)
        
        elif 'sleep' in self.status:
            if position == 'before':
                print(self.name,'is asleep!')
            elif position == 'during':
                chance = [True,False,False]
                sleep = choice(chance)
                if sleep == True:
                    print(self.name,'woke up!')
                    act.append(True)
                else:
                    print(self.name,'is fast asleep')
                    act.append(False)
              
        return False not in act
    
class pokedex: #fills the global pokedex
    def __init__(self):
        self.squirtle = pokemon('Squirtle', 2, 'This pokemon likes to squirt water at people that get too close', 5, ['water','water'], 21, {'attack':14,'defense':15, 'speed':12},\
                                {1:[tackle, 'tackle'],2:[tailWhip, 'tail whip']}, 100, 100, 1.0)
        self.charmander = pokemon('Charmander', 3, 'This pokemon has a firey tail!', 5, ['fire','fire'], 19, {'attack':18, 'defense':12, 'speed':14},\
                                  {1:[scratch,'scratch'], 2:[leer,'leer']}, 100, 100, 1.0)
        self.bulbasaur = pokemon('Bulbasaur', 1, 'This pokemon has a large plant bulb on it\'s back', 5, ['grass','poison'], 24, {'attack':10, 'defense':16, 'speed':10},\
                                 {1:[tackle, 'tackle'], 2:[leer, 'leer']}, 100, 100, 1.0)
        self.pidgey = pokemon('Pidgey',4,'This pokemon is very common in large cities where people feed them', 5, ['normal','flying'], 16, {'attack':13, 'defense':13, 'speed':13},\
                              {1:[wingAttack, 'wing attack'], 2:[gust, 'gust']}, 50, 60, 1.0)
        self.ratata = pokemon('Ratata',5,'This pokemon has strong teeth, it has been known to chew through metal!', 5, ['normal','normal'],17,{'attack':14, 'defense':12, 'speed':13},\
                              {1:[tackle, 'tackle'],2:[tailWhip, 'tail whip']}, 50, 50, 1.0)
pokedex = pokedex() #actually creates the pokedex

moveTree = {'Squirtle':{6:[bubble, 'bubble']},\
            'Charmander':{6:[ember,'ember']},\
            'Bulbasaur':{6:[leechSeed, 'leech seed']},\
            'Pidgey':{},\
            'Ratata':{}}
