# dialogs/rapport_form_cons_traverse_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_cons_traverseDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "trav_ecou",
            "ty_trav",
            "nb_tuyaux",
            "mat_trav",
            "for_trav",
            "etat_trav",
            "diam_trav",
            "larg_pb",
            "enj_trav",
            "obs_trav",
            "pour_obs",
            "mat_obs1",
            "mat_obs2",
            "cast_trav",
            "com_gen",
            "photo1",
            "photo2",
            "photo3",
            "com_p",
        ]

        sections = {
            "Général": [
                "trav_ecou",
                "ty_trav",
                "nb_tuyaux",
                "mat_trav",
                "for_trav",
                "etat_trav",
                "diam_trav",
                "larg_pb",
                "enj_trav",
                "obs_trav",
                "pour_obs",
                "mat_obs1",
                "mat_obs2",
                "cast_trav",
                "com_gen",
            ],
            "Photos": [
                "photo1",
                "photo2",
                "photo3",
                "com_p",
            ],
        }

        super().__init__("Form_Cons_Traverse", champs, sections)
