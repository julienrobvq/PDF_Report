# rapports/base.py

from qgis.PyQt.QtWidgets import *
from qgis.core import QgsProject, QgsExpression
from PyQt5.QtCore import QDate, QTime, QDateTime

class BaseRapportDialog(QDialog):

    def __init__(self, layer_form_name, champs_affiches, parent=None):
        super().__init__(parent)
        
        self.layer_form_name = layer_form_name
        self.champs_affiches = champs_affiches

        #  Interface de base
        self.setWindowTitle("Outil de création de rapport")
        self.resize(380, 100)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sélectionnez un projet :"))
        self.proj_combo = QComboBox()
        layout.addWidget(self.proj_combo)

        # Bouton OK
        self.btn_ok = QPushButton("Générer le rapport")
        layout.addWidget(self.btn_ok)
        self.btn_ok.clicked.connect(self.accept)

        #  Couches QGIS
        self.layer_form_name = layer_form_name
        layers_form = QgsProject.instance().mapLayersByName(self.layer_form_name)
        if not layers_form:
            QMessageBox.critical(self, "Erreur", "Couche introuvable.")
            self._init_ok = False
            return
        
        self._init_ok = True
        self.layer_form = layers_form[0]

        # Evenement
        layers_evt = QgsProject.instance().mapLayersByName("Evenement")
        if not layers_evt:
            QMessageBox.critical(self, "Erreur", "Couche 'Evenement introuvable.")
            self.reject(); return

        self.layer_evt = layers_evt[0]
        self.id_field_proj = "ID_Proj"
        self.remplir_projets()
    
    def export_word(self, file_path):
        raise NotImplementedError("Erreur de génération de rapport")

    # Liste des projets
    def remplir_projets(self):
        field = self.layer_evt.fields().field(self.id_field_proj)
        cfg = field.editorWidgetSetup()

        projets_dict = {}

        for f in self.layer_evt.getFeatures():
            raw_value = f[self.id_field_proj]
            if raw_value in (None, "", " "):
                continue

            display_value = raw_value

            # ValueMap
            if cfg.type() == "ValueMap":
                mapping = cfg.config().get("map", {})
                display_value = mapping.get(str(raw_value), raw_value)

            # ValueRelation
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

    # Section rapports
    def get_selection(self):
        id_proj = self.proj_combo.currentData()
        return id_proj

    
    def get_display_value(self, layer, feature, field_name):
        return self._get_display_value_core(layer, feature, field_name)

    def get_evt_display_value(self, feat_evt, field_name):
        return self._get_display_value_core(self.layer_evt, feat_evt, field_name)

    # Génération du rapport 
    def _get_display_value_core(self, layer, feature, field_name):
        field = layer.fields().field(field_name)
        cfg = field.editorWidgetSetup()
        value = feature.attribute(field_name)
        
        # --- Choix multiples ---
        if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
            raw = value[1:-1]
            items, current, in_quotes = [], "", False

            for c in raw:
                if c == '"':
                    in_quotes = not in_quotes
                elif c == "," and not in_quotes:
                    items.append(current.strip().strip('"'))
                    current = ""
                else:
                    current += c

            if current:
                items.append(current.strip().strip('"'))

            valeurs_affichees = []

            if cfg.type() == "ValueMap":
                raw_map = cfg.config().get("map", {})

                for v in items:
                    val_aff = v

                    if isinstance(raw_map, dict):
                        val_aff = raw_map.get(v, v)

                    elif isinstance(raw_map, list):
                        for item in raw_map:
                            if isinstance(item, dict):
                                for k, lbl in item.items():
                                    if str(k) == str(v):
                                        val_aff = str(lbl)

                    valeurs_affichees.append(val_aff)

            elif cfg.type() == "ValueRelation":
                rel_layer_id = cfg.config().get("Layer")
                key_field = cfg.config().get("Key")
                value_field = cfg.config().get("Value")
                rel_layer = QgsProject.instance().mapLayer(rel_layer_id)

                if rel_layer:
                    for v in items:
                        for f in rel_layer.getFeatures():
                            if str(f[key_field]) == str(v):
                                valeurs_affichees.append(str(f[value_field]))
                                break
            else:
                valeurs_affichees = items

            return ", ".join(valeurs_affichees)

        # --- Dates / heures ---
        if isinstance(value, QDateTime):
            return value.toString("yyyy-MM-dd HH:mm")
        if isinstance(value, QTime):
            return value.toString("HH:mm")
        if isinstance(value, QDate):
            return value.toString("yyyy-MM-dd")

        try:
            inner = value.toPyObject() if hasattr(value, "toPyObject") else value
            if isinstance(inner, QDateTime):
                return inner.toString("yyyy-MM-dd HH:mm")
            if isinstance(inner, QTime):
                return inner.toString("HH:mm")
            if isinstance(inner, QDate):
                return inner.toString("yyyy-MM-dd")
        except:
            pass

        if value in (None, ""):
            return ""

        # --- ValueMap ---
        if cfg.type() == "ValueMap":
            raw_map = cfg.config().get("map", {})

            # Cas 1 : ValueMap stocké sous forme de dict
            if isinstance(raw_map, dict):
                return raw_map.get(str(value), str(value))

            # Cas 2 : ValueMap stocké sous forme de liste
            elif isinstance(raw_map, list):
                for item in raw_map:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            if str(k) == str(value):
                                return str(v)

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

    def accept(self):
        #  Récupération des paramètres 
        id_proj = self.get_selection()

        self.current_id_proj = id_proj

        #  Extensions suggérées 
        default_name = "Rapport.docx"
        
        # Enregistrement
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Enregistrer le rapport",
            default_name
        )

        if not file_path:
            return
        if not file_path.lower().endswith(".docx"):
            file_path += ".docx"

        # Récupération des données

        layer_evt = self.layer_evt
        expr_evt = QgsExpression.createFieldEqualityExpression("ID_Proj", str(id_proj))
        layer_evt.selectByExpression(expr_evt)
        feats_evt = layer_evt.selectedFeatures()

        if not feats_evt:
            QMessageBox.warning(self, "Avertissement", f"Aucun événement trouvé pour {id_proj}.")
            return

        id_even_values = [
            f["ID_EVEN"] for f in feats_evt
            if f["ID_EVEN"] not in (None, "", " ")
        ]

        if not id_even_values:
            QMessageBox.warning(self, "Avertissement", "Aucun ID_EVEN trouvé pour ce projet.")
            return

        valeurs_str = ",".join([f"'{v}'" for v in id_even_values])
        expr_form = f'"ID_EVEN" IN ({valeurs_str})'
        self.layer_form.selectByExpression(expr_form)
        feats_form = self.layer_form.selectedFeatures()
        self.current_feats_evt = feats_evt
        self.current_feats_form = feats_form

        if not feats_form:
            QMessageBox.warning(self, "Avertissement", "Aucun enregistrement trouvé.")
            return

        self.export_word(file_path)
        super().accept()
    
    def exec_(self):
        if not getattr(self, "_init_ok", True):
            return 0
        return super().exec_()