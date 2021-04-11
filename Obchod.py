#shop list - 0. name, 1. dmg 2. price 3. equipable 4. type
wooden_sword = ["Wooden sword", 5, 100, True, "weapon"]
rusty_sword = ["Rusty sword", 10, 250, True, "weapon"]
iron_sword = ["Iron sword", 15, 500, True, "weapon"]
katana = ["Katana", 20, 1000, True, "weapon"]
axe = ["Axe", 30, 2000, True, "weapon"]
fake_Exit = []
shop_list = [fake_Exit, wooden_sword, rusty_sword, iron_sword, katana, axe]


#Prodej
def buy_in_shop(money, inventory):
    choice_of_doing = input("Co chceš dělat? (buy/sell/exit)" )
    if choice_of_doing == "buy":
        print(f"Máš tolik {money} a v našem obchodě máme následující: ")
        for i in shop_list:
            if i != fake_Exit:
                print("Zbraň: {} dmg: +{} cena: {}".format(i[0], i[1], i[2]))
            
        select_item = int(input ("Co si z toho koupíš? (napiš číslo od 1 do 5 nebo 0 pro odchod) "))
        lengt_of_shop = len(shop_list)
        if select_item > lengt_of_shop:
            while select_item > lengt_of_shop:
                print("Toto není v nabídce!")
                select_item = int(input ("Co si z toho koupíš? (napiš číslo od 1 do 5) "))
        if select_item == 0:
            print("Opustil jsi obchod")
            return(money)
        
        #kontrola zdali má peníze
        if money < shop_list[select_item][2]:
            while select_item > lengt_of_shop or money < shop_list[select_item][2]:
                print("Na tohle nemáš prachy!")
                select_item = int(input ("Co si z toho koupíš? (napiš číslo od 1 do 5) "))
        if select_item == 1:
            print(f"Koupil sis {shop_list[select_item][0]} ")
            money = money - shop_list[select_item][2]
            inventory.append(shop_list[select_item])
            shop_list.pop(select_item)
            print(money)
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
        elif select_item == 5:
            print(f"Koupil sis {shop_list[select_item][0]} ")
            utok = utok + shop_list[select_item][1]
            penize = penize - shop_list[select_item][2]
            inventory.append(shop_list[select_item])
            shop_list.pop(select_item)
            print(penize)
            print(utok)
            print(shop_list)
            print(inventory)
        return (money)
    elif choice_of_doing == "sell":
        print("Sorry!! WIP!!")
    
        
#penize = buy_in_shop(1000)
#print("Na konci obchodování máš tolik peněz: ", penize)
#try:
#except IndexError:
    #print("Posral jsi to! Zadal jsi něco špatně.. zkus to znovu")
   
#while = True:
 #   print("Vešel jsi do obchodu")