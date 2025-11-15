# dialogs/rapport_form_habitataqua_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_habitataquaDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Sonde",
            "Profondeur",
            "Prof_Moins2m",
            "Vitesse",
            "Transparence",
            "Type_Fond",
            "Granulometrie",
            "Bois_Abri",
            "Bois_Precision",
            "Pierres_Abri",
            "Pierres_Precision",
            "Fosses_Abri",
            "Ombrage_VegLitt",
            "Herbier_VegLitt",
            "Berge_VegTot",
            "Berge_ArbrTot",
            "Berge_ArbuTot",
            "Berge_HerbTot",
            "Angle_Pente",
            "Talus_VegTot",
            "Talus_ArbrTot",
            "Talus_ArbuTot",
            "Talus_HerbTot",
        ]

        sections = {
            "Général": [
                "Bois_Precision",
            ],
            "Si moins de 2m": [
                "Prof_Moins2m",
            ],
            "Fond": [
                "Type_Fond",
                "Granulometrie",
            ],
            "Abri": [
                "Bois_Abri",
                "Pierres_Abri",
                "Fosses_Abri",
            ],
            "Si oui": [
                "Pierres_Precision",
            ],
            "Végétation littorale": [
                "Ombrage_VegLitt",
                "Herbier_VegLitt",
            ],
            "Végétation Berge/Talus": [
                "Berge_VegTot",
                "Berge_ArbrTot",
                "Berge_ArbuTot",
                "Berge_HerbTot",
                "Angle_Pente",
                "Talus_VegTot",
                "Talus_ArbrTot",
                "Talus_ArbuTot",
                "Talus_HerbTot",
            ],
        }

        super().__init__("Form_HabitatAqua", champs, sections)
