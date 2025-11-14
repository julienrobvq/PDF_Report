# dialogs/rapport_form_sediment_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_sedimentDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Sed_DepMeublAff",
            "Sed_LamEau",
            "Sed_EpaissDep",
            "Sed_Alluvion",
            "Sed_AlluvFreq",
            "Sed_DepRav",
            "Sed_DepTaille",
            "Sed_DepTailleRive",
            "Sed_DepEmbouch",
            "Sed_DepEmbTaille",
            "Sed_DepEmbRive",
        ]

        sections = {
            "Général": [
                "Sed_AlluvFreq",
                "Sed_DepTaille",
                "Sed_DepTailleRive",
            ],
            "Ampleur de l'envasement": [
                "Sed_DepMeublAff",
                "Sed_LamEau",
                "Sed_EpaissDep",
            ],
            "Alluvions": [
                "Sed_Alluvion",
                "Sed_DepRav",
                "Sed_DepEmbouch",
            ],
            "Sans titre": [
                "Sed_DepEmbTaille",
                "Sed_DepEmbRive",
            ],
        }

        super().__init__("Form_Sediment", champs, sections)
