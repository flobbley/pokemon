from random import *

def scratch(attack):
    """
    Main damage attack, right now all the other physical attacks are clones of this
    """
    damType = 'HP'
    hit = randint(1,100)
    if hit <=95: #95% hit rate
        damage = 10+(attack)//10
        return damage, damType
    else:
        print('but it missed!')
        return 0, damType

def tailWhip(attack):
    """
    main defense damaging attack, right now all the other stat damage attacks are clones of this
    """
    damType = 'defense'
    hit = randint(1,100)
    if hit <= 95:
        defdam = (attack)//5
        return defdam, damType
    else:
        return 0, damType

def tackle(attack):
    damType = 'HP'
    hit = randint(1,100)
    if hit <=95:
        damage = 10+(attack)//10
        return damage, damType
    else:
        print('but it missed!')
        return 0, damType

def leer(attack):
    damType = 'defense'
    hit = randint(1,100)
    if hit <= 95:
        defdam = (attack)//5
        return defdam, damType
    else:
        return 0, damType

def wingAttack(attack):
    damType = 'HP'
    hit = randint(1,100)
    if hit <=95:
        damage = 10+(attack)//10
        return damage, damType
    else:
        print('but it missed!')
        return 0, damType

def gust(attack):
    damType = 'HP'
    hit = randint(1,100)
    if hit <=95:
        damage = 10+(attack)//10
        return damage, damType
    else:
        print('but it missed!')
        return 0, damType
