# dialogs/rapport_form_descenviro_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_descenviroDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "TAir",
            "TEau",
            "Transparence",
            "Meteo",
            "PluieRecente",
            "DirVent",
            "CaractVent",
            "Couv_Nuag",
            "Couv_For",
            "Menace",
        ]

        sections = {
            "Général": [
                "TAir",
                "TEau",
                "Transparence",
                "Meteo",
                "PluieRecente",
                "DirVent",
                "CaractVent",
                "Couv_Nuag",
                "Couv_For",
                "Menace",
            ],
        }

        super().__init__("Form_DescEnviro", champs, sections)
