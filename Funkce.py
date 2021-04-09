from random import randrange
def boj(ut, ob, utN, obN):
    var_ob_player = ob + randrange(0, 6)
    var_ob_enemy = obN + randrange(0,6)
    zraneni_player = utN - var_ob_player #Zranění které dostal hrdina od nepřítele
    if zraneni_player < 0:
        zraneni_player = 0
    zraneni_enemy = ut - var_ob_enemy #Zranění které dostal nepřítel od hrdiny
    if zraneni_enemy < 0:
        zraneni_enemy = 0
    return (zraneni_enemy, zraneni_player)