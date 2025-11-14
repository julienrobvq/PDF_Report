"""
Ce script permet de créer les fichiers de dialogues de façon automatisée à partir des QML des formulaires.
Le script parcours le contenu d'un dossier de manière récursive et extrait les informations de chaque formulaire.
Les fichiers de dialogues sont ensuite crées et enregistrés dans un autre dossier.

"""

import xml.etree.ElementTree as ET
import os
import re

#Parameters
dossier_qml = "qml"
dossier_sortie = os.path.join("dialogs")
os.makedirs(dossier_sortie, exist_ok=True)


def pythonize_name(name):
    return re.sub(r'\W+', '_', name).lower()


def classize_name(name):
    parts = re.split(r'\W+', name)
    return "".join(p.capitalize() for p in parts if p)


def format_list(lst, indent=12):
    s = "[\n"
    for item in lst:
        s += " " * indent + f"\"{item}\",\n"
    s += " " * (indent - 4) + "]"
    return s


# Extraction champs
def extraire_structure(qml_path):
    tree = ET.parse(qml_path)
    root = tree.getroot()

    # Trouver la racine du formulaire
    form_root = root.find(".//attributeEditorForm")
    if form_root is None:
        form_root = root

    champs_formulaire = []
    sections = {}

    # Parcours les qml
    def parcourir(element, section_actuelle=None):
        tag = element.tag
        name = element.attrib.get("name")

        # Conteneur (onglet, groupe…)
        if tag == "attributeEditorContainer":
            titre = name or "Sans titre"
            sections[titre] = []
            for child in element:
                parcourir(child, titre)
            return

        # Champ du formulaire
        if tag == "attributeEditorField":
            field_name = element.attrib.get("name")
            if field_name:
                champs_formulaire.append(field_name)
                if section_actuelle:
                    sections[section_actuelle].append(field_name)
            return

        # Continuer récursion
        for child in element:
            parcourir(child, section_actuelle)

    parcourir(form_root)

    # Dédupliquer champs
    champs_formulaire = list(dict.fromkeys(champs_formulaire))

    # Champs inclus dans un conteneur
    champs_in_sections = set(ch for lst in sections.values() for ch in lst)

    # Champs hors conteneurs dans section Général
    orphelins = [ch for ch in champs_formulaire if ch not in champs_in_sections]

    if orphelins:
        sections["Général"] = orphelins

    # Section général en premier dans les rapport
    if "Général" in sections:
        sections = {"Général": sections["Général"], **{k: v for k, v in sections.items() if k != "Général"}}

    return champs_formulaire, sections


# Génération des dialogues
for fichier in os.listdir(dossier_qml):
    if not fichier.lower().endswith(".qml"):
        continue

    chemin_qml = os.path.join(dossier_qml, fichier)

    champs, sections = extraire_structure(chemin_qml)

    layername = os.path.splitext(fichier)[0]
    py_name = pythonize_name(layername)
    class_name = "Rapport" + classize_name(layername) + "Dialog"

    fichier_sortie = os.path.join(
        dossier_sortie,
        f"rapport_{py_name}_dialog.py"
    )

    contenu = f"# dialogs/rapport_{py_name}_dialog.py\n\n"
    contenu += "from .base_rapport_dialog import BaseRapportDialog\n\n"
    contenu += f"class {class_name}(BaseRapportDialog):\n"
    contenu += f"    def __init__(self):\n\n"

    contenu += f"        champs = {format_list(champs, indent=12)}\n\n"

    contenu += "        sections = {\n"
    for section, champs_list in sections.items():
        contenu += f"            \"{section}\": {format_list(champs_list, indent=16)},\n"
    contenu += "        }\n\n"

    contenu += f"        super().__init__(\"{layername}\", champs, sections)\n"

    with open(fichier_sortie, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"Créé : {fichier_sortie}")

print("\nDialogs générés dans :", dossier_sortie)