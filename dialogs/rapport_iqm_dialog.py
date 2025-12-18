# dialogs/rapport_form_iqm_dialog.py
from .base_rapport_dialog import BaseRapportDialog
class RapportIQM(BaseRapportDialog):
    def __init__(self):
        champs = [
            "obs",
            "date",
            "nom_riv",
            "troncon",
            "confinemen",
            "longueur",
            "notesgener",
            "iqm",
            "indic_complet",
            "val_max",
            "iqm_partiel",
            "c1_desc",
            "c2_desc",
            "c3_desc",
            "c_comment",
            "a1_desc",
            "a2_desc",
            "a3_desc",
            "a4_desc",
            "a5_desc",
            "a6_desc",
            "a9_desc_1",
            "a10_desc",
            "a11_desc",
            "a12_desc",
            "a7_desc",
            "a8_desc",
            "a_comment",
            "f1_desc",
            "f9_desc",
            "f10_desc",
            "f11_desc",
            "f12_desc",
            "f13_desc",
            "f3_desc",
            "f6_desc",
            "f2_desc",
            "f4_desc",
            "f5_desc",
            "f7_desc",
            "f8_desc",
            "f_comment",
        ]
        sections = {
            "Métadonnées" : {
                "_level" : 2,
                "_field" : []
                },
            "Édition et mise à jour": {
                "_level" : 3,
                "_field" : ["obs", "date"]
            },

            "Tronçon" : {
                "_level" : 2,
                "_field" : []
            },
            "Propriétés du tronçon": {
                "_level" : 3,
                "_field" : [
                "nom_riv",
                "troncon",
                "confinemen",
                "longueur",
                "notesgener"]
            },
            "Diagnostic": {
                "_level" : 3,
                "_field" : ["iqm"]
            },
            "IQM proxi": {
                "_level" : 3,
                "_field" : 
                ["indic_complet",
                "val_max",
                "iqm_partiel"]
            },
            "Ajustements Patrons observés au niveau du chenal (trajectoire historique)": {
                "_level" : 3,
                "_field" :
                ["c1_desc",
                "c2_desc",
                "c3_desc"]
            },
            "Commentaires": {
                "_level" : 3,
                "_field" :
                ["c_comment"]
            },
            "Anthropisation" : {
                "_level" : 2,
                "_field" : []
            },
            "Patrons observés au niveau du chenal (trajectoire historique)" : {
                "_level" : 2,
                "_field" : []
            },
            "Tronçons confinés ou non confinés": {
                "_level" : 3,
                "_field" : ["a1_desc",
                "a2_desc",
                "a3_desc",
                "a4_desc",
                "a5_desc",
                "a6_desc",
                "a9_desc_1",
                "a10_desc",
                "a11_desc",
                "a12_desc"]
            },
            "Tronçons non confinés seulement": {
                "_level" : 3,
                "_field" : ["a7_desc",
                "a8_desc"]
            },
            "Commentaires": {
                "_level" : 3,
                "_field" : ["a_comment"]
            },
            "Fonctionnement Géomorphologique" : {
                "_level" : 2,
                "_field" : []
            },
            "Tronçons confinés ou non confinés": {
                "_level" : 3,
                "_field" : ["f1_desc",
                "f9_desc",
                "f10_desc",
                "f11_desc",
                "f12_desc",
                "f13_desc"]
            },
            "Tronçons confinés seulement": {
                "_level" : 3,
                "_field" : ["f3_desc",
                "f6_desc"]
            },
            "Tronçons non confinés seulement": {
                "_level" : 3,
                "_field" : ["f2_desc",
                "f4_desc",
                "f5_desc",
                "f7_desc",
                "f8_desc"]
            },
            "Commentaires": {
                "_level" : 3,
                "_field" : ["f_comment",]
            },
        }
        
        super().__init__("Form_IQM", champs, sections)