# dialogs/rapport_form_goutt_suivi_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_goutt_suiviDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Date_Suiv",
            "Nom_Insp_Suiv",
            "Situat_Suiv",
            "Amenag_Suiv",
            "Conform_Suiv",
            "Comment_Suiv",
            "Photo_Suiv",
        ]

        sections = {
            "Général": [
                "Date_Suiv",
                "Nom_Insp_Suiv",
                "Situat_Suiv",
                "Amenag_Suiv",
                "Conform_Suiv",
                "Comment_Suiv",
                "Photo_Suiv",
            ],
        }

        super().__init__("Form_Goutt_Suivi", champs, sections)
