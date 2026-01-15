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
            "Type_Pert",
            "pression",
            "press_distance",
            "Eau_SurfLib",
            "Lien_Hydro",
            "Lien_Hydro_Type",
        ]

    def exec_(self):
        if not getattr(self, "_init_ok", True):
            return 0
        return super().exec_()

    def export_word(self, file_path):

        template_path = os.path.join(os.path.dirname(__file__), "templates", "template_mhh.docx")
        doc = DocxTemplate(template_path)

        items = []

        for feat_mhh in self.current_feats_form:
            id_ref = feat_mhh["ID_MHH"]

            feat_even = next(
                (f for f in self.current_feats_even if f["ID_EVEN"] == feat_mhh["ID_EVEN"]),
                None
            )

            feat_sol = next((f for f in self.layer_sol.getFeatures() if f["ID_MHH"] == id_ref), None)
            feat_pert = next((f for f in self.layer_pert.getFeatures() if f["ID_MH"] == id_ref), None)
            feat_veget = next((f for f in self.layer_veget.getFeatures() if f["ID_MHH"] == id_ref), None)

            item = {
                "mhh": {},
                "even": {},
                "sol": {},
                "pert": {},
                "veget": {},
            }

            # mhh
            for champ in self.champs_affiches:
                if champ in self.layer_mhh.fields().names():
                    item["mhh"][champ] = self.get_display_value(self.layer_mhh, feat_mhh, champ)

            # evenement
            if feat_even:
                for champ in self.champs_affiches:
                    if champ in self.layer_even.fields().names():
                        item["even"][champ] = self.get_display_value(self.layer_even, feat_even, champ)

            # sol
            if feat_sol:
                for champ in self.champs_affiches:
                    if champ in self.layer_sol.fields().names():
                        item["sol"][champ] = self.get_display_value(self.layer_sol, feat_sol, champ)

            # perturbations
            if feat_pert:
                for champ in self.champs_affiches:
                    if champ in self.layer_pert.fields().names():
                        item["pert"][champ] = self.get_display_value(self.layer_pert, feat_pert, champ)

            # vegetation
            if feat_veget:
                for champ in self.champs_affiches:
                    if champ in self.layer_veget.fields().names():
                        item["veget"][champ] = self.get_display_value(self.layer_veget, feat_veget, champ)

            items.append(item)

        context = {"items": items}

        doc.render(context)
        doc.save(file_path)

        for l in (self.layer_even, self.layer_form, self.layer_sol, self.layer_pert, self.layer_veget):
            if l:
                l.removeSelection()

        QMessageBox.information(self, "Bravo", f"Rapport Milieu humide généré.")