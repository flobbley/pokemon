from random import *
import os

global clearVar
syst = os.name
if syst == 'nt':
    clearVar = "cls"
else:
    clearVar = "clear"

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
        

def typeMod(damageType, attackerType, defenderType):
    """
    returns the damage multiplier based on attack type, attacker type, and defender type
    damage type; string
    attacker type; list of two strings
    defender type; list of two strings
    """
    base = 1
    if damageType in attackerType:
        base *= 1.5
    effectiveMod = typeChart(defenderType[0], damageType)
    if defenderType[0] != defenderType[1]:
        effMod2 = typeChart(defenderType[1], damageType)
        effectiveMod *= effMod2
    if effectiveMod > 1:
        print('It\'s super effective!')
    elif effectiveMod == 0:
        print('It had no effect!')
    elif effectiveMod <1 and effectiveMod>0:
        print('it wasn\'t very effective...')
    base *= effectiveMod
    return base

def battleDisplay(playerPoke, opponentPoke):
    """
    Will display sprites and HP bars
    """
    print(str(opponentPoke.name),str(opponentPoke.level), 'HP:'+opponentPoke.HPBar(),str(opponentPoke.HP)+'/'+str(opponentPoke.maxHP))
    print(str(playerPoke.name),str(playerPoke.level), 'HP:'+playerPoke.HPBar(),str(playerPoke.HP)+'/'+str(playerPoke.maxHP))

def hit(percent):
    didHit = randint(1,100)
    if didHit <= percent:
        return True
    else:
        return False

def damage(attacker, defender, power, attackStat, defenseStat):
    a = (2*attacker.level)/5+2
    b = power*attacker.tempStats[attackStat]/defender.tempStats[defenseStat]
    c = a*b/50+2
    return c
    
def scratchAttack(attacker, defender, computer):
    """
    Main damage attack, right now all the other physical attacks are clones of this
    """
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack', 'defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def tailWhipAttack(attacker, defender, computer):
    """
    main defense damaging attack, right now all the other stat damage attacks are clones of this
    """
    if hit(95)==True:
        defender.statChange('defense', False)
    else:
        print('but it missed!')

def tackleAttack(attacker, defender, computer):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack', 'defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leerAttack(attacker, defender, computer):
    if hit(95)==True:
        defender.statChange('defense', False)
    else:
        print('but it failed!')

def wingAttackAttack(attacker, defender, computer):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack', 'defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def gustAttack(attacker, defender, computer):
    power = 40
    damageType = 'flying'
    if hit(95)==True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power,'attack','defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def bubbleAttack(attacker, defender, computer):
    damageType = 'water'
    power = 40
    if hit(95) == True:
        if randint(1,10) == 5:
            defender.statChange('speed', False)
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power,'sp.attack','sp.defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')
        
def emberAttack(attacker, defender):
    damageType = 'fire'
    power = 40
    if hit(95) == True:
        if 'burn' not in defender.status:
            if randint(1,10) == 5:
                defender.status.append('burn')
                print(defender.name,'was burned!')
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'sp.attack','sp.defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leechSeedAttack(attacker, defender, computer):
    damageType = 'grass'
    if 'grass' in defender.typ:
        print(defender.name,'was not affected')
    else:
        if 'leech' not in defender.status:
            print(defender.name,'was seeded')
            defender.status.append('leech')
        else:
            print('There was no effect')

def quickAttackAttack(attacker, defender, computer):
    damageType = 'normal'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack','defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def poisonStingAttack(attacker, defender, computer):
    damageType = 'poison'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        if damageMod != 0 and 'poison' not in defender.status:
            if randint(1,10) == 5:
                defender.status.append('poison')
                print(defender.name,'was poisoned!')
            damageDone = damage(attacker, defender, power, 'attack', 'defense')
            damageDone *= damageMod
            defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def stringShotAttack(attacker, defender, computer):
    if hit(95)==True:
        defender.statChange('speed', False)
    else:
        print('but it missed!')

def hardenAttack(attacker, defender, computer):
    attacker.statChange('defense',True)

def twinNeedleAttack(attacker, defender, computer):
    damageType = 'bug'
    power = 25
    input()
    for i in range(2):
        os.system(clearVar)
        if computer == True:
            battleDisplay(defender,attacker)
        else:
            battleDisplay(attacker,defender)
        if hit(95) == True:
            damageMod = typeMod(damageType, attacker.typ, defender.typ)
            if damageMod != 0:
                if i == 0:
                    print('first strike hit!')
                    input()
                if i == 1:
                    print('second strike hit!')
                if 'poison' not in defender.status:
                    if randint(1,5) == 5:
                        defender.status.append('poison')
                        print(defender.name,'was poisoned!')
                damageMod = typeMod(damageType, attacker.typ, defender.typ)
                damageDone = damage(attacker, defender, power, 'attack', 'defense')
                damageDone*=damageMod
                defender.damageTaken(round(damageDone))
            
        else:
            if i == 0:
                print('first strike missed!')
                input()
            if i == 1:
                print('second strike missed!')

def confusionAttack(attacker, defender, computer):
    damageType = 'psychic'
    power = 50
    if hit(95) == True:
        if 'confusion' not in defender.status:
            if randint(1,10) == 5:
                defender.status.append('confusion')
                print(defender.name,'became confused!')
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'sp.attack', 'sp.defense')
        damageDone*=damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def thundershockAttack(attacker, defender, computer):
    damageType = 'electric'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        if damageMod != 0:
            if 'paralyzed' not in defender.status:
                if randint(1,10) == 5:
                    defender.status.append('paralyzed')
                    print(defender.name,'became paralyzed!')
            damageDone = damage(attacker, defender, power, 'sp.attack', 'sp.defense')
            damageDone*=damageMod
            defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')
    
class move:
    def __init__(self, name, priority, duration, technique):
        self.name = name
        self.priority = priority
        self.technique = technique
        self.duration = duration
        
    def useMove(self, attacker, defender, computer = False):
        print(attacker.name,'used',self.name+'!')
        return self.technique(attacker, defender, computer)


scratch = move('scratch',0,0,scratchAttack)
tackle = move('tackle',0,0,tackleAttack)
leer = move('leer',0,0,leerAttack)
tailWhip = move('tail whip',0,0,tailWhipAttack)
wingAttack = move('wing attack',0,0,wingAttackAttack)
gust = move('gust',0,0,gustAttack)
bubble = move('bubble',0,0,bubbleAttack)
ember = move('ember',0,0,emberAttack)
leechSeed = move('leech seed',0,0,leechSeedAttack)
quickAttack = move('quick attack',1,0,quickAttackAttack)
poisonSting = move('poison sting',0,0,poisonStingAttack)
stringShot = move('string shot',0,0,stringShotAttack)
harden = move('harden',0,0,hardenAttack)
twinNeedle = move('twin needle',0,0,twinNeedleAttack)
confusion = move('confusion',0,0,confusionAttack)
thundershock = move('thunder shock',0,0,thundershockAttack)
