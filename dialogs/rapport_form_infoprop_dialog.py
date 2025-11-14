# dialogs/rapport_form_infoprop_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_infopropDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "nolot",
            "maj",
            "Prenom_Prop",
            "Nom_Prop",
            "Sexe_Prop",
            "Age_Prop",
            "autreproprio",
            "Adr_No",
            "Adr_Rue",
            "Adr_App",
            "Adr_CodePost",
            "Adr_Ville",
            "tel",
            "cell",
            "courriel",
            "dateheure",
            "renc_notes",
            "autorisation_proprio",
            "Comment",
        ]

        sections = {
            "Général": [
                "nolot",
                "maj",
            ],
            "Propriétaire": [
                "Prenom_Prop",
                "Nom_Prop",
                "Sexe_Prop",
                "Age_Prop",
                "autreproprio",
            ],
            "Adresse": [
                "Adr_No",
                "Adr_Rue",
                "Adr_App",
                "Adr_CodePost",
                "Adr_Ville",
            ],
            "Contact": [
                "tel",
                "cell",
                "courriel",
            ],
            "Rencontre": [
                "dateheure",
                "renc_notes",
                "autorisation_proprio",
                "Comment",
            ],
        }

        super().__init__("Form_InfoProp", champs, sections)
