"""
Ce script est exécutable dans QGIS et permet d'enregistrer les QML des couches dans un dossier.
Dans ce cas-ci, les couches ayant un nom débutant par Form_ sont sélectionnées.
Les conditions d'exportation peuvent être adaptées selon les besoins.

"""

import os
from qgis.core import QgsProject

# chemin
dossier_sortie = r"C:\Users\ROBVQ\Desktop\test_rapport\qml"

# Crée le dossier s'il n'existe pas
os.makedirs(dossier_sortie, exist_ok=True)

# Récupération du projet
proj = QgsProject.instance()

# Parcours des couches du projet
for layer in proj.mapLayers().values():

    nom = layer.name()

    # Filtre : seulement les couches qui commencent par Form_
    if not nom.startswith("Form_"):
        continue

    # Construction du chemin du fichier de sortie
    chemin_qml = os.path.join(dossier_sortie, f"{nom}.qml")

    # Sauvegarde du style complet (symbologie + formulaires + champs)
    ok = layer.saveNamedStyle(chemin_qml)

    if ok:
        print(f"Style exporté : {chemin_qml}")
    else:
        print(f"ERREUR pour : {nom}")