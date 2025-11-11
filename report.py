# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QComboBox, QCheckBox, QLabel, QPushButton, QScrollArea, QWidget, QGridLayout, QMessageBox, QHBoxLayout, QLineEdit, QFileDialog
from qgis.core import QgsProject, QgsExpression
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class RapportEEE(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sélection du site et des champs")
        self.resize(380, 420)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sélectionnez un projet :"))
        self.site_combo = QComboBox()
        layout.addWidget(self.site_combo)
        
        layout.addWidget(QLabel("Titre du rapport :"))
        self.titre_rapport = QLineEdit()
        layout.addWidget(self.titre_rapport)

        layout.addWidget(QLabel("Champs à inclure :"))
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

        # Charger la couche
        layers = QgsProject.instance().mapLayersByName("Form_EEE")
        if not layers:
            QMessageBox.critical(self, "Erreur", "Couche 'Form_EEE' introuvable.")
            self.reject(); return
        self.layer = layers[0]

        self.site_field = "site"

        # Champs EEE
        self.champs_affiches = [
            "site",
            "zgie",
            "region",
            "Munic",
            "mrc",
            "Respo",
            "Milieu",
            "Repere",
            "Contrainte",
            "categorie",
            "EEE_Type",
            "lat_flore",
            "autre_sp",
            "autre_nom_latin",
            "Superf_m2",
            "StadeDev",
            "site_autre_stade",
            "site_stade_1",
            "site_stade_2",
            "site_stade_3",
            "site_stade_4",
            "site_stade_5",
            "cause_probag",
            "hote",
            "Trt_av",
            "Trt_avQui",
            "Trt_avType",
            "TraitRecom",
            "EEE_Comment",
            "photo1"
        ]

        # Evenement

        self.champs_evenement = ["Date", "Heure", "ID_Proj"]
        self.champs_affiches.extend(self.champs_evenement)

        self.remplir_sites()
        self.remplir_champs()

    def remplir_sites(self):
        valeurs = sorted({f[self.site_field] for f in self.layer.getFeatures()
                          if f[self.site_field] not in (None, "", " ")})
        self.site_combo.addItems([str(v) for v in valeurs])

    def remplir_champs(self):
        self.checkboxes = []
        for i, champ in enumerate(self.champs_affiches):
            if champ in self.layer.fields().names():
                alias = self.layer.fields().field(champ).alias() or champ
            else:
                alias = f"{champ}"
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
        site = self.site_combo.currentText()
        champs = [cb.toolTip() for cb in self.checkboxes if cb.isChecked()]
        titre = self.titre_rapport.text()
        return site, champs, titre

def get_display_value(layer, feature, field_name):
    """Retourne la valeur affichée dans QGIS pour un champ donné."""
    field = layer.fields().field(field_name)
    cfg = field.editorWidgetSetup()
    value = feature.attribute(field_name)

    if value in (None, ""):
        return ""

    # --- ValueMap ---
    if cfg.type() == "ValueMap":
        mapping = cfg.config().get("map", {})
        for k, v in mapping.items():
            if str(k) == str(value):
                return v
        return str(value)

    # --- ValueRelation ---
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

    # --- Valeur par défaut ---
    return str(value)

# --- Exécution ---
# --- Exécution ---
dlg = RapportEEE()
if dlg.exec_():
    site, champs, titre_rapport = dlg.get_selection()

    # --- Récupération des données dans QGIS ---
    layer = QgsProject.instance().mapLayersByName("Form_EEE")[0]
    expr = QgsExpression.createFieldEqualityExpression("site", site)
    layer.selectByExpression(expr)
    feats = layer.selectedFeatures()

    if not feats:
        QMessageBox.warning(None, "Avertissement", "Aucun enregistrement trouvé pour ce site.")
    else:
        feat = feats[0]  # premier enregistrement

        # --- Récupération des données associées dans la table Evenement ---
        layer_evt = QgsProject.instance().mapLayersByName("Evenement")[0]
        id_even = feat.attribute("ID_EVEN")
        feat_evt = None

        if id_even is not None:
            expr_evt = f'"ID_EVEN" = \'{id_even}\''
            layer_evt.selectByExpression(expr_evt)
            feats_evt = layer_evt.selectedFeatures()
            if feats_evt:
                feat_evt = feats_evt[0]

        # --- Fonction de récupération de la valeur affichée pour Evenement ---
        def get_evt_display_value(field_name):
            if not feat_evt:
                return ""
            field = feat_evt.fields().field(field_name)
            cfg = field.editorWidgetSetup()
            value = feat_evt.attribute(field_name)

            if value in (None, ""):
                return ""

            # Conversion pour QDate / QTime / QDateTime
            if hasattr(value, "toString"):
                type_name = type(value).__name__
                if "QDateTime" in type_name:
                    return value.toString("yyyy-MM-dd HH:mm")
                elif "QTime" in type_name:
                    return value.toString("HH:mm")
                elif "QDate" in type_name:
                    return value.toString("yyyy-MM-dd")

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

            # Valeur brute sinon
            return str(value)

        # --- Sélection du fichier de sortie ---
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Enregistrer le rapport",
            "Rapport.pdf",
            "Fichiers PDF (*.pdf)"
        )

        # Si l'utilisateur annule, on arrête
        if not file_path:
            QMessageBox.information(None, "Annulé", "Génération du rapport annulée.")
        else:
            # --- Définir les sections et champs associés ---
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

            # --- Création du PDF ---
            doc = SimpleDocTemplate(file_path, pagesize=A4)
            styles = getSampleStyleSheet()
            story = []

        story.append(Paragraph(titre_rapport, styles["Title"]))
        
        story.append(Spacer(1, 20))

        # --- Parcourir les sections et injecter les champs sélectionnés ---
        for titre, liste_champs in sections.items():
            story.append(Paragraph(titre, styles["Heading2"]))
            contenu = []

            for champ in liste_champs:
                if champ in champs:  # seulement ceux cochés
                    if champ in layer.fields().names():
                        alias = layer.fields().field(champ).alias() or champ
                        valeur = get_display_value(layer, feat, champ)
                    elif feat_evt and champ in feat_evt.fields().names():
                        alias = feat_evt.fields().field(champ).alias() or champ
                        valeur = get_evt_display_value(champ)
                    else:
                        continue

                    # Ignorer les valeurs nulles
                    if valeur not in ("", "NULL", "Null"):
                        contenu.append(f"<b>{alias}</b> : {valeur}")

            if contenu:
                story.append(Paragraph("<br/>".join(contenu), styles["BodyText"]))
            else:
                story.append(Paragraph("(Aucun champ sélectionné pour cette section)", styles["Italic"]))

            story.append(Spacer(1, 15))

        # --- Génération du PDF ---
        doc.build(story)
        print("Rapport généré avec succès.")