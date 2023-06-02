# import pyperclip

def poser_questions(questionChoix):
    choix = questionChoix[1]
    print(" ", questionChoix[0])
    for i in range(len(choix)):
        print(" ", i+1, " - ", choix[i])
    try:
        return choix[int(input("Votre choix : "))-1]
    except:
        return poser_questions(questionChoix)

def poser_questions_facultative(question,reponse_positive,reponse_negative):
    reponse = input(question)
    return reponse_positive[0] + reponse + reponse_positive[1]+ "\n" if reponse else reponse_negative + "\n"

def poser_questions_repetitives(question):
    description_comment = ""
    reponses = ""
    while True:
        try:
            for i in range(len(question)):
                reponse = poser_questions_facultative(question[i][0],question[i][1],"")
                if not reponse and i == 0:
                    return description_comment
                else:
                    reponses += reponse
            description_comment += reponses + "\n"
            reponses = ""
        except:
            reponse = poser_questions_facultative(question,("",""),"")
            if not reponse :
                return description_comment
            description_comment += reponse + "\n"  

def temoins(temoin):

    temoin_question = f"Le témoin {temoin} est : ",("Conforme","Non-conforme","Absent","Non Applicable")
    reponse = poser_questions(temoin_question)
    if reponse != "Non Applicable":    
        return f"Le témoin {temoin} est {reponse}\n"
    else:
        return ""

def donnees_prelevements():
    TypesControle = ("QUOI : Quel type de contrôle ?",("de Surface","d’Air Dynamique","d’Air Statique","de Tenue","de Gant","de Comptage particulaire"))
    TypeControle = poser_questions(TypesControle)
    
    if TypeControle == "d’Air Dynamique":
        unite = " UFC/m3"
    elif TypeControle == "d'Air Statique" or TypeControle == "de Gant":
        unite = " UFC"
    elif TypeControle == "de Surface" or TypeControle == "de Tenue":
        unite = " UFC/25cm2"
    elif TypeControle == "de Comptage particulaire" and classe == "A":
        unite = " part./m3"
    elif TypeControle == "de Comptage particulaire" and stade == "hors activité" and classe == "B":
        unite = " part./690L"
    elif TypeControle == "de Comptage particulaire" and classe == "B" or classe == "C":
        unite = " part./p3"

    point = input("du(des) point(s) (code et intitulé) : ")

    frequences = ("QUOI : Sélection de la fréquence : ",("par lot","journalier","hebdomadaire","mensuel","trimestriel","annuel"))
    frequence = poser_questions(frequences)

    statuts = ("QUOI : Sélection du statut : ",("absent(s)","non conforme(s)"))
    statut = poser_questions(statuts)

    resultat = input("QUOI : Quel est le résultat ? : ") + unite

    statuts_resultat =("QUOI : Quel est le type de non conformité ? ",("OOT","OOS"))
    statut_resultat = poser_questions(statuts_resultat)

    alerte = poser_questions_facultative("QUOI : Quelle est la limite d'alerte ? : ",("",f" {unite}"),"Aucune")

    action = input("QUOI : Quelle est la limite d'action ? : ") + unite
    
    description_prelevement = f"""
Contrôle d'environnement {TypeControle} du(des) point(s) : {point}.
Prélèvement(s) réalisé(s) en {stade} {donnees_produit}.
Il s’agit d’un contrôle {frequence}.
Résultat(s) {statut}.
    
Résultat : {resultat} en {statut_resultat}
Limite d’alerte : {alerte}
Limite d’action / NMA  = {action}
"""
    
    return description_prelevement

nb_prelevements = int(input("Combien de prélèvements concernés : "))

zone = input("OU : Quelle est la zone ? ")
piece = input("OU : Quelle est la pièce ? ")
classe = input("OU : Quelle est la classe ? ")
produit = input("QUOI : Pour un produit préciser Nom/code/lot : ").split("/")
try:
    nomProduit,code,lot = produit[0],produit[1],produit[2]
    donnees_produit = f"du Lot : {lot} Produit : {nomProduit} Code : {code}"
except:
    donnees_produit = ""

stades = ("Sélection du stade : ",("cours de remplissage", "cours de sertissage","fin de poste","déchargement","après intervention","inter-lot","hors activité","habilitation"))
stade = poser_questions(stades)

description = f"""
QUOI ?
"""   

for i in range(nb_prelevements):
    description += donnees_prelevements()

temoinpos = temoins("Témoin positif")
temoinneg = temoins("Témoin négatif")
temoincoul = temoins("Témoin coulage de swab")
temoincomp = temoins("Témoin comptage")

germes = "Identification des germes détectés à réaliser. \n" if input("germes à identifier ? (O) : ") else ""

visa_preleveur = input("QUI : Prélèvement(s) réalisé(s) par (VISA) : ")
service_preleveur = input("QUI : Service du préleveur : ")

visa_reception_incubation = poser_questions_facultative("QUI : Incubation, réception réalisé par (VISA) : ",("Réception et incubation réalisées par : ","\n"),"")
visa_lecteur = poser_questions_facultative("QUI : Lecture réalisé par (VISA): ",("Lecture réalisée par: ","\n"),"")


date_prelevement = input("QUAND : Prélèvement réalisé le : ")
horaire = poser_questions_facultative("QUAND : Quelle heure? ",(" à ","\n"),"horaire non précisé \n")

date_incubation = poser_questions_facultative("QUAND : Date de mise en incubation : ",("Incubation réalisée le : ",""),"")
date_lecture = poser_questions_facultative("QUAND : Date de la lecture : ",("Lecture réalisée le : ",""),"")

incidents = poser_questions_repetitives("Incidents à déclarer : ")
milieux = poser_questions_repetitives((("Nom du milieux : ",("Milieux : ","")),("Lot du milieux : ",(", Lot : ","")),("Expiration :",(", Exp :",""))))
equipements =poser_questions_repetitives((("Nom de l'équipement : ",("Equipement : ","")),("Date de calibration : ",(", Calibré le : ",""))))


description += f"""
{temoinpos}{temoinneg}{temoincoul}{temoincomp}
{germes}
QUI ?
Prélèvement réalisé par : {visa_preleveur} (Service : {service_preleveur})
{visa_reception_incubation}Lecture réalisée par : {visa_lecteur}

OU ? 
Prélèvement réalisé en Zone : {zone} / Pièce : {piece} / Classe : {classe}
Incubation / Lecture réalisées dans la pièce 1F19 du laboratoire de bactériologie.

QUAND ?
Prélèvement réalisé le : {date_prelevement} {horaire}{date_incubation}{date_lecture}

COMMENT ? 


{incidents}
{milieux}
{equipements}

COMBIEN ?
{nb_prelevements} prélèvement(s) concerné(s)

POURQUOI ?
Ecart par rapport à la BOP."""

# print(description)

# pyperclip.copy(description)

# print(pyperclip.paste())
