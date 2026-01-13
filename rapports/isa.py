# rapports/isa.py

import os
from .base import BaseRapport
from docxtpl import DocxTemplate
from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QMessageBox


class RapportISA(BaseRapport):

    def __init__(self, parent=None):

        super().__init__(
            layer_form_name="Form_ISA_Propriete",
            champs_affiches=[],
            parent=parent
        )

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

        template_path = os.path.join(os.path.dirname(__file__), "templates", "template_isa.docx")
        doc = DocxTemplate(template_path)

        items = []

        for feat_prop in self.current_feats_form:
            id_ref = feat_prop["id_instsept"]

            feat_puits = next((f for f in self.layer_puits.getFeatures() if f["adr_comp"] == id_ref), None)
            feat_fosse = next((f for f in self.layer_fosse.getFeatures() if f["adr_comp"] == id_ref), None)
            feat_epur = next((f for f in self.layer_epur.getFeatures() if f["adr_comp"] == id_ref), None)

            item = {
                "propriete": {},
                "puits": {},
                "fosse": {},
                "epurateur": {},
            }

            # propriete
            for champ in self.champs_affiches:
                if champ in self.layer_prop.fields().names():
                    item["propriete"][champ] = self.get_display_value(self.layer_prop, feat_prop, champ)

            # puits
            if feat_puits:
                for champ in self.champs_affiches:
                    if champ in self.layer_puits.fields().names():
                        item["puits"][champ] = self.get_display_value(self.layer_puits, feat_puits, champ)

            # fosse
            if feat_fosse:
                for champ in self.champs_affiches:
                    if champ in self.layer_fosse.fields().names():
                        item["fosse"][champ] = self.get_display_value(self.layer_fosse, feat_fosse, champ)

            # epurateur
            if feat_epur:
                for champ in self.champs_affiches:
                    if champ in self.layer_epur.fields().names():
                        item["epurateur"][champ] = self.get_display_value(self.layer_epur, feat_epur, champ)
            
            items.append(item)
        
        context = {"items": items}

        doc.render(context)
        doc.save(file_path)
        
        for l in (self.layer_form, self.layer_puits, self.layer_fosse, self.layer_epur):
            if l:
                l.removeSelection()
        
        QMessageBox.information(self, "Bravo", "Lettre ISA générée")