# dialogs/rapport_form_physicochimie_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_physicochimieDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "PlanEau",
            "Profond_m",
            "Temp_c",
            "Conductivite",
            "Conduct_Unite",
            "Unite_aut",
            "TDS",
            "Sal",
            "DO_%",
            "DO_mgL",
            "pH",
            "pH_mV",
            "ORP",
            "Transp_m",
            "Coul_Eau",
            "Station",
            "Comment",
            "Vent",
            "Meteo",
            "Utilisateur",
        ]

        sections = {
            "Général": [
                "PlanEau",
                "Profond_m",
                "Temp_c",
                "Conductivite",
                "Conduct_Unite",
                "TDS",
                "Sal",
                "DO_%",
                "DO_mgL",
                "pH",
                "pH_mV",
                "ORP",
                "Transp_m",
                "Coul_Eau",
                "Station",
                "Comment",
                "Vent",
                "Meteo",
                "Utilisateur",
            ],
            "Autre": [
                "Unite_aut",
            ],
        }

        super().__init__("Form_PhysicoChimie", champs, sections)
