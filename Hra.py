from random import randrange
import random
jmeno_hrdiny = input("Zadej jméno hrdiny: ")
penize = 0
zivoty = randrange(10, 31)
utok = 5
obrana = 0
krysa = ["Krysa", 1, 0, 10] # 0. jméno, 1. útok, 2. obrana, 3. životy
bandita = ["Bandita", 10, 3, 30]
medved = ["Medvěd", 8, 2, 15]
nepritel = [krysa, bandita, medved]


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
    get_nepritel = random.choice(nepritel)
    print(f"{jmeno_hrdiny} bojuje proti {get_nepritel[0]}")
    #Tady začíná souboj 
    zivoty_nepritel = get_nepritel[3]
    while zivoty > 0:
        if zivoty_nepritel > 0:
            zraneni_enemy, zraneni_player = boj(utok, obrana, get_nepritel[1], get_nepritel[2])
            print(f"Zranění nepřítele je {zraneni_enemy}")
            print(f"Zranění hráče je {zraneni_player}")
            zivoty = zivoty - zraneni_player
            zivoty_nepritel = zivoty_nepritel - zraneni_enemy
            print(f"Máš {zivoty} životů") 
            print(f"{get_nepritel[0]} má {zivoty_nepritel} životů")
        else: 
            print("Vyhrál jsi!")
            penize = + 10
            break
    else:
        print("Prohrál jsi!")
# Tady začíná souboj
else:
    print("Nerozumím! Posral jsi to!")





