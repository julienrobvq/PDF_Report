# dialogs/rapport_form_bathy_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_bathyDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Profondeur",
            "Comment",
        ]

        sections = {
            "Général": [
                "Profondeur",
                "Comment",
            ],
        }

        super().__init__("Form_Bathy", champs, sections)
