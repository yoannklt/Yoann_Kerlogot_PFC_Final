#DEBUT

#On admet que la fonction random existe et renvoie un chiffre aléatoire entre 1 et 3
#On admet que la fonction input existe et demande à l'utilisateur de rentrer une chaine de caractères et la retourne

#Définir la fonction pierreFeuilleCiseaux n'ayant aucun argument
    #Créer nickname une variable et lui associer le retour d'execution de la fonction input("Quel est votre pseudo ?: ")
    #Créer playerPoints une variable et lui associer 0
    #Créer computerPoints une variable et lui associer 0
    #Créer score une variable et lui associer la concatenation de nickname + ": " + str(playerPoints) + "  " + "Ordinateur: " + str(computerPoints)

    #Créer play une variable et lui associer le retour d'execution de la fonction input("D'accord {nickname}, voulez-vous jouer ?: ")
        #Si play est égal à "yes"
            #Alors play est vraie (True)
        #Sinon si play est égal à "non"
            #Alors play est faux (False)

        #Créer computerChoice une variable et lui associer le retour d'execution de la fonction random
        #Si computerChoice est égal à 1
            #Alors computerChoice est égal à "Ciseaux"
        #Sinon si computerChoice est égal à 2
            #Alors computerChoice est égal à "Pierre"
        #Sinon computerChoice est égal à "Feuille"

        #Tant que play est vraie (True)
            #Créer playerChoice une variable et lui associer le retour d'execution de la fonction input("(P)ierre/(F)euille/(C)iseaux")
            #Si playerChoice est égal à "P" ou "p" 
                #Alors playerChoice est égal à "Pierre"
            #Sinon si playerChoice est égal à "F" ou "f" 
                #Alors playerChoice est égal à "Feuille"
            #Sinon playerChoice est égal à "Ciseaux"

            #Si playerChoice est égal à computerChoice 
                #Alors afficher playerChoice + "VS .." + computerChoice
                #Afficher "Egalité"
                #Afficher score
            #Sinon si playerChoice est égal à "Pierre" ET computerChoice est égal à "Ciseaux"
                #Alors afficher la concatenation de  playerChoice + "VS .." + computerChoice
                #Afficher la concatenation de  nickname + "gagne"
                #Incrémenter playerPoints de 1
                #Afficher score
            #Sinon si playerChoice est égal à "Feuille" ET computerChoice est égal à "Pierre"
                #Alors afficher playerChoice + "VS .." + computerChoice
                #Afficher la concatenation de  nickname + "gagne"
                #Incrémenter playerPoints de 1
                #Afficher score
            #Sinon si playerChoice est égal à "Ciseaux" ET computerChoice est égal à "Feuille"
                #Alors afficher  la concatenation de playerChoice + "VS .." + computerChoice
                #Afficher la concatenation de  nickname + "gagne"
                #Incrémenter playerPoints de 1
                #Afficher score

            #Si playerChoice est égal à "Pierre" ET computerChoice est égal à "Feuille"
                #Alors afficher la concatenation de  playerChoice + "VS .." + computerChoice
                #Afficher "L'ordinateur gagne"
                #Incrémenter computerPoints de 1
                #Afficher score
            #Sinon si playerChoice est égal à "Feuille" ET computerChoice est égal à "Ciseaux"
                #Alors afficher la concatenation de  playerChoice + "VS .." + computerChoice
                #Afficher "L'ordinateur gagne"
                #Incrémenter computerPoints de 1
                #Afficher score
            #Sinon si playerChoice est égal à "Ciseaux" ET computerChoice est égal à "Pierre"
                #Alors afficher la concatenation de  playerChoice + "VS .." + computerChoice
                #Afficher "L'ordinateur gagne"
                #Incrémenter computerPoints de 1
                #Afficher score
                
            #Si playerPoints est égal à 3
                #Alors afficher la concatenation de "Vous avez gagné" + nickname
                #Afficher score
                #Créer replay une variable et lui associer le retour d'exécution de la fonction input("Rejouer, (o)ui/(n)on : ")
                    #Si replay est égal à "O" ou "o"
                        #Alors continuer la boucle
                    #Sinon casser la boucle
            #Sinon computerPoints est égal à 3
                #Alors afficher "L'ordinateur est gagnant !"
                #Afficher score
                #Créer replay une variable et lui associer le retour d'exécution de la fonction input("Rejouer, (o)ui/(n)on : ")
                    #Si replay est égal à "O" ou "o"
                        #Alors continuer la boucle
                    #Sinon casser la boucle
                    
        #Afficher "D'accord à la prochaine !"        
            
            
#Exécuter pierreFeuilleCiseaux() 

#FIN