from random import randrange
import random
jmeno_hrdiny = input("Zadej jméno hrdiny: ")
penize = 0
zivoty = randrange(10, 31)
utok = 5
obrana = 0
krysa_utok = 5
krysa_obrana = 0
krysa_zivoty = 25


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


print(f"""Tvůj hrdina se jmenuje {jmeno_hrdiny}, má {zivoty} životů a {penize} penez.
Nachází se ve městě Lotaru. Je zde kovárna a aréna""")
cesta = input("Kam chceš jít? (napiš Kovárna nebo arena) ")
if cesta == "Kovárna":
    print("Vešel jsi do kovárny. WIP")
elif cesta == "arena":
    print("Vítej v aréně!")
    print(jmeno_hrdiny, " bojuje proti kryse")
    #Tady začíná souboj s krysou
    zraneni_enemy, zraneni_player = boj(utok, obrana, krysa_utok, krysa_obrana)
    print(f"Zranění nepřítele je {zraneni_enemy}")
    print(f"Zranění hráče je {zraneni_player}")
    zivoty = zivoty - zraneni_player
    krysa_zivoty = krysa_zivoty - zraneni_enemy
    print(f"Máš {zivoty} životů") 
    print(f"Krysa má {krysa_zivoty} životů")
    while zivoty > 0:
        if krysa_zivoty > 0:
            zraneni_enemy, zraneni_player = boj(utok, obrana, krysa_utok, krysa_obrana)
            print(f"Zranění nepřítele je {zraneni_enemy}")
            print(f"Zranění hráče je {zraneni_player}")
            zivoty = zivoty - zraneni_player
            krysa_zivoty = krysa_zivoty - zraneni_enemy
            print(f"Máš {zivoty} životů") 
            print(f"Krysa má {krysa_zivoty} životů")
        else: 
            print("Vyhrál jsi!")
            break
    else:
        print("Prohrál jsi!")
# Tady končí souboj s krysou
else:
    print("Nerozumím! Posral jsi to!")





