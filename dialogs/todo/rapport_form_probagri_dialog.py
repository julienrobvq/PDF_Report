# dialogs/rapport_form_probagri_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_probagriDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "site",
            "long",
            "lat",
            "problem1",
            "problem2",
            "problem3",
            "problem4",
            "comment",
            "photo",
            "amen1",
            "amen2",
            "comment2",
            "photo2",
        ]

        sections = {
            "Général": [
                "problem2",
                "problem3",
                "problem4",
            ],
            "Site": [
                "site",
                "long",
                "lat",
            ],
            "Problématique": [
                "problem1",
                "comment",
                "photo",
            ],
            "Sans titre": [
                "amen2",
            ],
            "Aménagement": [
                "amen1",
                "comment2",
                "photo2",
            ],
        }

        super().__init__("Form_ProbAgri", champs, sections)
