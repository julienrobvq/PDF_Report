# dialogs/rapport_form_cons_obstruction_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_cons_obstructionDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "og_obs1",
            "og_obs2",
            "com_obs",
            "deg_obs",
            "larg_obs",
            "haut_obs",
            "stab_obs",
            "ind_stab",
            "ind_cast",
            "bar_cast",
            "com_cast",
            "pres_trav",
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
            "Général": [
                "og_obs1",
                "og_obs2",
                "com_obs",
                "deg_obs",
                "larg_obs",
                "haut_obs",
                "stab_obs",
                "ind_stab",
                "ind_cast",
                "bar_cast",
                "com_cast",
                "pres_trav",
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

        super().__init__("Form_Cons_Obstruction", champs, sections)
