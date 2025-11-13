# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QComboBox, QCheckBox, QLabel, QPushButton,
    QScrollArea, QWidget, QGridLayout, QMessageBox, QHBoxLayout,
    QLineEdit, QFileDialog
)
from qgis.core import QgsProject, QgsExpression
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet
import os


class RapportEEE(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outil de création de rapport")
        self.resize(380, 420)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sélectionnez un projet :"))
        self.proj_combo = QComboBox()
        layout.addWidget(self.proj_combo)

        layout.addWidget(QLabel("Titre du rapport :"))
        self.titre_rapport = QLineEdit()
        layout.addWidget(self.titre_rapport)

        layout.addWidget(QLabel("Champs à inclure dans le rapport :"))
        scroll = QScrollArea()
        container = QWidget()
        self.champ_layout = QGridLayout(container)
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)

        btn_layout = QHBoxLayout()
        self.btn_select_all = QPushButton("Tout sélectionner")
        self.btn_unselect_all = QPushButton("Tout désélectionner")
        btn_layout.addWidget(self.btn_select_all)
        btn_layout.addWidget(self.btn_unselect_all)
        layout.addLayout(btn_layout)

        self.btn_select_all.clicked.connect(self.select_all)
        self.btn_unselect_all.clicked.connect(self.unselect_all)

        self.btn_ok = QPushButton("Générer le rapport")
        layout.addWidget(self.btn_ok)
        self.btn_ok.clicked.connect(self.accept)

        #  Couches QGIS 
        self.layer_form = QgsProject.instance().mapLayersByName("Form_EEE")[0] # À modifier pour autre rapport
        self.layer_evt = QgsProject.instance().mapLayersByName("Evenement")[0]

        #  Champs à afficher - À modifier pour autre rapport

        self.champs_affiches = [
            "site", "zgie", "region", "Munic", "mrc", "Respo", "Milieu",
            "Repere", "Contrainte", "categorie", "EEE_Type", "lat_flore",
            "autre_sp", "autre_nom_latin", "Superf_m2", "StadeDev",
            "site_autre_stade", "site_stade_1", "site_stade_2", "site_stade_3",
            "site_stade_4", "site_stade_5", "cause_probag", "hote", "Trt_av",
            "Trt_avQui", "Trt_avType", "TraitRecom", "EEE_Comment", "photo1"
        ]
        self.champs_evenement = ["Date", "Heure", "ID_Proj"]
        self.champs_affiches = self.champs_evenement + self.champs_affiches

        self.id_field_proj = "ID_Proj"
        self.remplir_projets()
        self.remplir_champs()

    def remplir_projets(self):
        """Affiche les projets une seule fois, valeur visible + valeur brute """
        field = self.layer_evt.fields().field(self.id_field_proj)
        cfg = field.editorWidgetSetup()

        projets_dict = {}  # {valeur_brute: valeur_visible}

        for f in self.layer_evt.getFeatures():
            raw_value = f[self.id_field_proj]
            if raw_value in (None, "", " "):
                continue

            display_value = raw_value
            if cfg.type() == "ValueMap":
                mapping = cfg.config().get("map", {})
                display_value = mapping.get(str(raw_value), raw_value)
            elif cfg.type() == "ValueRelation":
                rel_layer_id = cfg.config().get("Layer")
                key_field = cfg.config().get("Key")
                value_field = cfg.config().get("Value")
                rel_layer = QgsProject.instance().mapLayer(rel_layer_id)
                if rel_layer:
                    for rel_feat in rel_layer.getFeatures():
                        if str(rel_feat[key_field]) == str(raw_value):
                            display_value = rel_feat[value_field]
                            break

            projets_dict[str(raw_value)] = str(display_value)

        for raw, display in sorted(projets_dict.items(), key=lambda x: x[1]):
            self.proj_combo.addItem(display, raw)

    def remplir_champs(self):
        self.checkboxes = []
        for i, champ in enumerate(self.champs_affiches):
            if champ in self.layer_form.fields().names():
                # Alias provenant de la couche Form_EEE
                alias = self.layer_form.fields().field(champ).alias() or champ

            elif champ in self.layer_evt.fields().names():
                # Alias provenant de la couche Evenement
                alias = self.layer_evt.fields().field(champ).alias() or champ

            else:
                alias = champ

            cb = QCheckBox(alias)
            cb.setToolTip(champ)
            self.champ_layout.addWidget(cb, i, 0)
            self.checkboxes.append(cb)

    def select_all(self):
        for cb in self.checkboxes:
            cb.setChecked(True)

    def unselect_all(self):
        for cb in self.checkboxes:
            cb.setChecked(False)

    def get_selection(self):
        id_proj = self.proj_combo.currentData()  # valeur brute
        champs = [cb.toolTip() for cb in self.checkboxes if cb.isChecked()]
        titre = self.titre_rapport.text()
        return id_proj, champs, titre


def get_display_value(layer, feature, field_name):
    """Retourne la valeur affichée dans QGIS pour un champ donné."""
    field = layer.fields().field(field_name)
    cfg = field.editorWidgetSetup()
    value = feature.attribute(field_name)

    if value in (None, ""):
        return ""

    # ValueMap
    if cfg.type() == "ValueMap":
        mapping = cfg.config().get("map", {})
        for k, v in mapping.items():
            if str(k) == str(value):
                return v
        return str(value)

    # ValueRelation
    if cfg.type() == "ValueRelation":
        rel_layer_id = cfg.config().get("Layer")
        key_field = cfg.config().get("Key")
        value_field = cfg.config().get("Value")
        rel_layer = QgsProject.instance().mapLayer(rel_layer_id)
        if rel_layer:
            for f in rel_layer.getFeatures():
                if str(f[key_field]) == str(value):
                    return str(f[value_field])
        return str(value)

    return str(value)


#  Création du rapport
dlg = RapportEEE()
if dlg.exec_():
    id_proj, champs, titre_rapport = dlg.get_selection()

    layer_evt = QgsProject.instance().mapLayersByName("Evenement")[0]
    expr_evt = QgsExpression.createFieldEqualityExpression("ID_Proj", str(id_proj))
    layer_evt.selectByExpression(expr_evt)
    feats_evt = layer_evt.selectedFeatures()

    if not feats_evt:
        QMessageBox.warning(None, "Avertissement", f"Aucun événement trouvé pour le projet {id_proj}.")
    else:
        #  Récupérer tous les ID_EVEN associés 
        id_even_values = [f["ID_EVEN"] for f in feats_evt if f["ID_EVEN"] not in (None, "", " ")]
        if not id_even_values:
            QMessageBox.warning(None, "Avertissement", "Aucun ID_EVEN trouvé pour ce projet.")
        else:
            layer_form = QgsProject.instance().mapLayersByName("Form_EEE")[0] # À modifier pour un autre rapport
            valeurs_str = ",".join([f"'{v}'" for v in id_even_values])
            expr_form = f'"ID_EVEN" IN ({valeurs_str})'
            layer_form.selectByExpression(expr_form)
            feats_form = layer_form.selectedFeatures()

            if not feats_form:
                QMessageBox.warning(None, "Avertissement", "Aucun enregistrement trouvé pour ces événements.")
            else:
                #  Choisir le fichier de sortie 
                file_path, _ = QFileDialog.getSaveFileName(
                    None,
                    "Enregistrer le rapport",
                    "Rapport.pdf",
                    "Fichiers PDF (*.pdf)"
                )

                # --- Dossier DCIM situé à côté du projet QGIS actif ---
                project_path = QgsProject.instance().fileName()
                project_dir = os.path.dirname(project_path)
                photo_root = os.path.join(project_dir, "DCIM")

                # Vérification de l’existence du dossier
                if not os.path.exists(photo_root):
                    QMessageBox.warning(None, "Avertissement", f"Dossier 'DCIM' introuvable :\n{photo_root}")
                if not file_path:
                    QMessageBox.information(None, "Annulé", "Génération du rapport annulée.")
                else:
                    #  Création du PDF 
                    doc = SimpleDocTemplate(file_path, pagesize=A4)
                    styles = getSampleStyleSheet()
                    story = []

                    #  Titre
                    story.append(Paragraph(titre_rapport, styles["Title"]))
                    story.append(Spacer(1, 20))

                    #  Parcourir chaque enregistrement Form_EEE 
                    for idx, feat in enumerate(feats_form):
                        # Lier l'événement correspondant
                        id_even = feat["ID_EVEN"]
                        feat_evt = next((e for e in feats_evt if e["ID_EVEN"] == id_even), None)

                        if not feat_evt:
                            continue

                        def get_evt_display_value(field_name):
                            field = feat_evt.fields().field(field_name)
                            cfg = field.editorWidgetSetup()
                            value = feat_evt.attribute(field_name)
                            if value in (None, ""):
                                return ""
                            if hasattr(value, "toString"):
                                type_name = type(value).__name__
                                if "QDateTime" in type_name:
                                    return value.toString("yyyy-MM-dd HH:mm")
                                elif "QTime" in type_name:
                                    return value.toString("HH:mm")
                                elif "QDate" in type_name:
                                    return value.toString("yyyy-MM-dd")
                            if cfg.type() == "ValueMap":
                                mapping = cfg.config().get("map", {})
                                for k, v in mapping.items():
                                    if str(k) == str(value):
                                        return v
                            if cfg.type() == "ValueRelation":
                                rel_layer_id = cfg.config().get("Layer")
                                key_field = cfg.config().get("Key")
                                value_field = cfg.config().get("Value")
                                rel_layer = QgsProject.instance().mapLayer(rel_layer_id)
                                if rel_layer:
                                    for f in rel_layer.getFeatures():
                                        if str(f[key_field]) == str(value):
                                            return str(f[value_field])
                            return str(value)

                        #  Sections du rapport - À modifier pour un autre rapport
                        sections = {
                            "Identification": ["site", "Date", "Heure", "ID_Proj"],
                            "Localisation": [
                                "site", "zgie", "region", "Munic", "mrc", "Respo",
                                "Milieu", "Repere", "Contrainte"
                            ],
                            "Observations": [
                                "categorie", "EEE_Type", "lat_flore", "autre_sp",
                                "autre_nom_latin", "Superf_m2", "StadeDev",
                                "site_autre_stade", "site_stade_1", "site_stade_2",
                                "site_stade_3", "site_stade_4", "site_stade_5",
                                "cause_probag", "hote"
                            ],
                            "Traitement": [
                                "Trt_av", "Trt_avQui", "Trt_avType", "TraitRecom"
                            ],
                            "Commentaires et photos": ["EEE_Comment", "photo1"]
                        }

                        #  Contenu de la page 
                        for titre, liste_champs in sections.items():
                            story.append(Paragraph(titre, styles["Heading2"]))
                            contenu = []
                            for champ in liste_champs:
                                if champ in champs:
                                    if champ in layer_form.fields().names():
                                        alias = layer_form.fields().field(champ).alias() or champ
                                        valeur = get_display_value(layer_form, feat, champ)
                                    elif champ in feat_evt.fields().names():
                                        alias = feat_evt.fields().field(champ).alias() or champ
                                        valeur = get_evt_display_value(champ)
                                    else:
                                        continue
                                    if valeur not in ("", "NULL", "Null"):
                                        if "photo" in champ.lower():
                                            # Stocker l'image à insérer plus tard
                                            rel_path = valeur.replace("/", os.sep).replace("\\", os.sep).lstrip(os.sep)
                                            if rel_path.upper().startswith("DCIM" + os.sep.upper()):
                                                rel_path = rel_path[len("DCIM" + os.sep):]
                                            photo_path = os.path.normpath(os.path.join(photo_root, rel_path))
                                            contenu.append(("photo", alias, photo_path))
                                        else:
                                            contenu.append(("texte", alias, valeur))

                            if contenu:
                                for typ, alias, valeur in contenu:
                                    if typ == "texte":
                                        story.append(Paragraph(f"<b>{alias}</b> : {valeur}", styles["BodyText"]))
                                    elif typ == "photo":
                                        if os.path.exists(valeur):
                                            story.append(Spacer(1, 10))
                                            img = Image(valeur)
                                            img._restrictSize(A4[0] - 100, 300)
                                            story.append(img)
                                            story.append(Spacer(1, 10))
                                        else:
                                            story.append(Paragraph(f"<b>{alias}</b> : [Fichier introuvable : {valeur}]", styles["Italic"]))
                            else:
                                story.append(Paragraph("(Aucun champ sélectionné pour cette section)", styles["Italic"]))
                            story.append(Spacer(1, 15))

                        #  Page suivante sauf après la dernière 
                        if idx < len(feats_form) - 1:
                            story.append(PageBreak())

                    #  Génération finale 
                    doc.build(story)
                    print("Rapport généré :", file_path)
