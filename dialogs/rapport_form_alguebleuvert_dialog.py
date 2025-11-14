# dialogs/rapport_form_alguebleuvert_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_alguebleuvertDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Cat_1",
            "Cat_2a",
            "Desc_2a",
            "Cat_2b",
            "Desc_2b",
            "Comment",
        ]

        sections = {
            "Général": [
                "Cat_1",
                "Cat_2a",
                "Cat_2b",
                "Comment",
            ],
            "Description - Catégorie 2a": [
                "Desc_2a",
            ],
            "Description - Catégorie 2b": [
                "Desc_2b",
            ],
        }

        super().__init__("Form_AlgueBleuVert", champs, sections)
