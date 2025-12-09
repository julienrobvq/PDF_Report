# dialogs/rapport_eee_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportEEEDialog(BaseRapportDialog):
    def __init__(self):
        champs = [
            "site", "zgie", "region", "Munic", "mrc", "Respo", "Milieu",
            "Repere", "Contrainte", "categorie", "EEE_Type", "lat_flore",
            "autre_sp", "autre_nom_latin", "Superf_m2", "StadeDev",
            "site_autre_stade", "site_stade_1", "site_stade_2",
            "site_stade_3", "site_stade_4", "site_stade_5",
            "cause_probag", "hote", "Trt_av", "Trt_avQui",
            "Trt_avType", "TraitRecom", "EEE_Comment", "photo1"
        ]

        sections = {
            "Identification": ["site", "Date", "Heure", "ID_Proj", "ID_Employ"],
            "Localisation": [
                "site", "zgie", "region", "Munic", "mrc", "Respo",
                "Milieu", "Repere", "Contrainte"
            ],
            "Observations": [
                "categorie", "EEE_Type", "lat_flore", "autre_sp",
                "autre_nom_latin", "Superf_m2", "StadeDev",
                "site_autre_stade", "site_stade_1", "site_stade_2",
                "site_stade_3", "site_stade_4", "site_stade_5",
                "cause_probag", "hote"
            ],
            "Traitement": [
                "Trt_av", "Trt_avQui", "Trt_avType", "TraitRecom"
            ],
            "Commentaires et photos": ["EEE_Comment", "photo1"]
        }

        super().__init__("Form_EEE", champs, sections)
