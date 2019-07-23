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

def damage(attacker, defender, power):
    a = (2*attacker.level)/5+2
    b = power*attacker.tempStats['attack']/defender.tempStats['defense']
    c = a*b/50+2
    return c
    
def scratch(attacker, defender):
    """
    Main damage attack, right now all the other physical attacks are clones of this
    """
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def tailWhip(attacker, defender):
    """
    main defense damaging attack, right now all the other stat damage attacks are clones of this
    """
    if hit(95)==True:
        defDam = (attacker.stats['attack'])//5
        defender.statDam(defDam, 'defense')
        return attacker, defender
    else:
        print('but it missed!')
        return attacker, defender

def tackle(attacker, defender):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leer(attacker, defender):
    if hit(95)==True:
        defDam = (attacker.stats['attack'])//5
        defender.statDam(defDam, 'defense')
    else:
        print('but it failed!')

def wingAttack(attacker, defender):
    damageType = 'normal'
    power = 40
    if hit(95) == True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def gust(attacker, defender):
    power = 40
    damageType = 'flying'
    if hit(95)==True: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def bubble(attacker, defender):
    damageType = 'water'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')
        
def ember(attacker, defender):
    damageType = 'fire'
    power = 40
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        defender.damageTaken(round(damageDone))
    else:
        print('but it missed!')

def leechSeed(attacker, defender):
    damageType = 'grass'
    power = 25
    if hit(95) == True:
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damageDone = damage(attacker, defender, power)
        damageDone *= damageMod
        before = attacker.HP
        defender.damageTaken(round(damageDone))
        attacker.heal(damageDone//2)
        after = attacker.HP
        battleDisplay(attacker, defender)
        print(attacker.name,'healed itself', after-before, 'HP!')
    else:
        print('but it missed!')
                        
