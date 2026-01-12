# rapports/isa.py

import os
from .base import BaseRapportDialog
from docxtpl import DocxTemplate
from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QMessageBox


class RapportISA(BaseRapportDialog):

    def __init__(self, parent=None):

        super().__init__(
            layer_form_name="Form_ISA_Propriete",
            champs_affiches=[],
            parent=parent
        )

        # si couche prop est pas la on cancel
        if not hasattr(self, "layer_form"):
            self._init_ok = False
            return

        self._init_ok = True

        self.layer_prop = self.layer_form

        self.layer_puits = QgsProject.instance().mapLayersByName("Form_ISA_Puits")[0]
        self.layer_fosse = QgsProject.instance().mapLayersByName("Form_ISA_Fosse")[0]
        self.layer_epur = QgsProject.instance().mapLayersByName("Form_ISA_Epurateur")[0]

        self.champs_affiches = [
            "matricule", "adr_comp", "Prenom_Prop", "Nom_Prop", "autreproprio",
            "tel", "dateconst", "utilbati", "nbchambre", "anneevid",
            "rejetdirect", "class_prel", "recommand", "Adr_No", "Adr_Rue",
            "Adr_Ville", "nolot", "Date", "typebati", "directives",
            "systprimaire", "capfosse", "anneesystsec", "syst_part", "etat_fosse",
            "etat_couv", "accescouvfosse", "prefiltre", "mat_couv", "etat_couv",
            "sysprimaire", "etat_fosse", "cons_pol",
            "type_alim", "alim_com",
            "systsec", "anne_const", "systsecav"
        ]

    def exec_(self):
        if not getattr(self, "_init_ok", True):
            return 0
        return super().exec_()

    def export_word(self, file_path):

        template_path = os.path.join(
            os.path.dirname(__file__),
            "template_isa.docx"
        )
        doc = DocxTemplate(template_path)

        feat_prop = self.current_feats_form[0]
        id_ref = feat_prop["id_instsept"]

        feat_puits = next(
            (f for f in self.layer_puits.getFeatures() if f["adr_comp"] == id_ref),
            None
        )
        feat_fosse = next(
            (f for f in self.layer_fosse.getFeatures() if f["adr_comp"] == id_ref),
            None
        )
        feat_epur = next(
            (f for f in self.layer_epur.getFeatures() if f["adr_comp"] == id_ref),
            None
        )

        context = {
            "propriete": {},
            "puits": {},
            "fosse": {},
            "epurateur": {},
        }

        for champ in self.champs_affiches:
            if champ in self.layer_prop.fields().names():
                context["propriete"][champ] = self.get_display_value(
                    self.layer_prop, feat_prop, champ
                )

        if feat_puits:
            for champ in self.champs_affiches:
                if champ in self.layer_puits.fields().names():
                    context["puits"][champ] = self.get_display_value(
                        self.layer_puits, feat_puits, champ
                    )

        if feat_fosse:
            for champ in self.champs_affiches:
                if champ in self.layer_fosse.fields().names():
                    context["fosse"][champ] = self.get_display_value(
                        self.layer_fosse, feat_fosse, champ
                    )

        if feat_epur:
            for champ in self.champs_affiches:
                if champ in self.layer_epur.fields().names():
                    context["epurateur"][champ] = self.get_display_value(
                        self.layer_epur, feat_epur, champ
                    )

        doc.render(context)
        doc.save(file_path)
        QMessageBox.information(self, "Bravo", "Lettre ISA générée")