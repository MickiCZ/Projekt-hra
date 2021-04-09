utok = 0
obrana = 0
penize = 1000
inventory = []

#shop list - 0. name, 1. dmg 2. price
wooden_sword = ["Wooden sword", 5, 100]
rusty_sword = ["Rusty sword", 10, 250]
iron_sword = ["Iron sword", 15, 500]
katana = ["Katana", 20, 1000]
axe = ["Axe", 30, 2000]
shop_list = [wooden_sword, rusty_sword, iron_sword, katana, axe]
print("V našem obchodě máme následující: ")
for i in shop_list:
    print("Zbraň: {} dmg: +{} cena: {}".format(i[0], i[1], i[2]))

#Prodej
def buy_in_shop():
    global utok
    global penize
    select_item = int(input ("Co si z toho koupíš? (napiš číslo od 0 do 4) "))
    lengt_of_shop = len(shop_list)
    if select_item > lengt_of_shop:
        while select_item > lengt_of_shop:
            print("Toto není v nabídce!")
            select_item = int(input ("Co si z toho koupíš? (napiš číslo od 0 do 4) "))
    #kontrola zdali má peníze
    if penize < shop_list[select_item][2]:
        while select_item > lengt_of_shop or penize < shop_list[select_item][2]:
            print("Na tohle nemáš prachy!")
            select_item = int(input ("Co si z toho koupíš? (napiš číslo od 0 do 4) "))
    if select_item == 0:
        print(f"Koupil sis {shop_list[select_item][0]} ")
        utok = utok + shop_list[select_item][1]
        penize = penize - shop_list[select_item][2]
        inventory.append(shop_list[select_item])
        shop_list.pop(select_item)
        print(penize)
        print(utok)
        print(shop_list)
        print(inventory)
        buy_in_shop()
    elif select_item == 1:
        print(f"Koupil sis {shop_list[select_item][0]} ")
        utok = utok + shop_list[select_item][1]
        penize = penize - shop_list[select_item][2]
        inventory.append(shop_list[select_item])
        shop_list.pop(select_item)
        print(penize)
        print(utok)
        print(shop_list)
        print(inventory)
    elif select_item == 2:
        print(f"Koupil sis {shop_list[select_item][0]} ")
        utok = utok + shop_list[select_item][1]
        penize = penize - shop_list[select_item][2]
        inventory.append(shop_list[select_item])
        shop_list.pop(select_item)
        print(penize)
        print(utok)
        print(shop_list)
        print(inventory)
    elif select_item == 3:
        print(f"Koupil sis {shop_list[select_item][0]} ")
        utok = utok + shop_list[select_item][1]
        penize = penize - shop_list[select_item][2]
        inventory.append(shop_list[select_item])
        shop_list.pop(select_item)
        print(penize)
        print(utok)
        print(shop_list)
        print(inventory)
    elif select_item == 4:
        print(f"Koupil sis {shop_list[select_item][0]} ")
        utok = utok + shop_list[select_item][1]
        penize = penize - shop_list[select_item][2]
        inventory.append(shop_list[select_item])
        shop_list.pop(select_item)
        print(penize)
        print(utok)
        print(shop_list)
        print(inventory)

#try:
buy_in_shop()
print(utok)
print(penize)
#except IndexError:
    #print("Posral jsi to! Zadal jsi něco špatně.. zkus to znovu")
   
#while = True:
 #   print("Vešel jsi do obchodu")