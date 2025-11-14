# dialogs/rapport_form_idec_dialog.py

from .base_rapport_dialog import BaseRapportDialog

class RapportForm_idecDialog(BaseRapportDialog):
    def __init__(self):

        champs = [
            "num_station",
            "riviere",
            "localite",
            "date_heure",
            "analyste",
            "coordox_wsg84",
            "coordoy_wsg84",
            "echantillon",
            "temperaturec",
            "ph",
            "conductivite",
            "o2_diss_mgl",
            "o2_diss_heure",
            "o2_diss_pourcent",
            "mes_turb",
            "mes_turb_unite",
            "niveau_eau",
            "courant",
            "transparence",
            "acc_sed_fins",
            "biom_periph",
            "lumiere",
            "pierre_bloc",
            "cailloux",
            "beton",
            "substrats_ajoutes",
            "sediments_nrecomm",
            "mousse",
            "alguefil",
            "plante_aqua",
            "flor_cyano",
            "autres_obs",
            "photo_amont",
            "photo_aval",
            "photo_subtrat",
            "commentaires",
        ]

        sections = {
            "Nom": [
                "num_station",
                "riviere",
                "localite",
                "date_heure",
                "analyste",
                "coordox_wsg84",
                "coordoy_wsg84",
            ],
            "Multisonde": [
                "echantillon",
                "temperaturec",
                "ph",
                "conductivite",
                "o2_diss_mgl",
                "o2_diss_heure",
                "o2_diss_pourcent",
                "mes_turb",
                "mes_turb_unite",
            ],
            "Observation": [
                "niveau_eau",
                "courant",
                "transparence",
                "acc_sed_fins",
                "biom_periph",
                "lumiere",
            ],
            "Diatomée": [
                "mousse",
                "alguefil",
                "plante_aqua",
                "flor_cyano",
                "autres_obs",
            ],
            "Description du substrat": [
                "pierre_bloc",
                "cailloux",
                "beton",
                "substrats_ajoutes",
                "sediments_nrecomm",
            ],
            "Photo": [
                "photo_amont",
                "photo_aval",
                "photo_subtrat",
            ],
            "Commentaires": [
                "commentaires",
            ],
        }

        super().__init__("Form_IDEC", champs, sections)
