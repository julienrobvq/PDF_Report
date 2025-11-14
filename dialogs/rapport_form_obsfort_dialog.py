# dialogs/rapport_form_obsfort_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_obsfortDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Niv1",
            "Niv2",
            "Niv3",
            "Niv4",
            "Niv5",
            "Proportion",
            "Urgence",
            "Comment",
        ]

        sections = {
            "Général": [
                "Proportion",
                "Urgence",
                "Comment",
            ],
            "Niveau 1": [
                "Niv1",
            ],
            "Niveau 2": [
                "Niv2",
            ],
            "Niveau 3": [
                "Niv3",
            ],
            "Niveau 4": [
                "Niv4",
            ],
            "Niveau 5": [
                "Niv5",
            ],
        }

        super().__init__("Form_ObsFort", champs, sections)
