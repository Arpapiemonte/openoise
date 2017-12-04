# -*- coding: utf-8 -*-
"""
/***************************************************************************
 opeNoise

 Qgis Plugin to compute noise levels

                             -------------------
        begin                : March 2014
        copyright            : (C) 2014 by Arpa Piemonte
        email                : s.masera@arpa.piemonte.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
import os,shutil, sys

# Set up current path, so that we know where to look for mudules
currentPath = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/tools'))

import do_CreateReceiverPoints,do_CalculateNoiseLevels,do_AssignLevelsToBuildings,do_ApplyNoiseSymbology,do_Credits

class opeNoise:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'opeNoise_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        
    def initGui(self):
        
        # opeNoise         
        self.opeNoise_menu = QMenu(QCoreApplication.translate("opeNoise", "&opeNoise"))
        self.opeNoise_menu.setIcon(QIcon(":/plugins/opeNoise/icons/icon_opeNoise.png"))

        # CreateReceiverPoints
        self.CreateReceiverPoints_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_CreateReceiverPoints.png"),
                                        QCoreApplication.translate("opeNoise", "Create Receiver Points"), self.iface.mainWindow())
        self.CreateReceiverPoints_item.triggered.connect(self.CreateReceiverPoints_show)

        # CalculateNoiseLevels
        self.CalculateNoiseLevels_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_CalculateNoiseLevels.png"),
                                        QCoreApplication.translate("opeNoise", "Calculate Noise Levels"), self.iface.mainWindow())
        self.CalculateNoiseLevels_item.triggered.connect(self.CalculateNoiseLevels_show)

        # AssignLevelsToBuildings
        self.AssignLevelsToBuildings_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_AssignLevelsToBuildings.png"),
                                        QCoreApplication.translate("opeNoise", "Assign Levels To Buildings"), self.iface.mainWindow())
        self.AssignLevelsToBuildings_item.triggered.connect(self.AssignLevelsToBuildings_show)
        
        # AssignLevelsToBuildings
        self.ApplyNoiseSymbology_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_ApplyNoiseSymbology.png"),
                                        QCoreApplication.translate("opeNoise", "Apply Noise Symbology"), self.iface.mainWindow())
        self.ApplyNoiseSymbology_item.triggered.connect(self.ApplyNoiseSymbology_show)
        
        # Information
#        self.Informations_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_Informations.png"),
#                                        QCoreApplication.translate("opeNoise", "Informations"), self.iface.mainWindow())
#        self.Informations_item.triggered.connect(self.Informations_show)  

        # Credits
        self.Credits_item = QAction(QIcon(":/plugins/opeNoise/icons/icon_Informations.png"),
                                        QCoreApplication.translate("opeNoise", "Credits"), self.iface.mainWindow())
        self.Credits_item.triggered.connect(self.Credits_show)  
        
        # add items
        self.opeNoise_menu.addActions([self.CreateReceiverPoints_item, 
                                       self.CalculateNoiseLevels_item,
                                       self.AssignLevelsToBuildings_item, 
                                       self.ApplyNoiseSymbology_item, 
#                                       self.Informations_item,
                                       self.Credits_item])
        
        self.menu = self.iface.pluginMenu()
        self.menu.addMenu( self.opeNoise_menu )       
            
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&opeNoise", self.CreateReceiverPoints_item)
        self.iface.removePluginMenu("&opeNoise", self.CalculateNoiseLevels_item)
        self.iface.removePluginMenu("&opeNoise", self.AssignLevelsToBuildings_item)     
        self.iface.removePluginMenu("&opeNoise", self.ApplyNoiseSymbology_item)     
#        self.iface.removePluginMenu("&opeNoise", self.Informations_item)
        self.iface.removePluginMenu("&opeNoise", self.Credits_item)
        
    def CreateReceiverPoints_show(self):
    
        d = do_CreateReceiverPoints.Dialog(self.iface)
        d.setWindowModality(Qt.ApplicationModal)
        d.setFixedSize(d.size())
        d.show()
        d.exec_()    

       
    def AssignLevelsToBuildings_show(self):

        d = do_AssignLevelsToBuildings.Dialog(self.iface)
        d.setWindowModality(Qt.ApplicationModal)
        d.setFixedSize(d.size())
        d.show()
        d.exec_()   

    def CalculateNoiseLevels_show(self):

        d = do_CalculateNoiseLevels.Dialog(self.iface)
        d.setWindowModality(Qt.ApplicationModal)
        d.setFixedSize(d.size())
        d.show()
        d.exec_()   

    def ApplyNoiseSymbology_show(self):

        d = do_ApplyNoiseSymbology.Dialog(self.iface)
        d.setWindowModality(Qt.ApplicationModal)
        d.setFixedSize(d.size())
        d.show()
        d.exec_()   
    
#    def Informations_show(self):
#
#        currentPath = os.path.dirname(__file__)
#        temp_dir = os.path.abspath(os.path.join(currentPath + os.sep + 'informations' + os.sep + 'OpeNoise_info.pdf'))
#
#        import webbrowser
#        webbrowser.open_new('file:' + temp_dir)
        
    def Credits_show(self):

        d = do_Credits.Dialog_info(self.iface)
        d.setWindowModality(Qt.ApplicationModal)
        d.setFixedSize(d.size())
        d.show()
        d.exec_()  
