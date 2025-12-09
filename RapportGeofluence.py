# -*- coding: utf-8 -*-
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from .dialogs.rapport_eee_site_dialog import RapportEEEDialog
from .dialogs.rapport_actdetection_dialog import RapportActDetectionDialog
from .dialogs.rapport_physicochimie_dialog import RapportPhysicochimieDialog
from .dialogs.rapport_mhh_dialog import RapportMHH

class RapportGeofluence:

    def __init__(self, iface):
        self.iface = iface
        self.actions = []

    def initGui(self):

        # Rapport EEE
        self.action_eee = QAction(QIcon(), "Rapport Espèces exotiques envahissantes", self.iface.mainWindow())
        self.action_eee.triggered.connect(self.run_eee)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_eee)
        self.actions.append(self.action_eee)

        # Rapport Activité de détection
        self.action_act = QAction(QIcon(), "Rapport Activité de détection", self.iface.mainWindow())
        self.action_act.triggered.connect(self.run_actdetection)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_act)
        self.actions.append(self.action_act)

        # Rapport Physicochimie
        self.action_physico = QAction(QIcon(), "Rapport Physicochimie", self.iface.mainWindow())
        self.action_physico.triggered.connect(self.run_physicochimie)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_physico)
        self.actions.append(self.action_physico)

        # Rapport Milieux humides
        self.action_mhh = QAction(QIcon(), "Rapport Milieux humides", self.iface.mainWindow())
        self.action_mhh.triggered.connect(self.run_mhh)
        self.iface.addPluginToMenu("&Rapports Géofluence", self.action_mhh)
        self.actions.append(self.action_mhh)        


    def unload(self):
        for a in self.actions:
            self.iface.removePluginMenu("&Rapports Géofluence", a)

    def run_eee(self):
        dlg = RapportEEEDialog()
        dlg.exec_()

    def run_actdetection(self):
        dlg = RapportActDetectionDialog()
        dlg.exec_()

    def run_physicochimie(self):
        dlg = RapportPhysicochimieDialog()
        dlg.exec_()

    def run_mhh(self):
        dlg = RapportMHH()
        dlg.exec_()