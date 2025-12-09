# dialogs/rapport_form_erosion_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_erosionDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "Ero_Choix",
            "Ero_Comment",
            "Ero_Long",
            "Ero_Type",
            "Ero_Force",
            "Ero_Prio",
            "Ero_Trav",
            "Ero_Rive",
            "Terras",
            "Chen_Abd",
            "Banc_Perch",
            "Affouill_Infra",
            "Racin_Expo",
            "Chen_EtrProf",
            "Anc_Gliss",
            "Berge_Ero",
            "Lit_Compact",
            "Sed_Choix",
            "Sed_Comment",
            "Sed_Type",
            "DepotSemiAffl",
            "DepotMeublAffl",
            "LameEau",
            "EpaissDep",
            "Alluvion",
            "AlluvFreq",
            "DepotRav",
            "RavTaille",
            "RavTailleRive",
            "DepEmbouch",
            "DepEmbTaille",
            "DepEmbRive",
            "Epa_Sed",
            "Banc_Grav",
            "Infra_Ensouv",
            "Drag_Freq",
            "EspRed_Pont",
            "Delta_Cone",
            "Berg_PeuProf",
            "Stab_Comment",
            "Berge_Stab",
            "Banc_Veget",
            "Lit_Veget",
            "Abs_Sed",
        ]

        sections = {
            "Général": [
                "Ero_Type",
                "Ero_Trav",
                "Ero_Rive",
                "AlluvFreq",
                "RavTaille",
                "RavTailleRive",
            ],
            "Érosion": [
                "Ero_Choix",
                "Ero_Comment",
            ],
            "Version simplifiée": [
                "Ero_Long",
                "Sed_Type",
                "Ero_Force",
                "Ero_Prio",
            ],
            "Autres": [
                "Sed_Comment",
            ],
            "Version longue": [
            ],
            "Indice-Incision": [
                "Terras",
                "Chen_Abd",
                "Banc_Perch",
                "Affouill_Infra",
                "Racin_Expo",
                "Chen_EtrProf",
                "Anc_Gliss",
                "Berge_Ero",
                "Lit_Compact",
            ],
            "Sédimentation": [
                "Sed_Choix",
                "Sed_Comment",
            ],
            "Dépôts meubles semi-affleurant": [
                "DepotSemiAffl",
            ],
            "Ampleur de l'envasement": [
                "DepotMeublAffl",
                "LameEau",
                "EpaissDep",
            ],
            "Alluvions": [
                "Alluvion",
                "DepotRav",
                "DepEmbouch",
            ],
            "Sans titre": [
                "DepEmbTaille",
                "DepEmbRive",
            ],
            "Indice-Aggradation": [
                "Epa_Sed",
                "Banc_Grav",
                "Infra_Ensouv",
                "Drag_Freq",
                "EspRed_Pont",
                "Delta_Cone",
                "Berg_PeuProf",
            ],
            "Stabilité": [
                "Stab_Comment",
                "Berge_Stab",
                "Banc_Veget",
                "Lit_Veget",
                "Abs_Sed",
            ],
            "Photos": [
            ],
        }

        super().__init__("Form_Erosion", champs, sections)
