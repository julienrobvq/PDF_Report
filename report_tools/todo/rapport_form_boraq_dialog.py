# dialogs/rapport_form_boraq_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_boraqDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "OBSERVATEURS",
            "ORGANISATION",
            "Date_Saisie",
            "Saisie_Par",
            "Region",
            "Valid_Reg",
            "Ville",
            "Photo",
            "Ident_GPS",
            "Heure",
            "Date_Jour",
            "Date_Mois",
            "Date_Annee",
            "Tmp_Tot",
            "Long_Parc",
            "Larg_Parc",
            "Nb_Struct",
            "Type_Obs",
            "Nom_Commun",
            "Code_Esp",
            "Precision",
            "Cote_Chant",
            "Lieu_Capt",
            "Sexe",
            "ID_Indiv",
            "LIndiv",
            "LPastron",
            "LDossiere",
            "Poids",
            "Age",
            "capture",
            "Desc_Lieu",
            "Habitat",
            "Nb_Adulte",
            "Nb_Juvenile",
            "Nb_Oeuf",
            "Nb_Total",
            "Comment",
        ]

        sections = {
            "Général": [
                "Comment",
            ],
            "Observation": [
                "Type_Obs",
                "Nom_Commun",
                "Code_Esp",
                "Precision",
                "Cote_Chant",
                "Lieu_Capt",
                "Sexe",
                "ID_Indiv",
                "LIndiv",
                "Poids",
                "Age",
                "capture",
            ],
            "Tortue": [
                "LPastron",
                "LDossiere",
            ],
            "Habitat": [
                "Desc_Lieu",
                "Habitat",
                "Nb_Adulte",
                "Nb_Juvenile",
                "Nb_Oeuf",
                "Nb_Total",
            ],
        }

        super().__init__("Form_BORAQ", champs, sections)
