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
default_hp = randrange(10, 31)
hp = default_hp
xp = 0
utok = 5
obrana = 0
lvl = 1
#player stats:
# 0. jméno, 1. útok, 2. obrana. 3. def_životy, 
# 4. akt_životy, 5. lvl, 6. xp, 7. money, 
# 8. inventory, 9. equip
player = [jmeno_hrdiny, utok, obrana, default_hp, hp, lvl, xp, penize, inventory_list, equiped]
print("Vytvořil jsi hrdinu se jménem {}. Ten má útok: {} a obranu: {}. Životy: {}/{}. Aktuální lvl {} a zkušenosti: {}. Tvůj hrdina má {} peněz. V invetáří je: {} a vybaveno má: {}. Přeji příjemnou hru!".format(player[0],player[1],player[2],player[4],player[3],player[5],player[6],player[7],player[8],player[9]))

# 0. jméno, 1. útok, 2. obrana, 3. životy, 4. xp, 5. loot
krysa = ["Krysa", 1, 0, 10, 50,[["krysí ocas", 0, 1, False, "item"], ["krysí zub", 0, 1, False, "item"], ["krysí bobek", 0, 1, False, "item"]]]
bandita = ["Bandita", 10, 3, 30, 60,[["bandití ocas", 0, 1, False, "item"], ["bandití zub", 0, 1, False, "item"], ["bandití bobek", 0, 1, False, "item"]]]
medved = ["Medvěd", 8, 2, 15, 40,[["medvědí ocas", 0, 1, False, "item"], ["medvědí zub", 0, 1, False, "item"], ["medvědí bobek", 0, 1, False, "item"]]]
nepritel = [krysa]





while hp > 0:
    #Zisk nového lvl
    if xp >= 100: 
       (utok, default_hp, lvl, xp, hp) = Funkce.level_up(xp, default_hp, utok, lvl)

    print(f"""Tvůj hrdina se jmenuje {jmeno_hrdiny}, je na {lvl}. úrovni. aktuálně má {hp} životů z maximálních {default_hp} životů, {penize} peněz a {xp} zkušeností.
    Nachází se ve městě Lotaru. Je zde kovárna a aréna""")

    cesta = input("Kam chceš jít? (napiš forge nebo arena nebo inv) ")
    if cesta == 'inv':
    	Inventář.inventory(inventory_list, equiped)

    elif cesta == "forge":
        print("Vešel jsi do kovárny.")
        penize = Obchod.buy_in_shop(penize, inventory_list)
        
    elif cesta == "arena":
        print("Vítej v aréně!")

        (hp, xp, inventory_list) = Funkce.fight(nepritel, hp, utok, obrana, jmeno_hrdiny, xp, inventory_list)

        
    # Tady začíná souboj
    else:
        print("Nerozumím! Posral jsi to!")





