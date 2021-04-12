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
bandita = ["Bandita", 10, 3, 30, 60,[["bandití ocas", 0, 1, False, "item"], ["bandití zub", 0, 1, False, "item"], ["bandití bobek", 0, 1, False, "item"]]]
medved = ["Medvěd", 8, 2, 15, 40,[["medvědí ocas", 0, 1, False, "item"], ["medvědí zub", 0, 1, False, "item"], ["medvědí bobek", 0, 1, False, "item"]]]
nepritel = [krysa]





while zivoty > 0:
    #Zisk nového lvl
    if xp >= 100: 
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

        (zivoty, xp, inventory_list) = Funkce.fight(nepritel, zivoty, utok, obrana, jmeno_hrdiny, xp, inventory_list)

        
    # Tady začíná souboj
    else:
        print("Nerozumím! Posral jsi to!")





