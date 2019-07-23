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
    base *= effectiveMod
    return base

def scratch(attacker, defender):
    """
    Main damage attack, right now all the other physical attacks are clones of this
    """
    hit = randint(1,100)
    damageType = 'normal'
    if hit <=95: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damage = 10+(attacker.tempStats['attack'])//10
        damage *= damageMod
        defender.damageTaken(damage)
    else:
        print('but it missed!')

def tailWhip(attacker, defender):
    """
    main defense damaging attack, right now all the other stat damage attacks are clones of this
    """
    hit = randint(1,100)
    if hit <= 95:
        defDam = (attacker.stats['attack'])//5
        defender.statDam(defDam, 'defense')
        return attacker, defender
    else:
        print('but it missed!')
        return attacker, defender

def tackle(attacker, defender):
    hit = randint(1,100)
    damageType = 'normal'
    if hit <=95: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damage = 10+(attacker.tempStats['attack'])//10
        damage *= damageMod
        defender.damageTaken(damage)
    else:
        print('but it missed!')

def leer(attacker, defender):
    hit = randint(1,100)
    if hit <= 95:
        defDam = (attacker.stats['attack'])//5
        defender.statDam(defDam, 'defense')
    else:
        print('but it failed!')

def wingAttack(attacker, defender):
    hit = randint(1,100)
    damageType = 'normal'
    if hit <=95: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damage = 10+(attacker.tempStats['attack'])//10
        damage *= damageMod
        defender.damageTaken(damage)
    else:
        print('but it missed!')

def gust(attacker, defender):
    hit = randint(1,100)
    damageType = 'flying'
    if hit <=95: #95% hit rate
        damageMod = typeMod(damageType, attacker.typ, defender.typ)
        damage = 10+(attacker.tempStats['attack'])//10
        damage *= damageMod
        defender.damageTaken(damage)
    else:
        print('but it missed!')
