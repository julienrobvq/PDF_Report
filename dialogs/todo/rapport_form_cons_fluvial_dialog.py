# dialogs/rapport_form_cons_fluvial_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_cons_fluvialDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "mot_visi",
            "typ_ecou",
            "jur_ecou",
            "typ_conf",
            "com_conf",
            "sty_fluv",
            "com_fluv",
            "ind_inon",
            "ind_mobi",
            "dist_recul",
            "ind_avul",
            "ind_mouv",
            "ind_incv",
            "ind_aggr",
            "ind_obst",
            "com_indi",
            "prin_enj",
            "posi_enj",
            "dist_enj",
            "haut_enj",
            "autr_enj",
            "inter_rea",
            "inter_fut",
            "coord_o",
            "com_o",
            "com_gen",
            "photo1",
            "desc_p1",
            "photo2",
            "desc_p2",
            "photo3",
            "desc_p3",
            "com_p",
        ]

        sections = {
            "Environnement fluvial": [
                "mot_visi",
                "typ_ecou",
                "jur_ecou",
                "typ_conf",
                "com_conf",
                "sty_fluv",
                "com_fluv",
            ],
            "Indicateurs": [
                "ind_inon",
                "ind_mobi",
                "dist_recul",
                "ind_avul",
                "ind_mouv",
                "ind_incv",
                "ind_aggr",
                "ind_obst",
                "com_indi",
            ],
            "Enjeux": [
                "prin_enj",
                "posi_enj",
                "dist_enj",
                "haut_enj",
                "autr_enj",
            ],
            "Interventions": [
                "inter_rea",
                "inter_fut",
            ],
            "Observateur": [
                "coord_o",
                "com_o",
            ],
            "Commentaires": [
                "com_gen",
            ],
            "Photos": [
                "photo1",
                "desc_p1",
                "photo2",
                "desc_p2",
                "photo3",
                "desc_p3",
                "com_p",
            ],
        }

        super().__init__("Form_Cons_Fluvial", champs, sections)
