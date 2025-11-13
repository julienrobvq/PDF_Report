import xml.etree.ElementTree as ET

# --- Paramètres ---
qml_path = "activitedetection.qml"

# --- Lecture du fichier ---
tree = ET.parse(qml_path)
root = tree.getroot()

champs_affiches = []
sections = {}

def parcourir_element(element, section_actuelle=None):
    """
    Parcourt récursivement la structure du formulaire QGIS.
    Ignore les conteneurs qui ne contiennent aucun champ.
    """
    tag = element.tag
    name = element.attrib.get("name")

    # Conteneur (onglet, groupe, etc.)
    if tag in ("attributeEditorContainer", "attributeEditorForm", "attributeEditorRelation"):
        titre = name or "Sans titre"
        champs_section = []

        for child in element:
            champs_section += parcourir_element(child, section_actuelle=titre)

        # On n'ajoute la section que si elle contient des champs
        if champs_section:
            sections[titre] = champs_section

        return champs_section

    # Champ simple
    elif tag == "attributeEditorField":
        field_name = element.attrib.get("name")
        if field_name:
            champs_affiches.append(field_name)
            return [field_name]

    # Autres éléments
    champs_total = []
    for child in element:
        champs_total += parcourir_element(child, section_actuelle)

    return champs_total


# --- Parcours ---
for elem in root.iter("attributeEditorContainer"):
    parcourir_element(elem)

# Dédupliquer en gardant l'ordre
champs_affiches = list(dict.fromkeys(champs_affiches))


# -------------------------------------------------------------------
#           🔽 OUTPUT EXACTEMENT FORMATTÉ COMME TON EXEMPLE
# -------------------------------------------------------------------

def format_list(lst, indent=12):
    """
    Formatte une liste Python sur plusieurs lignes
    avec indentation personnalisée.
    """
    s = "[\n"
    for item in lst:
        s += " " * indent + f"\"{item}\",\n"
    s += " " * (indent - 4) + "]"
    return s


# --- Impression finale ---
print("champs = " + format_list(champs_affiches, indent=12) + "\n")

print("sections = {")
for section, champs in sections.items():
    print(f"    \"{section}\": " + format_list(champs, indent=12) + ",")
print("}")
