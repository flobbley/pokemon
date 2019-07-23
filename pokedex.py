from moves import *
import copy

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
    def __init__(self,name,level,typ,maxHP,stats, moves, baseXP,needXP, XPmod):
        self.name = name
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

    def damageTaken(self, damage): #reduces the HP when damage is taken
        if damage == 0:
            self.HP = self.HP
        else:
            self.HP -= damage

    def useMove(self, index, opponent): #uses the indicated move
        x = self.moves[index][0]
        x(self, opponent)

    def statDam(self, damage, stat): #reduces the appropriate stat when stat damage is taken
        if damage == 0:
            print('but it missed!')
        elif self.tempStats[str(stat)] <10:
            print(str(self.name)+'\'s', stat,'can\'t be reduced anymore!')
        else:
            print(str(self.name)+'\'s',str(stat),'fell!')
            oldStat = self.tempStats[str(stat)]
            self.tempStats[str(stat)] = self.tempStats[str(stat)] + (self.tempStats['defense'])//30 - damage
            if self.tempStats[str(stat)]>oldStat:
                self.tempStats[str(stat)] = oldStat

    def XPGain(self, opponent):
        gain = opponent.baseXP
        self.gainedXP += gain
        print(self.name,'gained',gain,'experience!')
        if self.gainedXP >= self.needXP:
            self.level += 1
            print(self.name, 'grew to level', str(self.level)+'!')
            self.gainedXP = 0
            newXP = self.needXP*1.3
            self.needXP = newXP
            self.levelUp()

    def levelUp(self):
        self.maxHP += 2
        self.stats['attack'] += 2
        self.stats['defense'] +=2
        self.stats['speed'] += 2
        self.tempStats['attack'] += 2
        self.tempStats['defense'] += 2
        self.tempStats['speed'] += 2

    def statRestore(self):
        self.tempStats = copy.deepcopy(self.stats)

    def heal(self, amount):
        self.HP += amount
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        
class pokedex: #fills the global pokedex
    def __init__(self):
        self.squirtle = pokemon('Squirtle', 5, ['water','water'], 50, {'attack':50,'defense':40, 'speed':40},\
                                {1:[tackle, 'tackle'],2:[tailWhip, 'tail whip'],3:[bubble,'bubble']}, 100, 100, 1.0)
        self.charmander = pokemon('Charmander', 5, ['fire','fire'], 40, {'attack':70, 'defense':30, 'speed':60},\
                                  {1:[scratch,'scratch'], 2:[leer,'leer'], 3:[ember,'ember']}, 100, 100, 1.0)
        self.bulbasaur = pokemon('Bulbasaur',5, ['grass','poison'], 60, {'attack':30, 'defense':30, 'speed':30},\
                                 {1:[tackle, 'tackle'], 2:[leer, 'leer'],3:[leechSeed, 'leech seed']}, 100, 100, 1.0)
        self.pidgey = pokemon('Pidgey', 5, ['normal','flying'], 30, {'attack':70, 'defense':50, 'speed':50},\
                              {1:[wingAttack, 'wing attack'], 2:[gust, 'gust']}, 50, 60, 1.0)

pokedex = pokedex() #actually creates the pokedex
