# dialogs/rapport_form_adu_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_aduDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Site",
            "CooGPSX",
            "CooGPSY",
            "Munic",
            "Repere",
            "ProprioTyp",
            "Prec",
            "Prec_Av",
            "Erosion",
            "Permeab",
            "Type_Surf",
            "AD_Ruiss",
            "Direc_AD",
            "Exutoire_Drain",
            "Sect_Prob",
            "Cont_Ruiss",
            "Contrainte",
            "ContrCom",
            "Comm1",
            "Comm2",
            "Recommandation",
            "photo1",
            "photo2",
        ]

        sections = {
            "Général": [
                "Site",
                "CooGPSX",
                "CooGPSY",
                "Munic",
                "Repere",
                "ProprioTyp",
                "Prec",
                "Prec_Av",
                "Erosion",
                "Permeab",
                "Type_Surf",
                "AD_Ruiss",
                "Direc_AD",
                "Exutoire_Drain",
                "Sect_Prob",
                "Cont_Ruiss",
                "Contrainte",
                "ContrCom",
                "Comm1",
                "Comm2",
                "Recommandation",
            ],
            "Photos": [
                "photo1",
                "photo2",
            ],
        }

        super().__init__("Form_ADU", champs, sections)
