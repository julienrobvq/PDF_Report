# dialogs/rapport_form_admin_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_adminDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Secteur",
            "Rue",
            "Adresse",
            "Typ_Constr",
            "PreNom_Proprio1",
            "PreNom_Proprio2",
            "Num_Tel1",
            "Num_Tel2",
            "Courriel",
            "Date_Vis1",
            "Renc_Proprio1",
            "Meteo_Vis1",
            "Date_Vis2",
            "Renc_Proprio2",
            "Meteo_Vis2",
            "Date_RDV",
            "ListeJdP_2023",
            "Suivi_Faire",
            "Sujet_Suivi",
            "Suivi_Fait",
            "Date",
            "Comm_Autres",
        ]

        sections = {
            "Général": [
                "ListeJdP_2023",
                "Suivi_Faire",
                "Sujet_Suivi",
                "Suivi_Fait",
                "Date",
                "Comm_Autres",
            ],
            "Administration": [
                "Secteur",
                "Rue",
                "Adresse",
                "Typ_Constr",
                "PreNom_Proprio1",
                "PreNom_Proprio2",
                "Num_Tel1",
                "Num_Tel2",
                "Courriel",
                "Date_Vis1",
                "Renc_Proprio1",
                "Meteo_Vis1",
                "Date_Vis2",
                "Renc_Proprio2",
                "Meteo_Vis2",
                "Date_RDV",
            ],
            "Formulaire Gouttière": [
            ],
        }

        super().__init__("Form_Admin", champs, sections)
