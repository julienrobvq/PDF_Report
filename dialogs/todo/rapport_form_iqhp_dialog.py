# dialogs/rapport_form_iqhp_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_iqhpDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Subs_Type1",
            "Subs_Type2",
            "NbType",
            "RecLimon",
            "Subs_Enlis",
            "MinBerg",
            "VegSurp",
            "Recif",
            "FossProf",
            "DebrLign",
            "Racin",
            "Couv_Bloc",
            "Meand",
            "Macrop",
            "Qt_Couv",
            "Sinuo",
            "CompRapFo",
            "Canal",
            "Stabil",
            "DLarg",
            "DUtilTer",
            "DEros",
            "GLarg",
            "GUtilTer",
            "GEros",
            "ELZmax",
            "Morpho",
            "torrentiel",
            "rapide",
            "modere",
            "lent",
            "tourbi",
            "intersti",
            "intermi",
            "ERZmax",
            "Subst",
            "Enlis",
            "IQHP_Comment",
            "Bilan_Substrat",
            "Bilan_Couvert",
            "Bilan_Morpho",
            "Bilan_Erosion",
            "Bilan_EauLent",
            "Bilan_EauRapide",
            "Bilan_IQHP",
        ]

        sections = {
            "Substrat": [
                "Subs_Type1",
                "Subs_Type2",
                "NbType",
            ],
            "Limon": [
                "RecLimon",
                "Subs_Enlis",
            ],
            "Couvert": [
                "MinBerg",
                "VegSurp",
                "Recif",
                "FossProf",
                "DebrLign",
                "Racin",
                "Couv_Bloc",
                "Meand",
                "Macrop",
                "Qt_Couv",
            ],
            "Morphologie": [
                "Sinuo",
            ],
            "Fausses/Rapides": [
                "CompRapFo",
            ],
            "Canalisation": [
                "Canal",
            ],
            "Stabilité": [
                "Stabil",
            ],
            "Berge droite": [
                "DLarg",
                "DUtilTer",
                "DEros",
            ],
            "Berge gauche": [
                "GLarg",
                "GUtilTer",
                "GEros",
            ],
            "Eaux lentes": [
                "ELZmax",
                "Morpho",
            ],
            "Courant": [
                "torrentiel",
                "rapide",
                "modere",
                "lent",
                "tourbi",
                "intersti",
                "intermi",
            ],
            "Eaux rapides": [
                "ERZmax",
                "Subst",
                "Enlis",
            ],
            "Bilan (IQHP)": [
                "IQHP_Comment",
                "Bilan_Substrat",
                "Bilan_Couvert",
                "Bilan_Morpho",
                "Bilan_Erosion",
                "Bilan_EauLent",
                "Bilan_EauRapide",
                "Bilan_IQHP",
            ],
        }

        super().__init__("Form_IQHP", champs, sections)
