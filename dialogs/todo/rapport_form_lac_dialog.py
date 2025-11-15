# dialogs/rapport_form_lac_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_lacDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "nom",
            "ville",
            "obv",
            "num_rsvl",
            "x",
            "y",
            "superficie",
            "perimetre",
            "long_max",
            "larg_max",
            "fetch",
            "profon_moy",
            "profon_max",
            "rap_prof",
            "volume",
            "dev_perim",
            "nbr_iles",
            "surf_prog",
            "vol_prof",
            "alt",
            "position",
            "charge",
            "exutoire",
            "deb_exu",
            "renouvel",
            "int_renouv",
            "ratio_drain",
            "int_drain",
            "temps_res",
            "comment",
        ]

        sections = {
            "Identification du lac": [
                "nom",
                "ville",
                "obv",
                "num_rsvl",
                "x",
                "y",
            ],
            "Hydromorphologie": [
                "superficie",
                "perimetre",
                "long_max",
                "larg_max",
                "fetch",
                "profon_moy",
                "profon_max",
                "rap_prof",
                "volume",
                "dev_perim",
                "nbr_iles",
                "surf_prog",
                "vol_prof",
                "alt",
                "position",
                "charge",
                "exutoire",
                "deb_exu",
                "renouvel",
                "int_renouv",
                "ratio_drain",
                "int_drain",
                "temps_res",
                "comment",
            ],
        }

        super().__init__("Form_Lac", champs, sections)
