# dialogs/rapport_mhh_dialog.py

from .base_rapport_dialog import BaseRapportDialog
from docxtpl import DocxTemplate
import os
from qgis.PyQt.QtWidgets import QMessageBox


class RapportMHH(BaseRapportDialog):

    def __init__(self, parent=None):

        champs_affiches = [
            "Nom_station",
            "Date",
            "Heure",
            "num_echant",
            "contexte",
            "Situat",
            "FormTerr",
            "Depress",
            "Depres_pct",
            "Montic_pct",
        ]

        # Sections vides (tu peux en ajouter plus tard pour le PDF)
        sections = {}

        super().__init__(
            layer_form_name="Form_MHH",
            champs_affiches=champs_affiches,
            sections=sections,
            parent=parent
        )

    def export_word(self, file_path, story, titre_rapport):

        template_path = os.path.join(
            os.path.dirname(__file__),
            "MHH_Template.docx"
        )
        doc = DocxTemplate(template_path)

        # Première fiche
        feat = self.current_feats_form[0]
        feats_evt = self.current_feats_evt
        feat_evt = next(
            (e for e in feats_evt if e["ID_EVEN"] == feat["ID_EVEN"]),
            None
        )

        context = {}

        for champ in self.current_champs:
            if champ in self.layer_form.fields().names():
                context[champ] = self.get_display_value(
                    self.layer_form, feat, champ
                )

            elif feat_evt and champ in self.layer_evt.fields().names():
                context[champ] = self.get_evt_display_value(
                    feat_evt, champ
                )

        context["titre_rapport"] = titre_rapport

        doc.render(context)
        doc.save(file_path)

        QMessageBox.information(self, "Bravo", "Rapport Milieu humide généré")
