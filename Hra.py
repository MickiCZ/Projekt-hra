from random import randrange
import random
import Funkce
import Obchod
#import keyboard
import Inventář

jmeno_hrdiny = input("Zadej jméno hrdiny: ")
inventory_list = []
equiped = []
penize = 0
zivoty = randrange(10, 31)
default_hp = zivoty
xp = 0
utok = 5
obrana = 0
lvl = 1

# 0. jméno, 1. útok, 2. obrana, 3. životy, 4. xp, 5. loot
krysa = ["Krysa", 1, 0, 10, 50,[["krysí ocas", 0, 1, False, "item"], ["krysí zub", 0, 1, False, "item"], ["krysí bobek", 0, 1, False, "item"]]]
bandita = ["Bandita", 10, 3, 30]
medved = ["Medvěd", 8, 2, 15]
nepritel = [krysa]





while zivoty > 0:
    if xp >= 100: #Zisk nového lvl
       (utok, zivoty, lvl, xp) = Funkce.level_up(xp, zivoty, utok, lvl)

    print(f"""Tvůj hrdina se jmenuje {jmeno_hrdiny}, je na {lvl}. úrovni. aktuálně má {zivoty} životů z maximálních {default_hp} životů, {penize} peněz a {xp} zkušeností.
    Nachází se ve městě Lotaru. Je zde kovárna a aréna""")
    cesta = input("Kam chceš jít? (napiš forge nebo arena nebo inv) ")
    if cesta == 'inv':
    	Inventář.inventory(inventory_list, equiped)

    elif cesta == "forge":
        print("Vešel jsi do kovárny.")
        penize = Obchod.buy_in_shop(penize, inventory_list)
        
    elif cesta == "arena":
        print("Vítej v aréně!")
        get_nepritel = random.choice(nepritel)
        print(f"{jmeno_hrdiny} bojuje proti {get_nepritel[0]}")
        #Tady začíná souboj 
        zivoty_nepritel = get_nepritel[3]
        while zivoty > 0:
            if zivoty_nepritel > 0:
                zraneni_enemy, zraneni_player = Funkce.boj(utok, obrana, get_nepritel[1], get_nepritel[2])
                print(f"Zranění nepřítele je {zraneni_enemy}")
                print(f"Zranění hráče je {zraneni_player}")
                zivoty = zivoty - zraneni_player
                zivoty_nepritel = zivoty_nepritel - zraneni_enemy
                print(f"Máš {zivoty} životů") 
                print(f"{get_nepritel[0]} má {zivoty_nepritel} životů")
            else: 
                print("Vyhrál jsi!")
                penize = penize + 100
                xp = xp + get_nepritel[4]
                loot = get_nepritel[5][randrange(0, len(get_nepritel[5]))]
                inventory_list.append(loot)
                print(f"Získal jsi: {loot[0]}!")
                break
        else:
            print("Prohrál jsi!")
    # Tady začíná souboj
    else:
        print("Nerozumím! Posral jsi to!")





