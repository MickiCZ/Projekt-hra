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
krysa = ["Krysa", 1, 0, 10, 10,["krysí ocas", "krysí zub", "krysí bobek"]] # 0. jméno, 1. útok, 2. obrana, 3. životy, 4. xp, 5. loot
bandita = ["Bandita", 10, 3, 30]
medved = ["Medvěd", 8, 2, 15]
nepritel = [krysa]





while zivoty > 0:
    #if keyboard.read_key() == "i":
        #Inventář.inventory()
    if xp >= 100: #Zisk nového lvl
        print("Gratuluji získal jsi level.")
        utok += 1
        zivoty += 5
        lvl += 1
        xp -= 100
        print(f"Aktuálně máš {lvl}. úroveň, útok: {utok}, {zivoty} životů a {xp} zkušeností.")

    print(f"""Tvůj hrdina se jmenuje {jmeno_hrdiny}, je na {lvl}. úrovni. má {zivoty} životů a {penize} penez a {xp} zkušeností.
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
                inventory_list.append(get_nepritel[5][randrange(0, len(get_nepritel[5]))])
                print(inventory_list)
                break
        else:
            print("Prohrál jsi!")
    # Tady začíná souboj
    else:
        print("Nerozumím! Posral jsi to!")





