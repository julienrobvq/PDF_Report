# dialogs/rapport_form_peches_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_pechesDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "PlanEau",
            "Station",
            "Filet",
            "TypePlan",
            "Engin",
            "Heure_Pose",
            "Heure_Levee",
            "Maille",
            "Espece",
            "Poids_g",
            "Long_Tot_mm",
            "Long_Fourch_mm",
            "Sexe",
            "Maturite",
            "Otolithe",
            "Contenu_Stomach",
            "Comment",
        ]

        sections = {
            "Général": [
                "PlanEau",
                "Station",
                "Filet",
                "TypePlan",
                "Engin",
                "Heure_Pose",
                "Heure_Levee",
                "Maille",
                "Espece",
                "Poids_g",
                "Long_Tot_mm",
                "Long_Fourch_mm",
                "Sexe",
                "Maturite",
                "Otolithe",
                "Contenu_Stomach",
                "Comment",
            ],
        }

        super().__init__("Form_Peches", champs, sections)
