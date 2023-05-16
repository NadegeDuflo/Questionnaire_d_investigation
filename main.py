def poser_questions(questionChoix):
    choix = questionChoix[1]
    print(" ", questionChoix[0])
    for i in range(len(choix)):
        print(" ", i+1, " - ", choix[i])
    reponse = choix[int(input("Votre choix : "))-1]
    return reponse


def temoins(temoin):
    temoin_question = (f"Le témoin {temoin} est : ",("Conforme","Non-conforme","Absent"))
    try:
        return f"Le témoin {temoin} est "+ poser_questions(temoin_question)
    except:
        return ""

zone = input("Quelle est la zone ? ")
piece = input("Quelle est la pièce ? ")
classe = input("Quelle est la classe ? ")
TypesControle = ("Quel type de contrôle ?",("de Surface","d’Air Dynamique","d’Air Statique","de Tenue","de Gant","de Comptage particulaire"))
TypeControle = poser_questions(TypesControle)
stades = ("Sélection du stade : ",("cours de remplissage", "cours de sertissage","fin de poste","déchargement","après intervention","inter-lot","hors activité","habilitation"))
stade = poser_questions(stades)

if TypeControle == "d’Air Dynamique":
    unite = "UFC/m3"
elif TypeControle == "d'Air Statique" or TypeControle == "de Gant":
    unite = "UFC"
elif TypeControle == "de Surface" or TypeControle == "de Tenue":
    unite = "UFC/25cm2"
elif TypeControle == "de Comptage particulaire" and classe == "A":
    unite = "part./m3"
elif TypeControle == "de Comptage particulaire" and stade == "hors activité" and classe == "B":
    unite = "part./690L"
elif TypeControle == "de Comptage particulaire" and classe == "B" or classe == "C":
    unite = "part./p3"

    


point = input("du(des) point(s) (code et intitulé) : ")



frequences = ("Sélection de la fréquence : ",("par lot","journalier","hebdomadaire","mensuel","trimestriel","annuel"))
frequence = poser_questions(frequences)

produit = input("Pour un produit préciser Nom/code/lot : ").split("/")
try:
    nomProduit,code,lot = produit[0],produit[1],produit[2]
    donnees_produit = f"du Lot : {lot} Produit : {nomProduit} Code : {code}"
except:
    donnees_produit = ""

statuts = ("Sélection du statut : ",("absent(s)","non conforme(s)"))
statut = poser_questions(statuts)

resultat = input("Quel est le résultat avec l'unité ? : ")
statuts_resultat =("Quel est le type de non conformité ? ",("OOT","OOS"))
statut_resultat = poser_questions(statuts_resultat)
alerte = input("Quelle est la limite d'alerte ? : ")
action = input("Quelle est la limite d'action ? : ")
temoinpos = temoins("Témoin positif")
temoinneg = temoins("Témoin négatif")
temoincoul = temoins("Témoin coulage de swab")
temoincomp = temoins("Témoin comptage")

if input("germes à identifier ? O/N : "):
    germes = "Identification des germes détectés à réaliser"
else : 
    germes = ""

visa_preleveur = input("Prélèvement(s) réalisé(s) par (VISA) : ")
service_preleveur = input("Service du préleveur : ")
visa_reception_incubation = input("Incubation, réception réalisé par (VISA) : ")
visa_lecteur = input("Lecture réalisé par : ")

date_prelevement = input("Prélèvement réalisé le : ")
try:
    horaire = "à " + input("Quelle heure? ")
except:
    horaire = ""
try:
    date_incubation = "Incubation réalisée le : " + input("Date de mise en incubation : ")
    date_lecture = "Lecture réalisée le : " + input("Date de la lecture : ")
except:
    date_incubation = ""
    date_lecture = ""

description = f"""
QUOI ?
Contrôle d’environnement {TypeControle} du(des) point(s) : {point}.
Prélèvement(s) réalisé(s) en {stade}.
Il s’agit d’un contrôle {frequence}.
Résultat(s) {statut}.

{point}
Résultat : {resultat} {unite} en {statut_resultat}
Limite d’alerte  > {alerte} {unite}
Limite d’action / NMA  = {action} {unite}

{temoinpos}      
{temoinneg}
{temoincoul}
{temoincomp}

{germes}        

QUI ?
Prélèvement réalisé par : {visa_preleveur} (Service : {service_preleveur})
Réception et incubation réalisées par : {visa_reception_incubation}
Lecture réalisée par : {visa_lecteur}

OU ? 
Prélèvement réalisé en Zone : {zone} / Pièce : {piece} / Classe : {classe}
Incubation / Lecture réalisées dans la pièce 1F19 du laboratoire de bactériologie.

QUAND ?
Prélèvement réalisé le : {date_prelevement} {horaire}
{date_incubation}  
{date_lecture}

COMMENT ? 
Prélèvement réalisé selon la BOP 527-04-007 « Contrôle microbiologique des surfaces et tenues » / 527-04-003 « Contrôles d’environnement au niveau de la zone de prélèvements de l’inspection (Pont de prélèvements) / 527-04-025 « Contrôles d’environnement mensuels dans le laboratoire de bactériologie » / 527-04-055 « Contrôles microbiologiques et particulaires journaliers et hebdomadaires des zones de classes A, B, C et D » / 527-04-056 « Expression des résultats des contrôles mensuels et trimestriels dans les zones à atmosphère contrôlée » / 527-04-057 « Contrôles périodiques semestriels et annuels dans les zones à atmosphère contrôlée (SVP1-SVP2) » Version : (à compléter), Annexe n° : (à compléter).
(Compléter avec les éléments détectés lors du prélèvement, du transport, de l’incubation ou de la lecture des contrôles. 
Par exemples : 
Ex1 : Aucun incident n’a été relevé lors de la réalisation des prélèvements en zone
Ex2 : Boites observées rétractées ou mal fermées lors de la lecture
Ex3 : Swab observé non cassé ou fuyant lors de la mise en incubation)
(Si un évènement laboratoire peut expliquer la cause de l’écart, ouvrir une LAB dans trackwise)

COMBIEN ?
(Nombre à compléter) prélèvement(s) concerné(s)
POURQUOI ?
Ecart par rapport à la BOP."""

print(description)
