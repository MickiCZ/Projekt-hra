import random
from random import randrange

# 0. jméno, 1. útok, 2. obrana, 3. životy, 4. xp, 5. loot
krysa = ["Krysa", 1, 0, 10, 50,[["krysí ocas", 0, 1, False, "item"], ["krysí zub", 0, 1, False, "item"], ["krysí bobek", 0, 1, False, "item"]]]
bandita = ["Bandita", 10, 3, 30, 60,[["bandití ocas", 0, 1, False, "item"], ["bandití zub", 0, 1, False, "item"], ["bandití bobek", 0, 1, False, "item"]]]
medved = ["Medvěd", 8, 2, 15, 40,[["medvědí ocas", 0, 1, False, "item"], ["medvědí zub", 0, 1, False, "item"], ["medvědí bobek", 0, 1, False, "item"]]]
#nepritel = [krysa, medved, bandita]
#inventory = []
#xp = 0


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

def level_up(xp,hp,atck,lvl,):
    print("Gratuluji získal jsi level.")
    atck += 1
    hp += 5
    a_hp = hp
    lvl += 1
    xp -= 100
    print(f"Aktuálně máš {lvl}. úroveň, útok: {atck}, {hp} životů a {xp} zkušeností.")
    return (atck, hp, lvl, xp, a_hp)

def fight(enemy_list, player_hp, player_atc, player_def, player_name, player_xp, player_inventory):
    get_enemy = random.choice(enemy_list)
    enemy_name = get_enemy[0]
    print(f"{player_name} bojuje proti {get_enemy[0]}")
    enemy_hp = get_enemy[3]
    enemy_atc = get_enemy[1]
    enemy_def = get_enemy[2]
    enemy_loot = get_enemy[5][randrange(0, len(get_enemy[5]))]
    enemy_xp = get_enemy[4]
    xp = player_xp
    
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
            break
    else:
        print("Prohrál jsi!")
    return(player_hp, xp, player_inventory)
#fight(nepritel, 50, 10, 0, "Walak", xp, inventory)