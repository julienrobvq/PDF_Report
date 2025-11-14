# dialogs/rapport_form_infravert_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_infravertDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Type",
            "Etat",
            "Type_Obs",
            "PropPres",
            "Nom_Prop",
            "Urgence",
            "Comment_Gest",
            "Comment_Tech",
        ]

        sections = {
            "Général": [
                "Type",
                "Etat",
                "Comment_Gest",
                "Comment_Tech",
            ],
            "Sans titre": [
                "Type_Obs",
                "PropPres",
                "Nom_Prop",
                "Urgence",
            ],
        }

        super().__init__("Form_InfraVert", champs, sections)
