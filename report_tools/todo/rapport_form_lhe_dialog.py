# dialogs/rapport_form_lhe_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_lheDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Station",
            "TypeMilieu",
            "EchancSol",
            "RacineNue",
            "SolDenude",
            "Debris",
            "MarquesLineaire",
            "Lichen",
            "LimiteLitiere",
            "Mousses",
            "Limite_Sup",
            "Limite_Inf",
            "PositionLHE",
            "RiveOppos",
            "NivConfiance",
            "LocalPrecis",
            "Comment",
        ]

        sections = {
            "Général": [
                "Station",
                "TypeMilieu",
                "Limite_Sup",
                "Limite_Inf",
                "PositionLHE",
                "RiveOppos",
                "NivConfiance",
                "LocalPrecis",
                "Comment",
            ],
            "Signes biophysiques": [
                "EchancSol",
                "RacineNue",
                "SolDenude",
                "Debris",
                "MarquesLineaire",
                "Lichen",
                "LimiteLitiere",
                "Mousses",
            ],
        }

        super().__init__("Form_LHE", champs, sections)
