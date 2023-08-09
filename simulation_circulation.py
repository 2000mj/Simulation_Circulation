
import time

passa_one_three = True

def simuler_One_three_circulation():
    routes_actives = [1, 3]
    passages_pietons_actifs = [2, 4]

    if passa_one_three == True :
       for i in routes_actives:
           print(f"routes {i} est active et afficher Feu vert actif")
       print(f"routes 2 et 4 est desactive et afficher Feu rouge actif")
       for i in passages_pietons_actifs:
           print(f"passage {i} pour pietons est actif et afficher Feu vert actif")

def simuler_Two_Four_circulation():
        routes_actives = [2, 4]
        passages_pietons_actifs = [1, 3]

        if passa_one_three == False:
            for i in routes_actives:
                print(f"routes {i} est active et afficher Feu vert actif")
            print(f"routes 1 et 3 est desactive et afficher Feu rouge actif")

            for i in passages_pietons_actifs:
                print(f"passage {i} pour pietons est actif et afficher Feu vert actif")




def simuler_circulation():
    simuler_One_three_circulation()
    simuler_Two_Four_circulation()
    time.sleep(5)
    passa_one_three = False
    simuler_One_three_circulation()
    simuler_Two_Four_circulation()


while True :
    simuler_circulation()
