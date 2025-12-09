# dialogs/rapport_form_obstacle_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_obstacleDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Obt_Choix",
            "Obt_Type",
            "Obt_Ponceau",
            "Obt_Drain",
            "Obt_Comment",
            "Obt_Force",
            "Obt_Prio",
            "Obt_Statut",
            "barr_sever",
            "barr_haut",
            "barr_larg",
            "barr_pct_obst",
            "prof_eau",
        ]

        sections = {
            "Général": [
                "Obt_Choix",
            ],
            "Simplifiée": [
                "Obt_Type",
                "Obt_Force",
            ],
            "Ponceau": [
                "Obt_Ponceau",
            ],
            "Drain": [
                "Obt_Drain",
            ],
            "Autres": [
                "Obt_Comment",
            ],
            "Obstacle": [
                "Obt_Type",
                "Obt_Prio",
                "Obt_Statut",
                "barr_sever",
                "barr_haut",
                "barr_larg",
                "barr_pct_obst",
                "prof_eau",
                "Obt_Comment",
            ],
        }

        super().__init__("Form_Obstacle", champs, sections)
