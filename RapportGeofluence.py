# -*- coding: utf-8 -*-
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from .dialogs.rapport_eee_site_dialog import RapportEEEDialog
from .dialogs.rapport_actdetection_dialog import RapportActDetectionDialog

class RapportGeofluence:

    def __init__(self, iface):
        self.iface = iface
        self.actions = []

    def initGui(self):
        
        # Action du rapport EEE
        
        self.action_eee = QAction(QIcon(), "Rapport EEE", self.iface.mainWindow())
        self.action_eee.triggered.connect(self.run_eee)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_eee)
        self.actions.append(self.action_eee)

        # Rapport Activité de détection

        self.action_act = QAction("Rapport Activité de détection")
        self.action_act.triggered.connect(self.run_actdetection)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_act)

    def unload(self):
        for a in self.actions:
            self.iface.removePluginMenu("&Rapports Géofluence", a)

    def run_eee(self):
        dlg = RapportEEEDialog()
        dlg.exec_()

    def run_actdetection(self):
        dlg = RapportActDetectionDialog()
        dlg.exec_()