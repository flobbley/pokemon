from random import *

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
    print(str(opponentPoke.name), 'HP:'+opponentPoke.HPBar(),str(opponentPoke.HP)+'/'+str(opponentPoke.maxHP))
    print(str(playerPoke.name),'HP:'+playerPoke.HPBar(),str(playerPoke.HP)+'/'+str(playerPoke.maxHP))

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
    
def scratchAttack(attacker, defender):
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

def tailWhipAttack(attacker, defender):
    """
    main defense damaging attack, right now all the other stat damage attacks are clones of this
    """
    if hit(95)==True:
        defender.statChange('defense', False)
    else:
        print('but it missed!')

def tackleAttack(attacker, defender):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack', 'defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leerAttack(attacker, defender):
    if hit(95)==True:
        defender.statChange('defense', False)
    else:
        print('but it missed!')

def wingAttackAttack(attacker, defender):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack', 'defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def gustAttack(attacker, defender):
    power = 40
    damageType = 'flying'
    if hit(95)==True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power,'attack','defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def bubbleAttack(attacker, defender):
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
        if randint(1,10) == 5:
            defender.status.append('burn')
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'sp.attack','sp.defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leechSeedAttack(attacker, defender):
    damageType = 'grass'
    if 'grass' in defender.typ:
        print(defender.name,'was not affected')
    else:
        print(defender.name,'was seeded')
        defender.status.append('leech')

def quickAttackAttack(attacker, defender):
    damageType = 'normal'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power, 'attack','defense')
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')                 
class move:
    def __init__(self, name, priority, duration, technique):
        self.name = name
        self.priority = priority
        self.technique = technique
        self.duration = duration
        
    def useMove(self, attacker, defender):
        print(attacker.name,'used',self.name+'!')
        input()
        return self.technique(attacker, defender)


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
