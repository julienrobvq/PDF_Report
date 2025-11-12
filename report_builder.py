import xml.etree.ElementTree as ET

# --- Paramètres ---
qml_path = "ActDetection.qml"  # chemin vers ton fichier QML

# --- Lecture du fichier ---
tree = ET.parse(qml_path)
root = tree.getroot()

champs_affiches = []
sections = {}

def parcourir_element(element, section_actuelle=None):
    """
    Parcourt récursivement la structure du formulaire QGIS.
    - Si l'élément est un conteneur (onglet/groupe), crée une section temporaire.
    - Si aucun champ n'y est trouvé, la section est ignorée.
    """
    tag = element.tag
    name = element.attrib.get("name")

    # Si c'est un conteneur (onglet ou groupe)
    if tag in ("attributeEditorContainer", "attributeEditorForm", "attributeEditorRelation"):
        titre = name or "Sans titre"
        champs_section = []

        # Parcourt récursivement les éléments enfants
        for child in element:
            champs_section += parcourir_element(child, section_actuelle=titre)

        # Si le conteneur contient au moins un champ, on l’ajoute
        if champs_section:
            sections[titre] = champs_section
        return champs_section

    # Si c'est un champ
    elif tag == "attributeEditorField":
        field_name = element.attrib.get("name")
        if field_name:
            champs_affiches.append(field_name)
            return [field_name]

    # Sinon (autre type d’élément), on continue le parcours
    champs_total = []
    for child in element:
        champs_total += parcourir_element(child, section_actuelle)
    return champs_total

# --- Parcours complet ---
for elem in root.iter("attributeEditorContainer"):
    parcourir_element(elem)

# Suppression des doublons tout en gardant l’ordre
champs_affiches = list(dict.fromkeys(champs_affiches))

# --- Affichage formaté ---
print("self.champs_affiches = [")
for c in champs_affiches:
    print(f'    "{c}",')
print("]\n")

print("sections = {")
for section, champs in sections.items():
    print(f'    "{section}": [')
    for c in champs:
        print(f'        "{c}",')
    print("    ],")
print("}")