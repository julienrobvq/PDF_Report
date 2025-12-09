# dialogs/rapport_form_vegetberge_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_vegetbergeDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Type_Veget",
            "Dens_EmergIndig",
            "Dens_EmergEEE",
            "Esp_EEE",
            "Dens_Immerg",
            "Ombrage",
        ]

        sections = {
            "Général": [
                "Type_Veget",
                "Dens_EmergIndig",
                "Dens_EmergEEE",
                "Esp_EEE",
                "Dens_Immerg",
            ],
            "Sans titre": [
                "Ombrage",
            ],
        }

        super().__init__("Form_VegetBerge", champs, sections)
