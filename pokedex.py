from moves import *

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
            self.HP = self.HP + (self.stats['defense'])//15 - damage

    def useMove(self, index): #uses the indicated move
        x = self.moves[index][0]
        return x(self.stats['attack'])

    def statDam(self, damage, stat): #reduces the appropriate stat when stat damage is taken
        if damage == 0:
            print('but it missed!')
        elif self.stats[str(stat)] <10:
            print(str(self.name)+'\'s', stat,'can\'t be reduced anymore!')
        else:
            print(str(self.name)+'\'s',str(stat),'fell!')
            oldStat = self.stats[str(stat)]
            self.stats[str(stat)] = self.stats[str(stat)] + (self.stats['defense'])//30 - damage
            if self.stats[str(stat)]>oldStat:
                self.stats[str(stat)] = oldStat

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
        
class pokedex: #fills the global pokedex
    def __init__(self):
        self.squirtle = pokemon('Squirtle', 5, ['water','water'], 50, {'attack':50,'defense':40, 'speed':40}, {1:[tackle, 'tackle'],2:[tailWhip, 'tail whip']}, 100, 100, 1.0)
        self.charmander = pokemon('Charmander', 5, ['fire','fire'], 40, {'attack':70, 'defense':30, 'speed':60}, {1:[scratch,'scratch'], 2:[leer,'leer']}, 100, 100, 1.0)
        self.bulbasaur = pokemon('Bulbasaur',5, ['grass','poison'], 60, {'attack':30, 'defense':30, 'speed':30}, {1:[tackle, 'tackle'], 2:[leer, 'leer']}, 100, 100, 1.0)
        self.pidgey = pokemon('Pidgey', 5, ['normal','flying'], 30, {'attack':70, 'defense':50, 'speed':50}, {1:[wingAttack, 'wing attack'], 2:[gust, 'gust']}, 50, 60, 1.0)

pokedex = pokedex() #actually creates the pokedex

def typeChart(defendType, attackType):
    base = 1
    noEffect = 0
    notVeryEffective = 0.5
    superEffective = 2
    types = {'normal':{'fighting':superEffective, 'ghost':noEffect},\
             'fighting':{'flying':superEffective,'rock':notVeryEffective,'bug':notVeryEffective,'psychic':superEffective},\
             'flying':{'fighting':notVeryEffective,'ground':noEffect,'rock':superEffective,'bug':notVeryEffective,'grass':notVeryEffective, 'electric':superEffective, 'ice':superEffective},\
             'poison':{'fighting':notVeryEffective, 'poison':notVeryEffective, 'ground':superEffective,'bug':superEffective,'grass':notVeryEffective, 'psychic':superEffective},\
             'ground':{'poison':notVeryEffective, 'rock':notVeryEffective, 'water':superEffective, 'grass':superEffective, 'electric':noEffect, 'ice':superEffective},\
             'rock':{'normal':notVeryEffective, 'fighting':superEffective, 'flying':notVeryEffective, 'poison':notVeryEffective, 'ground':superEffective, 'fire':notVeryEffective, 'water':superEffective, 'grass':superEffective},\
             'bug':{'fighting':notVeryEffective, 'flying':superEffective, 'poison':superEffective, 'ground':notVeryEffective, 'rock':superEffective, 'fire':superEffective, 'grass':notVeryEffective},\
             'ghost':{'normal':noEffect, 'fighting':noEffect, 'poison':notVeryEffective, 'bug':notVeryEffective, 'ghost':superEffective},\
             'fire':{'ground':superEffective, 'rock':superEffective, 'bug':notVeryEffective, 'fire':notVeryEffective, 'water':superEffective, 'grass':notVeryEffective},\
             'water':{'fire':notVeryEffective, 'water':notVeryEffective, 'grass':superEffective, 'electric':superEffective, 'ice':notVeryEffective},\
             'grass':{'flying':superEffective, 'poison':superEffective, 'ground':notVeryEffective, 'bug':superEffective, 'fire':superEffective, 'water':notVeryEffective, 'grass':notVeryEffective, 'electric':notVeryEffective, 'ice':superEffective},\
             'electric':{'flying':notVeryEffective, 'ground':superEffective, 'electric':notVeryEffective},\
             'psychic':{'fighting':notVeryEffective, 'bug':superEffective, 'ghost':noEffect, 'psychic':notVeryEffective},\
             'ice':{'fighting':superEffective, 'rock':superEffective, 'fire':superEffective, 'ice':notVeryEffective},\
             'dragon':{'fire':notVeryEffective, 'water':notVeryEffective, 'grass':notVeryEffective, 'electric':notVeryEffective, 'ice':superEffective, 'dragon':superEffective}}
    if attackType in types[defendType]:
        return types[defendType][attackType]
    else:
        return base
    
def printChart():
    types = ['normal','fighting','flying','poison','ground','rock','bug','ghost','fire','water','grass','electric','psychic','ice','dragon']
    print('      ', end = ' ')
    for poke in types:
        spacing = 8 - len(poke)
        if poke == 'dragon':
            print(poke)
        else:
            print(poke+' '*spacing, end = " ")
    for poke in types:
        spacing = 8 - len(poke)
        print(poke+' '*spacing, end = "")
        for poke1 in types:
            x = typeChart(poke1, poke)
            digSpace = 4 - len(str(x))
            if poke1 == 'dragon':
                print('   ',x,' '*digSpace)
            else:
                print('   ',x,' '*digSpace, end ="")
        
