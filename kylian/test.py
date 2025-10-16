#import sys
import random
def jeu() :
 
   
    def defaite(fin_de_jeu) :
        #quit (jeu())
        print("Defaite")
        print(f"Vôtre score est de {pieces} pièces.") #ajoute "score" (nb de pieces)
        print("écris 'jeu()' pour rejouer !")
        fin_de_jeu = True
        return fin_de_jeu
   
   
    lieux = ["sous le lit", "sur le lit", "sous l'oreiller", "sous la couverture", "sur l'armoire", "dans l'armoire", "sous l'armoire", "sur le placard", "dans le placard", "sous le placard", "dans le tiroir du haut", "dans le tiroir du milieu", "dans le tiroir du bas", "sur la table de chevet", "dans le tiroir de la table de chevet", "sous la table de chevet", "sur l'étagère du haut de la bibliothèque", "sur l'étagère du milieu de la bibliothèque", "sur l'étagère du bas de la bibliothèque"]
    indices = ["belle tentative ratée ! peut-être te rattraperas-tu dans l'armoire ?", "bien essayé... peut-être sous le lit tu trouveras qui sais...", "t'es vraiment pas facile toi ! essaye sur l'étagère du haut de la bibliothèque.", "raté ! essaye sur la table de chevet.", "non ! mais essaye sous le placard.", "pas du tout ! essaye dans le tiroir du bas."]
    items = ["chapeau", "glaive", "flambeau", "sac de 3 pièces d'or", "sac de 3 pièces d'or", "sac de 3 pièces d'or", "sac de 3 pièces d'or", "sac de 6 pièces d'or",  "sac de 6 pièces d'or", "sac de 9 pièces d'or", "vide", "vide", "vide", "vide", "vide", "sbire du monstre", "sbire du monstre", "marchand"]

   
 
    pieces = 0
    ch = 0

    g = 0
   
    fl = 0
   
    fin_de_jeu = False

    def placer_monstre() :
        placement = int(random.randint(0, len(lieux) - 1 ))
        return placement

    def trouver_item(pieces, ch, g, fl) :
            t = random.randint(0, len(items) - 1)
            item_trouvé = items[t]
           
            if item_trouvé == "vide" :
                print("il n'y a rien ici !")
           
            elif item_trouvé == "chapeau" :
                ch += 1
                print("vous avez un chapeau ! en revanche, pas sûr qu'il vous serve contre le monstre.")
               
            elif item_trouvé == "glaive" :
                g += 1
                print("vous avez trouvé un glaive ! il pourrait vous être utile si vous tombez sur un sbire.")

            elif item_trouvé == "flambeau" :
                fl += 1
                print("vous avez trouvé un flambeau ! il pourrait vous être utile face au monstre, il craint le feu.")

            elif item_trouvé == "sac de 3 pièces d'or" :
                pieces += 3
                print(f"oh, un sac de 3 pièces d'or ! vous avez maintenant {pieces} pièces d'or.")

            elif item_trouvé == "sac de 6 pièces d'or" :
                pieces += 6
                print(f"oh, un sac de 6 pièces d'or ! vous avez maintenant {pieces} pièces d'or.")    

            elif item_trouvé == "sac de 9 pièces d'or" :
                pieces += 9
                print(f"oh, un sac de 9 pièces d'or ! vous avez maintenant {pieces} pièces d'or.")

            elif item_trouvé == "sbire du monstre" :
                if g > 0 : #test1
                    glavi = str(input("un sbire se cachait là ! vous avez un glaive pour l'abbatre, l'utilisez-vous ? "))
                    if glavi == "oui" :
                        g = g - 1
                        print("ennemi abbatu !")
                    elif glavi == "non" :
                        print("dommage, le sbire vous mange.")
                        defaite(fin_de_jeu)
                elif g == 0 :
                    print("le sbire vous mange !")
                    defaite(fin_de_jeu)

            elif item_trouvé == "marchand" :
                achat=str(input(f"voilà le marchand se cachait là, vous avez {pieces} pièces d'or. vous pouvez acheter : un glaive (12 pièces d'or), un flambeau (15 pièces d'or) ou un chapeau (27 pièces d'or); que m'achètes-tu ?"))
                if achat == "rien" :
                    print("le marchand vous souhaite une bonne journée.")
                elif achat == "un glaive" or "glaive" :
                    if pieces < 12 :
                        print(f"vous ne pouvez pas vous le permettre ! vous n'avez que {pieces} pièces d'or.")
                    else :
                        g= g + 1
                        pieces = pieces - 12
                        print("ce glaive pourrait vous être utile si vous tombez sur un sbire ! il vous reste {pieces} pièces d'or. le marchand vous remercie.")
                elif achat == "un flambeau" or "flambeau" :
                    if pieces < 15 :
                        print(f"vous ne pouvez pas vous le permettre ! vous n'avez que {pieces} pièces d'or.")
                    else :
                        fl = fl + 1
                        pieces = pieces - 15
                        print("ce flambeau pourrait vous être utile si vous tombez sur le monstre, il craint le feu. il vous reste {pieces} pièces d'or. le marchand vous remercie.")
                elif achat == "un chapeau" or "chapeau" :
                    if pieces < 27 :
                        print(f"vous ne pouvez pas vous le permettre ! vous n'avez que {pieces} pièces d'or.")
                    else :
                        ch = ch + 1
                        print("vous avez un chapeau ! en revanche, pas sûr qu'il vous serve contre le monstre.")
                   
            items.pop(t)
            return pieces, ch , g , fl


    monstre = placer_monstre()

    print("Tu te trouves dans une mysterieuse chambre, un monstre s'y cache. Ne le trouve pas ou il te mangera.")

    lieu_fouillé = str(input("où fouilles-tu ? "))
    lieux_bannis = []
    n=60
    m=0
    nouveaux_indices = []
    def valeurs_n_m() :
        return 60, 60
    while lieu_fouillé != lieux[monstre] and not fin_de_jeu :
        
        if lieu_fouillé not in lieux :

            if n > 0 and not len(indices) == 0:
                p=random.randint(0, len(indices) - 1)
                print(indices[p])
                nouveaux_indices.append(indices[p])
                indices.pop(p)
                n = n - 10
            elif n == 0 and len(nouveaux_indices) != 0:
                b = random.randint(0, len(nouveaux_indices) - 1)
                print(nouveaux_indices[b])
                indices.append(nouveaux_indices[b])
                nouveaux_indices.pop(b)
                m = m - 10
                if len(nouveaux_indices) == 0 :
                    n, m = valeurs_n_m()
            lieu_fouillé = str(input("où fouilles-tu ? "))


            #else :
            #    print("oula")
               
        else :
            if lieu_fouillé in lieux_bannis :
                print("lieu vide !")
            elif lieu_fouillé not in lieux_bannis :
                pieces , ch, g, fl = trouver_item(pieces, ch, g, fl) #cherche un item dans sa liste items et le print
                lieux_bannis.append(lieu_fouillé)
                #lieux.remove(lieu_fouillé)
            lieu_fouillé=str(input("où fouilles-tu ? "))
            #print(f"indices {indices}\n")
            #print(f"nouveau {nouveaux_indices}\n")
       
    if fl > 0 :
        print("voilà le monstre ! grâce à votre flambeau il s'enfui de la chambre, vous gagnez la parti, bravo !")
        defaite(fin_de_jeu)
   
    elif ch > 0 :
        print("voilà le monstre, vous vous faîtes manger. joli chapeau !")
        defaite(fin_de_jeu)

    else :
        print("voilà le monstre ! vous vous faîtes manger.")
        defaite (fin_de_jeu)
jeu()