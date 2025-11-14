# dialogs/rapport_form_bene_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_beneDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Date",
            "Qui",
            "Type_Obs",
            "photo",
            "Insta_Pres",
            "Type_Travers",
            "Autre_Travers",
            "Travaux_Eff",
            "Autre_Travaux",
            "Materiaux_Trav",
            "Sign_Insta",
            "Recomm_Trav",
            "Comm",
        ]

        sections = {
            "Général": [
                "Date",
                "Qui",
                "Type_Obs",
                "photo",
                "Insta_Pres",
                "Type_Travers",
                "Travaux_Eff",
                "Sign_Insta",
                "Comm",
            ],
            "Sans titre": [
                "Recomm_Trav",
            ],
            "Écrire type de traverse": [
                "Autre_Travers",
            ],
            "Écrire nature des travaux effectués": [
                "Autre_Travaux",
            ],
            "Quel est le matériel de la traverse mis en place?": [
                "Materiaux_Trav",
            ],
        }

        super().__init__("Form_Bene", champs, sections)
