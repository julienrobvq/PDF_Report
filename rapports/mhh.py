# rapports/mhh.py

import os
from .base import BaseRapport
from docxtpl import DocxTemplate
from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QMessageBox


class RapportMHH(BaseRapport):

    def __init__(self, parent=None):
        super().__init__(
            layer_form_name="Form_MHH",
            champs_affiches=[],
            parent=parent,
        )

        if not hasattr(self, "layer_form"):
            self._init_ok = False
            return

        self._init_ok = True

        self.layer_mhh = self.layer_form
        self.layer_even = QgsProject.instance().mapLayersByName("Evenement")[0]
        self.layer_sol = QgsProject.instance().mapLayersByName("FormSect_Sol")[0]
        self.layer_pert = QgsProject.instance().mapLayersByName("FormSect_TypePert")[0]
        self.layer_veget = QgsProject.instance().mapLayersByName("FormSect_SP_Veget")[0]

        # MHH + Evenement
        self.champs_affiches = [
            "Nom_Station",
            "num_echant",
            "Contexte",
            "Situat",
            "FormTerr",
            "Depress",
            "Depres_Pct",
            "Montic_Pct",
            "Date",
            "Evalu_Princ",
            "Veg_Pert",
            "Sol_Pert",
            "Hydro_Pert",
            "MAnth",
            "Barr_Cast",
            "pression",
            "press_distance",
            "Eau_SurfLib",
            "Lien_Hydro",
            "Lien_Hydro_Type",
            "Litiere_Noir",
            "Effet_Rhizo",
            "Ecorc_Erod",
            "Inond",
            "Satur_Surf",
            "Lign_Marqu_Eau",
            "Debris_Depot",
            "Odeur_Souf",
            "Racine_Hors",
            "Mousse_Tronc",
            "Souch_Hyper",
            "Lentic_Hyper",
            "Racin_Surf",
            "Racin_Adven",
            "Prof_Roc",
            "sol_redox",
            "sol_reduct",
            "Cas_Cpx",
            "Prof_Nap",
            "Class_Draing",
            "Draing_Oblq",
            "Veg_DomH",
            "Veg_DomNH",
            "Bil_Veg",
            "Bil_Hyd",
            "Bil_SolHydro",
            "Bilan_MH",
            "Bil_Comment",
            "type_mh",
            "tourb_type",
        ]

        self.sol_fields = ["Typ_Horiz", "Epais_Horiz", "Typ_SolOrg", "prof_debut", "prof_fin",
                           "horizon", "Typ_Text", "Coul_Teint", "Mouc_Teint", "Mouc_Abond", "Mouc_Dim", "Mouc_Ctrst",]
        self.pert_fields = ["Type_Pert"]
        self.veget_fields = ["Strate", "Espece", "hauteur", "Recouv_Abs_Num", "Recouv_Rel_Num", "Dom", "Statut",]

    def exec_(self):
        if not getattr(self, "_init_ok", True):
            return 0
        return super().exec_()

    def _feat_to_dict(self, layer, feat, fields):
        d = {}
        for name in fields:
            if name in layer.fields().names():
                d[name] = self.get_display_value(layer, feat, name)
        return d

    def export_word(self, file_path):
        template_path = os.path.join(os.path.dirname(__file__), "templates", "template_mhh.docx")
        doc = DocxTemplate(template_path)

        items = []

        even_by_id = {f["ID_EVEN"]: f for f in self.current_feats_even if f["ID_EVEN"] not in (None, "", " ")}

        sols_by_mhh = {}
        for f in self.layer_sol.getFeatures():
            k = f["ID_MHH"]
            if k in (None, "", " "):
                continue
            sols_by_mhh.setdefault(k, []).append(f)

        perts_by_mhh = {}
        for f in self.layer_pert.getFeatures():
            k = f["ID_MH"]
            if k in (None, "", " "):
                continue
            perts_by_mhh.setdefault(k, []).append(f)


        vegs_by_mhh = {}
        for f in self.layer_veget.getFeatures():
            k = f["ID_MHH"]
            if k in (None, "", " "):
                continue
            vegs_by_mhh.setdefault(k, []).append(f)

        for feat_mhh in self.current_feats_form:
            id_mhh = feat_mhh["ID_MHH"]
            id_even = feat_mhh["ID_EVEN"]
            feat_even = even_by_id.get(id_even)

            item = {
                "mhh": {},
                "even": {},
                "sols": [],
                "perts": [],
                "vegets": [],
            }

            # MHH
            for champ in self.champs_affiches:
                if champ in self.layer_mhh.fields().names():
                    item["mhh"][champ] = self.get_display_value(self.layer_mhh, feat_mhh, champ)

            # Evenement
            if feat_even:
                for champ in self.champs_affiches:
                    if champ in self.layer_even.fields().names():
                        item["even"][champ] = self.get_display_value(self.layer_even, feat_even, champ)

            # Sols
            for f in sols_by_mhh.get(id_mhh, []):
                item["sols"].append(self._feat_to_dict(self.layer_sol, f, self.sol_fields))

            # Perturbations
            for f in perts_by_mhh.get(id_mhh, []):
                item["perts"].append(self._feat_to_dict(self.layer_pert, f, self.pert_fields))

            # Végétation
            for f in vegs_by_mhh.get(id_mhh, []):
                item["vegets"].append(self._feat_to_dict(self.layer_veget, f, self.veget_fields))

            items.append(item)

        doc.render({"items": items})
        doc.save(file_path)

        for lyr in (self.layer_even, self.layer_form, self.layer_sol, self.layer_pert, self.layer_veget):
            if lyr:
                lyr.removeSelection()

        QMessageBox.information(self, "Rapport", "Rapport Milieu humide généré.")