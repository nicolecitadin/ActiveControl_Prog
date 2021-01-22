# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.twd_windows = QTabWidget(self.centralwidget)
        self.twd_windows.setObjectName(u"twd_windows")
        self.twd_windows.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gbx_current = QGroupBox(self.tab)
        self.gbx_current.setObjectName(u"gbx_current")
        self.gbx_current.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.formLayout = QFormLayout(self.gbx_current)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_1 = QLabel(self.gbx_current)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_1)

        self.lbl_forceft = QLabel(self.gbx_current)
        self.lbl_forceft.setObjectName(u"lbl_forceft")
        self.lbl_forceft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lbl_forceft)

        self.lbl_2 = QLabel(self.gbx_current)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_2)

        self.lbl_timeft = QLabel(self.gbx_current)
        self.lbl_timeft.setObjectName(u"lbl_timeft")
        self.lbl_timeft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_timeft)

        self.lbl_3 = QLabel(self.gbx_current)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_3)

        self.lbl_aposft = QLabel(self.gbx_current)
        self.lbl_aposft.setObjectName(u"lbl_aposft")
        self.lbl_aposft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lbl_aposft)

        self.lbl_4 = QLabel(self.gbx_current)
        self.lbl_4.setObjectName(u"lbl_4")
        self.lbl_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_4)

        self.lbl_rposft = QLabel(self.gbx_current)
        self.lbl_rposft.setObjectName(u"lbl_rposft")
        self.lbl_rposft.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lbl_rposft)

        self.lbl_13 = QLabel(self.gbx_current)
        self.lbl_13.setObjectName(u"lbl_13")
        self.lbl_13.setEnabled(False)
        self.lbl_13.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_13)

        self.lbl_freqft = QLabel(self.gbx_current)
        self.lbl_freqft.setObjectName(u"lbl_freqft")
        self.lbl_freqft.setEnabled(False)
        self.lbl_freqft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lbl_freqft)


        self.horizontalLayout.addWidget(self.gbx_current)

        self.gbx_settings = QGroupBox(self.tab)
        self.gbx_settings.setObjectName(u"gbx_settings")
        self.gbx_settings.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.verticalLayout_6 = QVBoxLayout(self.gbx_settings)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_5 = QLabel(self.gbx_settings)
        self.lbl_5.setObjectName(u"lbl_5")
        self.lbl_5.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_5)

        self.lbl_6 = QLabel(self.gbx_settings)
        self.lbl_6.setObjectName(u"lbl_6")
        self.lbl_6.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_6)

        self.lbl_7 = QLabel(self.gbx_settings)
        self.lbl_7.setObjectName(u"lbl_7")
        self.lbl_7.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_7)

        self.lbl_8 = QLabel(self.gbx_settings)
        self.lbl_8.setObjectName(u"lbl_8")
        self.lbl_8.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_8)

        self.sbx_rposft = QSpinBox(self.gbx_settings)
        self.sbx_rposft.setObjectName(u"sbx_rposft")
        self.sbx_rposft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.sbx_rposft)

        self.dbx_forceft = QDoubleSpinBox(self.gbx_settings)
        self.dbx_forceft.setObjectName(u"dbx_forceft")
        self.dbx_forceft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dbx_forceft)

        self.box_time = QTimeEdit(self.gbx_settings)
        self.box_time.setObjectName(u"box_time")
        self.box_time.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.box_time)

        self.sbx_aposft = QSpinBox(self.gbx_settings)
        self.sbx_aposft.setObjectName(u"sbx_aposft")
        self.sbx_aposft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.sbx_aposft)

        self.lbl_14 = QLabel(self.gbx_settings)
        self.lbl_14.setObjectName(u"lbl_14")
        self.lbl_14.setEnabled(False)
        self.lbl_14.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.lbl_14)

        self.dbx_freqft = QDoubleSpinBox(self.gbx_settings)
        self.dbx_freqft.setObjectName(u"dbx_freqft")
        self.dbx_freqft.setEnabled(False)
        self.dbx_freqft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.dbx_freqft)


        self.verticalLayout_6.addLayout(self.formLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_update = QPushButton(self.gbx_settings)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.btn_update)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.gbx_settings)


        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.gbx_dtp = QGroupBox(self.tab)
        self.gbx_dtp.setObjectName(u"gbx_dtp")
        self.gbx_dtp.setMinimumSize(QSize(0, 100))
        self.gbx_dtp.setMaximumSize(QSize(16777215, 120))
        self.gbx_dtp.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.gridLayout_6 = QGridLayout(self.gbx_dtp)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.rbt_harft = QRadioButton(self.gbx_dtp)
        self.rbt_harft.setObjectName(u"rbt_harft")
        self.rbt_harft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_6.addWidget(self.rbt_harft, 0, 1, 1, 1)

        self.rbt_pulseft = QRadioButton(self.gbx_dtp)
        self.rbt_pulseft.setObjectName(u"rbt_pulseft")
        self.rbt_pulseft.setEnabled(True)
        self.rbt_pulseft.setMaximumSize(QSize(16777215, 16777215))
        self.rbt_pulseft.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.rbt_pulseft.setChecked(True)

        self.gridLayout_6.addWidget(self.rbt_pulseft, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.gbx_dtp, 1, 0, 1, 1)

        self.gbx_chart = QGroupBox(self.tab)
        self.gbx_chart.setObjectName(u"gbx_chart")
        self.gbx_chart.setMinimumSize(QSize(0, 0))
        self.gbx_chart.setMaximumSize(QSize(16777215, 16777215))
        self.gbx_chart.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayout_3 = QHBoxLayout(self.gbx_chart)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.wdg_forceft = QWidget(self.gbx_chart)
        self.wdg_forceft.setObjectName(u"wdg_forceft")
        self.wdg_forceft.setMinimumSize(QSize(0, 30))
        self.wdg_forceft.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.wdg_forceft)

        self.wdg_accetf = QWidget(self.gbx_chart)
        self.wdg_accetf.setObjectName(u"wdg_accetf")
        self.wdg_accetf.setMinimumSize(QSize(0, 30))
        self.wdg_accetf.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.wdg_accetf)


        self.gridLayout_5.addWidget(self.gbx_chart, 0, 0, 1, 1)

        self.twd_windows.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.hsl_pos = QSlider(self.tab_3)
        self.hsl_pos.setObjectName(u"hsl_pos")
        self.hsl_pos.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hsl_pos, 0, 1, 1, 1)

        self.lbl_12 = QLabel(self.tab_3)
        self.lbl_12.setObjectName(u"lbl_12")
        self.lbl_12.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_12, 1, 0, 1, 1)

        self.lbl_forcertime = QLabel(self.tab_3)
        self.lbl_forcertime.setObjectName(u"lbl_forcertime")
        self.lbl_forcertime.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout.addWidget(self.lbl_forcertime, 1, 2, 1, 1)

        self.hsl_force = QSlider(self.tab_3)
        self.hsl_force.setObjectName(u"hsl_force")
        self.hsl_force.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hsl_force, 1, 1, 1, 1)

        self.lbl_posrtime = QLabel(self.tab_3)
        self.lbl_posrtime.setObjectName(u"lbl_posrtime")
        self.lbl_posrtime.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_posrtime, 0, 2, 1, 1)

        self.lbl_11 = QLabel(self.tab_3)
        self.lbl_11.setObjectName(u"lbl_11")
        self.lbl_11.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_11, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 4, 0, 1, 1)

        self.gbx_posrt = QGroupBox(self.tab_3)
        self.gbx_posrt.setObjectName(u"gbx_posrt")
        self.gbx_posrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.gridLayout_4 = QGridLayout(self.gbx_posrt)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_9 = QLabel(self.gbx_posrt)
        self.lbl_9.setObjectName(u"lbl_9")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_9)

        self.sbx_aposrt = QSpinBox(self.gbx_posrt)
        self.sbx_aposrt.setObjectName(u"sbx_aposrt")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sbx_aposrt)


        self.gridLayout_4.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lbl_10 = QLabel(self.gbx_posrt)
        self.lbl_10.setObjectName(u"lbl_10")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_10)

        self.sbx_rposrt = QSpinBox(self.gbx_posrt)
        self.sbx_rposrt.setObjectName(u"sbx_rposrt")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.sbx_rposrt)


        self.gridLayout_4.addLayout(self.formLayout_4, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.gbx_posrt, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gbx_realtime = QGroupBox(self.tab_3)
        self.gbx_realtime.setObjectName(u"gbx_realtime")
        self.gbx_realtime.setMinimumSize(QSize(0, 95))
        self.gbx_realtime.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.gridLayout_2 = QGridLayout(self.gbx_realtime)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.wdg_chartr = QWidget(self.gbx_realtime)
        self.wdg_chartr.setObjectName(u"wdg_chartr")
        self.wdg_chartr.setMinimumSize(QSize(0, 180))
        self.wdg_chartr.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.wdg_chartr, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbx_realtime, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.twd_windows.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.twd_windows.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.twd_windows.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.twd_windows)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.twd_windows, self.rbt_pulseft)
        QWidget.setTabOrder(self.rbt_pulseft, self.rbt_harft)
        QWidget.setTabOrder(self.rbt_harft, self.dbx_forceft)
        QWidget.setTabOrder(self.dbx_forceft, self.box_time)
        QWidget.setTabOrder(self.box_time, self.sbx_aposft)
        QWidget.setTabOrder(self.sbx_aposft, self.sbx_rposft)
        QWidget.setTabOrder(self.sbx_rposft, self.dbx_freqft)
        QWidget.setTabOrder(self.dbx_freqft, self.btn_update)
        QWidget.setTabOrder(self.btn_update, self.sbx_rposrt)
        QWidget.setTabOrder(self.sbx_rposrt, self.hsl_pos)
        QWidget.setTabOrder(self.hsl_pos, self.hsl_force)
        QWidget.setTabOrder(self.hsl_force, self.sbx_aposrt)

        self.retranslateUi(MainWindow)

        self.twd_windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gbx_current.setTitle(QCoreApplication.translate("MainWindow", u"Current Values", None))
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"Force (N):", None))
        self.lbl_forceft.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lbl_2.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.lbl_timeft.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.lbl_3.setText(QCoreApplication.translate("MainWindow", u"Application Position:", None))
        self.lbl_aposft.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_4.setText(QCoreApplication.translate("MainWindow", u"Reading Position:", None))
        self.lbl_rposft.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_13.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz):", None))
        self.lbl_freqft.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.gbx_settings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lbl_5.setText(QCoreApplication.translate("MainWindow", u"Force (N):", None))
        self.lbl_6.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.lbl_7.setText(QCoreApplication.translate("MainWindow", u"Application Position:", None))
        self.lbl_8.setText(QCoreApplication.translate("MainWindow", u"Reading Position:", None))
        self.lbl_14.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.gbx_dtp.setTitle(QCoreApplication.translate("MainWindow", u"Disturbance Type", None))
        self.rbt_harft.setText(QCoreApplication.translate("MainWindow", u"Harmonic Force", None))
        self.rbt_pulseft.setText(QCoreApplication.translate("MainWindow", u"Single Pulse", None))
        self.gbx_chart.setTitle(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Fixed Time", None))
        self.lbl_12.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.lbl_forcertime.setText(QCoreApplication.translate("MainWindow", u"0,00", None))
        self.lbl_posrtime.setText(QCoreApplication.translate("MainWindow", u"0,00", None))
        self.lbl_11.setText(QCoreApplication.translate("MainWindow", u"Force (N)", None))
        self.gbx_posrt.setTitle(QCoreApplication.translate("MainWindow", u"Positions", None))
        self.lbl_9.setText(QCoreApplication.translate("MainWindow", u"Apply:", None))
        self.lbl_10.setText(QCoreApplication.translate("MainWindow", u"Read:", None))
        self.gbx_realtime.setTitle(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Real Time", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"3D Simulation", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

