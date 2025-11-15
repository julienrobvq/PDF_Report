# dialogs/rapport_form_goutt_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_gouttDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "AmenagGoutt",
            "AmenagGoutt_Autre",
            "Evac",
            "pompe",
            "pompe_evac",
            "pompe_comm",
            "amenag_init",
            "CommGoutt",
            "Source",
            "AmenagProp",
            "AmenagProp_Autre",
            "photo",
            "conform_init",
        ]

        sections = {
            "Général": [
                "AmenagGoutt",
                "AmenagGoutt_Autre",
                "pompe",
                "amenag_init",
                "CommGoutt",
                "Source",
                "AmenagProp",
                "AmenagProp_Autre",
                "photo",
                "conform_init",
            ],
            "Si connecté au drain": [
                "Evac",
            ],
            "Si pompe": [
                "pompe_evac",
                "pompe_comm",
            ],
            "Suivi": [
            ],
        }

        super().__init__("Form_Goutt", champs, sections)
