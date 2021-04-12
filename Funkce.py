import random
from random import randrange

# 0. jméno, 1. útok, 2. obrana, 3. životy, 4. xp, 5. loot
krysa = ["Krysa", 1, 0, 10, 50,[["krysí ocas", 0, 1, False, "item"], ["krysí zub", 0, 1, False, "item"], ["krysí bobek", 0, 1, False, "item"]]]
bandita = ["Bandita", 10, 3, 30, 60,[["bandití ocas", 0, 1, False, "item"], ["bandití zub", 0, 1, False, "item"], ["bandití bobek", 0, 1, False, "item"]]]
medved = ["Medvěd", 8, 2, 15, 40,[["medvědí ocas", 0, 1, False, "item"], ["medvědí zub", 0, 1, False, "item"], ["medvědí bobek", 0, 1, False, "item"]]]
#nepritel = [krysa, medved, bandita]
#inventory = []
#xp = 0


#Formula pro udělení poškození v souboji
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


#Level up systém
def level_up(xp,hp,atck,lvl,):
    print("Gratuluji získal jsi level.")
    atck += 1
    hp += 5
    a_hp = hp
    lvl += 1
    xp -= 100
    print(f"Aktuálně máš {lvl}. úroveň, útok: {atck}, {hp} životů a {xp} zkušeností.")
    return (atck, hp, lvl, xp, a_hp)


#Funkce souboje v aréně
def fight(enemy_list, player_hp, player_atc, player_def, player_name, player_xp, player_inventory, money,):
    get_enemy = random.choice(enemy_list)
    enemy_name = get_enemy[0]
    print(f"{player_name} bojuje proti {get_enemy[0]}")
    enemy_hp = get_enemy[3]
    enemy_atc = get_enemy[1]
    enemy_def = get_enemy[2]
    enemy_loot = get_enemy[5][randrange(0, len(get_enemy[5]))]
    enemy_xp = get_enemy[4]
    xp = player_xp
    loot_money = money
    
    while player_hp > 0:
        if enemy_hp > 0:
            zraneni_enemy, zraneni_player = boj(player_atc, player_def, enemy_atc, enemy_def)
            print(f"Zranění způsobené nepřítely je {zraneni_enemy}")
            print(f"Zranění způsobené hráči je {zraneni_player}")
            player_hp -= zraneni_player
            enemy_hp -= zraneni_enemy
            print(f"Máš {player_hp} životů") 
            print(f"{enemy_name} má {enemy_hp} životů")
        else:
            print("Vyhrál jsi!")
            xp = player_xp + enemy_xp
            player_inventory.append(enemy_loot)
            print(f"Získal jsi {enemy_loot[0]}")
            loot_money = money + 20
            break
    else:
        print("Prohrál jsi!")
    return(player_hp, xp, player_inventory, loot_money)
#fight(nepritel, 50, 10, 0, "Walak", xp, inventory)


#Fungování hostince
def tavern(money, def_hp, act_hp):
    hp = act_hp
    print("Vešel jsi do krásného hostince.")
    choice = input("Co chceš dělat? (sleep/exit) ")
    if choice == "sleep":
        print("Spaní zde stojí 50 peněz.")
        choice_sleep = input("Opravdu chceš přespat? (y/n) ")
        if choice_sleep == "y":
            if money < 50:
                print("Na to nemáš peníze. Přijď až je budeš mít")
                return(money, hp)
            money -= 50
            hp = def_hp
            print(f"Hezky jsi se vyspal. Tvé aktuální životy jsou {hp}/{def_hp}")
        elif choice_sleep == "n":
            print(f"Opouštíš hostinec. Tvé aktuální životy jsou {hp}/{def_hp}")
    elif choice == "exit":
        print(f"Opouštíš hostinec. Tvé aktuální životy jsou {hp}/{def_hp}")
    return(money, hp)


#Fungování inventáře
def inventory(inv, eqp, dmg):
    inventory_slot = 0
    item_summarize = ""
    equip_summarize = ""
    add_dmg = dmg
    for i in inv:
        if i[4] == "weapon":
            item_summarize = item_summarize + i[0] + " " + "+" + str(i[1]) +"Dmg, "
        else:
            item_summarize = item_summarize + i[0] + ", "
    for i in eqp:
        if i[4] == "weapon":
            equip_summarize = equip_summarize + i[0] + " " + "+" + str(i[1]) +"Dmg, "
        else:
            equip_summarize = equip_summarize + i[0] + ", "
    print(f"V inventáří máš: {item_summarize}a equipnuto máš: {equip_summarize}")
    for i in inv:
        if i[3] == True:
            print(i[0])
            want_equip = input("Chceš si to vybavit? (y/n) ")
            if want_equip == "y":
                eqp.append(i)
                inv.pop(inventory_slot)
                add_dmg = dmg + i[1]
        inventory_slot += 1
    for i in inv:
        if i[4] == "weapon":
            item_summarize = item_summarize + i[0] + " " + "+" + str(i[1]) +"Dmg, "
        else:
            item_summarize = item_summarize + i[0] + ", "
    for i in eqp:
        if i[4] == "weapon":
            equip_summarize = equip_summarize + i[0] + " " + "+" + str(i[1]) +"Dmg, "
        else:
            equip_summarize = equip_summarize + i[0] + ", "
    print(f"V inventáří máš: {item_summarize}a equipnuto máš: {equip_summarize}")
    return(add_dmg)