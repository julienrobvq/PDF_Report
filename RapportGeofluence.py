# -*- coding: utf-8 -*-
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from .rapports.mhh import RapportMHH
from .rapports.isa import RapportISA
from qgis.core import QgsProject

class RapportGeofluence:

    def __init__(self, iface):
        self.iface = iface
        self.actions = []
    
    def has_layers(self,layer_names):
        project = QgsProject.instance()
        return all(project.mapLayersByName(name) for name in layer_names)
    
    def initGui(self):

        # Rapport Milieux humides
        if self.has_layers(["Form_MHH"]):    
            self.action_mhh = QAction(QIcon(), "Rapport Milieux humides", self.iface.mainWindow())
            self.action_mhh.triggered.connect(self.run_mhh)
            self.iface.addPluginToMenu("&Rapports Géofluence", self.action_mhh)
            self.actions.append(self.action_mhh)

        # Rapport ISA
        if self.has_layers(["Form_ISA_Propriete", "Form_ISA_Puits", "Form_ISA_Fosse", "Form_ISA_Epurateur"]):
            self.action_isa = QAction(QIcon(), "Lettre Installation septique autonome", self.iface.mainWindow())
            self.action_isa.triggered.connect(self.run_isa)
            self.iface.addPluginToMenu("&Rapports Géofluence", self.action_isa)
            self.actions.append(self.action_isa)


    def unload(self):
        for a in self.actions:
            self.iface.removePluginMenu("&Rapports Géofluence", a)

    def run_mhh(self):
        dlg = RapportMHH()
        dlg.exec_()

    def run_isa(self):
        dlg = RapportISA()
        dlg.exec_()