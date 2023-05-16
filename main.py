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

nb_prelevements = int(input("Combien de prélèvements concernés : "))
zone = input("Quelle est la zone ? ")
piece = input("Quelle est la pièce ? ")
classe = input("Quelle est la classe ? ")
produit = input("Pour un produit préciser Nom/code/lot : ").split("/")
try:
    nomProduit,code,lot = produit[0],produit[1],produit[2]
    donnees_produit = f"du Lot : {lot} Produit : {nomProduit} Code : {code}"
except:
    donnees_produit = ""

stades = ("Sélection du stade : ",("cours de remplissage", "cours de sertissage","fin de poste","déchargement","après intervention","inter-lot","hors activité","habilitation"))
stade = poser_questions(stades)

description = f"""
QUOI ?
Contrôle d'environnement {donnees_produit}.
Prélèvement(s) réalisé(s) en {stade} .
"""   

def donnees_prelevements():
    TypesControle = ("Quel type de contrôle ?",("de Surface","d’Air Dynamique","d’Air Statique","de Tenue","de Gant","de Comptage particulaire"))
    TypeControle = poser_questions(TypesControle)
    
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

    statuts = ("Sélection du statut : ",("absent(s)","non conforme(s)"))
    statut = poser_questions(statuts)

    resultat = input("Quel est le résultat avec l'unité ? : ")
    statuts_resultat =("Quel est le type de non conformité ? ",("OOT","OOS"))
    statut_resultat = poser_questions(statuts_resultat)
    try:
        alerte = input("Quelle est la limite d'alerte ? : ")
    except:
        alerte = "Aucune"
    action = input("Quelle est la limite d'action ? : ")
    
    description_prelevement = f"""
    Contrôle {TypeControle} du(des) point(s) : {point}.
    Il s’agit d’un contrôle {frequence}.
    Résultat(s) {statut}.
       
    Résultat : {resultat} {unite} en {statut_resultat}
    Limite d’alerte  > {alerte} {unite}
    Limite d’action / NMA  = {action} {unite}
    """
    
    return description_prelevement

for i in range(nb_prelevements):
    description += donnees_prelevements()

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



description += f"""

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


COMBIEN ?
{nb_prelevements} prélèvement(s) concerné(s)

POURQUOI ?
Ecart par rapport à la BOP."""

print(description)
