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
        MainWindow.resize(882, 823)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.twd_windows = QTabWidget(self.centralwidget)
        self.twd_windows.setObjectName(u"twd_windows")
        self.twd_windows.setStyleSheet(u"")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 220))
        self.groupBox.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rbt_default = QRadioButton(self.groupBox)
        self.rbt_default.setObjectName(u"rbt_default")
        self.rbt_default.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.rbt_default.setChecked(True)

        self.horizontalLayout_4.addWidget(self.rbt_default)

        self.rbt_insert = QRadioButton(self.groupBox)
        self.rbt_insert.setObjectName(u"rbt_insert")
        self.rbt_insert.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.rbt_insert)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gbx_cvset = QGroupBox(self.tab_5)
        self.gbx_cvset.setObjectName(u"gbx_cvset")
        self.gbx_cvset.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayout_6 = QHBoxLayout(self.gbx_cvset)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbl_15 = QLabel(self.gbx_cvset)
        self.lbl_15.setObjectName(u"lbl_15")
        self.lbl_15.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_15, 2, 0, 1, 1)

        self.lbl_21 = QLabel(self.gbx_cvset)
        self.lbl_21.setObjectName(u"lbl_21")
        self.lbl_21.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_21, 0, 0, 1, 1)

        self.lbl_18 = QLabel(self.gbx_cvset)
        self.lbl_18.setObjectName(u"lbl_18")
        self.lbl_18.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_18, 4, 0, 1, 1)

        self.lbl_20 = QLabel(self.gbx_cvset)
        self.lbl_20.setObjectName(u"lbl_20")
        self.lbl_20.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_20, 6, 0, 1, 1)

        self.lbl_17 = QLabel(self.gbx_cvset)
        self.lbl_17.setObjectName(u"lbl_17")
        self.lbl_17.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_17, 3, 0, 1, 1)

        self.lbl_29 = QLabel(self.gbx_cvset)
        self.lbl_29.setObjectName(u"lbl_29")
        self.lbl_29.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_29, 0, 1, 1, 1)

        self.lbl_22 = QLabel(self.gbx_cvset)
        self.lbl_22.setObjectName(u"lbl_22")
        self.lbl_22.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_22, 1, 0, 1, 1)

        self.lbl_30 = QLabel(self.gbx_cvset)
        self.lbl_30.setObjectName(u"lbl_30")
        self.lbl_30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_30, 1, 1, 1, 1)

        self.lbl_19 = QLabel(self.gbx_cvset)
        self.lbl_19.setObjectName(u"lbl_19")
        self.lbl_19.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_19, 5, 0, 1, 1)

        self.lbl_23 = QLabel(self.gbx_cvset)
        self.lbl_23.setObjectName(u"lbl_23")
        self.lbl_23.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.lbl_23, 2, 1, 1, 1)

        self.lbl_25 = QLabel(self.gbx_cvset)
        self.lbl_25.setObjectName(u"lbl_25")
        self.lbl_25.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.lbl_25, 3, 1, 1, 1)

        self.lbl_26 = QLabel(self.gbx_cvset)
        self.lbl_26.setObjectName(u"lbl_26")
        self.lbl_26.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.lbl_26, 4, 1, 1, 1)

        self.lbl_27 = QLabel(self.gbx_cvset)
        self.lbl_27.setObjectName(u"lbl_27")
        self.lbl_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_27, 5, 1, 1, 1)

        self.lbl_28 = QLabel(self.gbx_cvset)
        self.lbl_28.setObjectName(u"lbl_28")
        self.lbl_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.lbl_28, 6, 1, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_7)


        self.horizontalLayout_2.addWidget(self.gbx_cvset)

        self.gbx_beamset = QGroupBox(self.tab_5)
        self.gbx_beamset.setObjectName(u"gbx_beamset")
        self.gbx_beamset.setEnabled(False)
        self.gbx_beamset.setMaximumSize(QSize(16777215, 16777215))
        self.gbx_beamset.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.gridLayout_4 = QGridLayout(self.gbx_beamset)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cbx_material = QComboBox(self.gbx_beamset)
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.addItem("")
        self.cbx_material.setObjectName(u"cbx_material")
        self.cbx_material.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.cbx_material, 0, 2, 1, 1)

        self.lbl_36 = QLabel(self.gbx_beamset)
        self.lbl_36.setObjectName(u"lbl_36")
        self.lbl_36.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_36, 6, 0, 1, 1)

        self.lbl_37 = QLabel(self.gbx_beamset)
        self.lbl_37.setObjectName(u"lbl_37")
        self.lbl_37.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_37, 0, 0, 1, 1)

        self.lbl_38 = QLabel(self.gbx_beamset)
        self.lbl_38.setObjectName(u"lbl_38")
        self.lbl_38.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_38, 1, 0, 1, 1)

        self.lbl_34 = QLabel(self.gbx_beamset)
        self.lbl_34.setObjectName(u"lbl_34")
        self.lbl_34.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_34, 4, 0, 1, 1)

        self.lbl_35 = QLabel(self.gbx_beamset)
        self.lbl_35.setObjectName(u"lbl_35")
        self.lbl_35.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_35, 5, 0, 1, 1)

        self.sbx_ndiv = QSpinBox(self.gbx_beamset)
        self.sbx_ndiv.setObjectName(u"sbx_ndiv")
        self.sbx_ndiv.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.sbx_ndiv, 2, 2, 1, 1)

        self.lbl_31 = QLabel(self.gbx_beamset)
        self.lbl_31.setObjectName(u"lbl_31")
        self.lbl_31.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_31, 2, 0, 1, 1)

        self.lbl_33 = QLabel(self.gbx_beamset)
        self.lbl_33.setObjectName(u"lbl_33")
        self.lbl_33.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lbl_33, 3, 0, 1, 1)

        self.dbx_width = QDoubleSpinBox(self.gbx_beamset)
        self.dbx_width.setObjectName(u"dbx_width")
        self.dbx_width.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.dbx_width, 3, 2, 1, 1)

        self.dbx_length = QDoubleSpinBox(self.gbx_beamset)
        self.dbx_length.setObjectName(u"dbx_length")
        self.dbx_length.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.dbx_length, 5, 2, 1, 1)

        self.dbx_thickn = QDoubleSpinBox(self.gbx_beamset)
        self.dbx_thickn.setObjectName(u"dbx_thickn")
        self.dbx_thickn.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.dbx_thickn, 4, 2, 1, 1)

        self.dbx_density = QDoubleSpinBox(self.gbx_beamset)
        self.dbx_density.setObjectName(u"dbx_density")
        self.dbx_density.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.dbx_density, 6, 2, 1, 1)

        self.dbx_elastic = QDoubleSpinBox(self.gbx_beamset)
        self.dbx_elastic.setObjectName(u"dbx_elastic")
        self.dbx_elastic.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.dbx_elastic, 1, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.gbx_beamset)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.btn_set = QPushButton(self.tab_5)
        self.btn_set.setObjectName(u"btn_set")
        self.btn_set.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.btn_set)

        self.twd_windows.addTab(self.tab_5, "")
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
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gbx_realtime = QGroupBox(self.tab_3)
        self.gbx_realtime.setObjectName(u"gbx_realtime")
        self.gbx_realtime.setMinimumSize(QSize(0, 0))
        self.gbx_realtime.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.gridLayout_9 = QGridLayout(self.gbx_realtime)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.wdg_forcert = QWidget(self.gbx_realtime)
        self.wdg_forcert.setObjectName(u"wdg_forcert")
        self.wdg_forcert.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.wdg_forcert, 0, 0, 1, 1)

        self.wdg_accert = QWidget(self.gbx_realtime)
        self.wdg_accert.setObjectName(u"wdg_accert")
        self.wdg_accert.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.wdg_accert, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.gbx_realtime)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gbx_dtypert = QGroupBox(self.tab_3)
        self.gbx_dtypert.setObjectName(u"gbx_dtypert")
        self.gbx_dtypert.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayout_5 = QHBoxLayout(self.gbx_dtypert)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rbt_pulsert = QRadioButton(self.gbx_dtypert)
        self.rbt_pulsert.setObjectName(u"rbt_pulsert")
        self.rbt_pulsert.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.rbt_pulsert.setChecked(True)

        self.horizontalLayout_5.addWidget(self.rbt_pulsert)

        self.rbt_hforcert = QRadioButton(self.gbx_dtypert)
        self.rbt_hforcert.setObjectName(u"rbt_hforcert")
        self.rbt_hforcert.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_5.addWidget(self.rbt_hforcert)


        self.horizontalLayout_8.addWidget(self.gbx_dtypert)

        self.gbx_posrt = QGroupBox(self.tab_3)
        self.gbx_posrt.setObjectName(u"gbx_posrt")
        self.gbx_posrt.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.formLayout_2 = QFormLayout(self.gbx_posrt)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_10 = QLabel(self.gbx_posrt)
        self.lbl_10.setObjectName(u"lbl_10")
        self.lbl_10.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_10)

        self.sbx_aposrt = QSpinBox(self.gbx_posrt)
        self.sbx_aposrt.setObjectName(u"sbx_aposrt")
        self.sbx_aposrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sbx_aposrt)

        self.lbl_9 = QLabel(self.gbx_posrt)
        self.lbl_9.setObjectName(u"lbl_9")
        self.lbl_9.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_9)

        self.sbx_rposrt = QSpinBox(self.gbx_posrt)
        self.sbx_rposrt.setObjectName(u"sbx_rposrt")
        self.sbx_rposrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sbx_rposrt)


        self.horizontalLayout_8.addWidget(self.gbx_posrt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gbx_tspeed = QGroupBox(self.tab_3)
        self.gbx_tspeed.setObjectName(u"gbx_tspeed")
        self.gbx_tspeed.setEnabled(True)
        self.gbx_tspeed.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.gridLayout_3 = QGridLayout(self.gbx_tspeed)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.gbx_tspeed)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rbt_normalrt = QRadioButton(self.frame)
        self.rbt_normalrt.setObjectName(u"rbt_normalrt")
        self.rbt_normalrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.rbt_normalrt.setChecked(True)

        self.verticalLayout_3.addWidget(self.rbt_normalrt)

        self.rbt_smotionrt = QRadioButton(self.frame)
        self.rbt_smotionrt.setObjectName(u"rbt_smotionrt")
        self.rbt_smotionrt.setEnabled(True)
        self.rbt_smotionrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.rbt_smotionrt)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.gbx_speedsm = QGroupBox(self.gbx_tspeed)
        self.gbx_speedsm.setObjectName(u"gbx_speedsm")
        self.gbx_speedsm.setEnabled(True)
        self.horizontalLayout_7 = QHBoxLayout(self.gbx_speedsm)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rbt_1 = QRadioButton(self.gbx_speedsm)
        self.rbt_1.setObjectName(u"rbt_1")
        self.rbt_1.setEnabled(True)
        self.rbt_1.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.rbt_1)

        self.rbt_01 = QRadioButton(self.gbx_speedsm)
        self.rbt_01.setObjectName(u"rbt_01")
        self.rbt_01.setEnabled(True)
        self.rbt_01.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout.addWidget(self.rbt_01)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.rbt_001 = QRadioButton(self.gbx_speedsm)
        self.rbt_001.setObjectName(u"rbt_001")
        self.rbt_001.setEnabled(True)
        self.rbt_001.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_9.addWidget(self.rbt_001)

        self.rbt_0001 = QRadioButton(self.gbx_speedsm)
        self.rbt_0001.setObjectName(u"rbt_0001")
        self.rbt_0001.setEnabled(True)
        self.rbt_0001.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_9.addWidget(self.rbt_0001)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)


        self.gridLayout_3.addWidget(self.gbx_speedsm, 0, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.gbx_tspeed)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_startrt = QPushButton(self.groupBox_2)
        self.btn_startrt.setObjectName(u"btn_startrt")
        self.btn_startrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.btn_startrt)

        self.btn_stoprt = QPushButton(self.groupBox_2)
        self.btn_stoprt.setObjectName(u"btn_stoprt")
        self.btn_stoprt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.btn_stoprt)

        self.btn_resetrt = QPushButton(self.groupBox_2)
        self.btn_resetrt.setObjectName(u"btn_resetrt")
        self.btn_resetrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.btn_resetrt)


        self.horizontalLayout_9.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_freqrt = QLabel(self.tab_3)
        self.lbl_freqrt.setObjectName(u"lbl_freqrt")
        self.lbl_freqrt.setEnabled(False)
        self.lbl_freqrt.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout.addWidget(self.lbl_freqrt, 1, 2, 1, 1)

        self.lbl_11 = QLabel(self.tab_3)
        self.lbl_11.setObjectName(u"lbl_11")
        self.lbl_11.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_11, 0, 0, 1, 1)

        self.lbl_forcert = QLabel(self.tab_3)
        self.lbl_forcert.setObjectName(u"lbl_forcert")
        self.lbl_forcert.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_forcert, 0, 2, 1, 1)

        self.hsl_force = QSlider(self.tab_3)
        self.hsl_force.setObjectName(u"hsl_force")
        self.hsl_force.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hsl_force, 0, 1, 1, 1)

        self.hsl_freq = QSlider(self.tab_3)
        self.hsl_freq.setObjectName(u"hsl_freq")
        self.hsl_freq.setEnabled(False)
        self.hsl_freq.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hsl_freq, 1, 1, 1, 1)

        self.lbl_12 = QLabel(self.tab_3)
        self.lbl_12.setObjectName(u"lbl_12")
        self.lbl_12.setEnabled(False)
        self.lbl_12.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lbl_12, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.twd_windows.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.twd_windows.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_10 = QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser = QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_10.addWidget(self.textBrowser)

        self.twd_windows.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.twd_windows)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.rbt_default, self.rbt_insert)
        QWidget.setTabOrder(self.rbt_insert, self.cbx_material)
        QWidget.setTabOrder(self.cbx_material, self.dbx_elastic)
        QWidget.setTabOrder(self.dbx_elastic, self.sbx_ndiv)
        QWidget.setTabOrder(self.sbx_ndiv, self.dbx_width)
        QWidget.setTabOrder(self.dbx_width, self.dbx_thickn)
        QWidget.setTabOrder(self.dbx_thickn, self.dbx_length)
        QWidget.setTabOrder(self.dbx_length, self.dbx_density)
        QWidget.setTabOrder(self.dbx_density, self.btn_set)
        QWidget.setTabOrder(self.btn_set, self.rbt_pulseft)
        QWidget.setTabOrder(self.rbt_pulseft, self.rbt_harft)
        QWidget.setTabOrder(self.rbt_harft, self.dbx_forceft)
        QWidget.setTabOrder(self.dbx_forceft, self.box_time)
        QWidget.setTabOrder(self.box_time, self.sbx_aposft)
        QWidget.setTabOrder(self.sbx_aposft, self.sbx_rposft)
        QWidget.setTabOrder(self.sbx_rposft, self.dbx_freqft)
        QWidget.setTabOrder(self.dbx_freqft, self.btn_update)
        QWidget.setTabOrder(self.btn_update, self.rbt_pulsert)
        QWidget.setTabOrder(self.rbt_pulsert, self.rbt_hforcert)
        QWidget.setTabOrder(self.rbt_hforcert, self.sbx_aposrt)
        QWidget.setTabOrder(self.sbx_aposrt, self.sbx_rposrt)
        QWidget.setTabOrder(self.sbx_rposrt, self.rbt_1)
        QWidget.setTabOrder(self.rbt_1, self.rbt_01)
        QWidget.setTabOrder(self.rbt_01, self.hsl_force)
        QWidget.setTabOrder(self.hsl_force, self.hsl_freq)

        self.retranslateUi(MainWindow)

        self.twd_windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.rbt_default.setText(QCoreApplication.translate("MainWindow", u"Default Values", None))
        self.rbt_insert.setText(QCoreApplication.translate("MainWindow", u"Insert Values", None))
        self.gbx_cvset.setTitle(QCoreApplication.translate("MainWindow", u"Current Values", None))
        self.lbl_15.setText(QCoreApplication.translate("MainWindow", u"Number of divisions:", None))
        self.lbl_21.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.lbl_18.setText(QCoreApplication.translate("MainWindow", u"Thickness (m):", None))
        self.lbl_20.setText(QCoreApplication.translate("MainWindow", u"Density:", None))
        self.lbl_17.setText(QCoreApplication.translate("MainWindow", u"Width (m):", None))
        self.lbl_29.setText(QCoreApplication.translate("MainWindow", u"Steel", None))
        self.lbl_22.setText(QCoreApplication.translate("MainWindow", u"Elastic modulus (GPa):", None))
        self.lbl_30.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.lbl_19.setText(QCoreApplication.translate("MainWindow", u"Length (m):", None))
        self.lbl_23.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.lbl_25.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.lbl_26.setText(QCoreApplication.translate("MainWindow", u"0.00575", None))
        self.lbl_27.setText(QCoreApplication.translate("MainWindow", u"0.58", None))
        self.lbl_28.setText(QCoreApplication.translate("MainWindow", u"7900", None))
        self.gbx_beamset.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.cbx_material.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00e7o Estrutural A-36", None))
        self.cbx_material.setItemText(1, QCoreApplication.translate("MainWindow", u"A\u00e7o Inoxid\u00e1vel 304", None))
        self.cbx_material.setItemText(2, QCoreApplication.translate("MainWindow", u"A\u00e7o-ferramenta L2", None))
        self.cbx_material.setItemText(3, QCoreApplication.translate("MainWindow", u"Alum\u00ednio Forjado 2014-T6", None))
        self.cbx_material.setItemText(4, QCoreApplication.translate("MainWindow", u"Alum\u00ednio Forjado 6061-T6", None))
        self.cbx_material.setItemText(5, QCoreApplication.translate("MainWindow", u"Cobre Bronze C86100", None))
        self.cbx_material.setItemText(6, QCoreApplication.translate("MainWindow", u"Cobre Lat\u00e3o Vermelho C83400", None))
        self.cbx_material.setItemText(7, QCoreApplication.translate("MainWindow", u"Concreto Alta Resist\u00eancia", None))
        self.cbx_material.setItemText(8, QCoreApplication.translate("MainWindow", u"Concreto Baixa Resist\u00eancia", None))
        self.cbx_material.setItemText(9, QCoreApplication.translate("MainWindow", u"Ferro Fundido Cinza ASTM 20", None))
        self.cbx_material.setItemText(10, QCoreApplication.translate("MainWindow", u"Ferro Fundido Male\u00e1vel ASTM A-197", None))
        self.cbx_material.setItemText(11, QCoreApplication.translate("MainWindow", u"Madeira Estrutural Abeto Douglas", None))
        self.cbx_material.setItemText(12, QCoreApplication.translate("MainWindow", u"Madeira Estrutural Abeto Branco", None))
        self.cbx_material.setItemText(13, QCoreApplication.translate("MainWindow", u"Magn\u00e9sio Am 1004-T61", None))
        self.cbx_material.setItemText(14, QCoreApplication.translate("MainWindow", u"Pl\u00e1stico Refor\u00e7ado Keviar 49", None))
        self.cbx_material.setItemText(15, QCoreApplication.translate("MainWindow", u"Pl\u00e1stico Refor\u00e7ado 30% Vidro", None))
        self.cbx_material.setItemText(16, QCoreApplication.translate("MainWindow", u"Tit\u00e2nio Ti-6A1-4V", None))

        self.lbl_36.setText(QCoreApplication.translate("MainWindow", u"Density:", None))
        self.lbl_37.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.lbl_38.setText(QCoreApplication.translate("MainWindow", u"Elastic modulus (GPa):", None))
        self.lbl_34.setText(QCoreApplication.translate("MainWindow", u"Thickness (m):", None))
        self.lbl_35.setText(QCoreApplication.translate("MainWindow", u"Length (m):", None))
        self.lbl_31.setText(QCoreApplication.translate("MainWindow", u"Number of divisions:", None))
        self.lbl_33.setText(QCoreApplication.translate("MainWindow", u"Width (m):", None))
        self.btn_set.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Beam Settings", None))
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
        self.gbx_chart.setTitle(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Fixed Time", None))
        self.gbx_realtime.setTitle(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.gbx_dtypert.setTitle(QCoreApplication.translate("MainWindow", u"Disturbance Type", None))
        self.rbt_pulsert.setText(QCoreApplication.translate("MainWindow", u"Single Pulse", None))
        self.rbt_hforcert.setText(QCoreApplication.translate("MainWindow", u"Harmonic Force", None))
        self.gbx_posrt.setTitle(QCoreApplication.translate("MainWindow", u"Positions", None))
        self.lbl_10.setText(QCoreApplication.translate("MainWindow", u"Apply:", None))
        self.lbl_9.setText(QCoreApplication.translate("MainWindow", u"Read:", None))
        self.gbx_tspeed.setTitle(QCoreApplication.translate("MainWindow", u"Time Speed", None))
        self.rbt_normalrt.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.rbt_smotionrt.setText(QCoreApplication.translate("MainWindow", u"Slow Motion", None))
        self.gbx_speedsm.setTitle(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.rbt_1.setText(QCoreApplication.translate("MainWindow", u"x0,1", None))
        self.rbt_01.setText(QCoreApplication.translate("MainWindow", u"x0,01", None))
        self.rbt_001.setText(QCoreApplication.translate("MainWindow", u"x0,001", None))
        self.rbt_0001.setText(QCoreApplication.translate("MainWindow", u"x0,0001", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.btn_startrt.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.btn_stoprt.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.btn_resetrt.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.lbl_freqrt.setText(QCoreApplication.translate("MainWindow", u"0,00", None))
        self.lbl_11.setText(QCoreApplication.translate("MainWindow", u"Force (N)", None))
        self.lbl_forcert.setText(QCoreApplication.translate("MainWindow", u"0,00", None))
        self.lbl_12.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Real Time", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"3D Simulation", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Note:</span><span style=\" font-size:10pt;\"> 'Real Time' and '3D Simulation' pages are still under development.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">References: </span><span style=\" font-size:10pt;\">Elastic Modulus Values</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">ROSA, Willian de Araujo. </span><span style=\" font-size:10pt; font-weight:600;\">Propriedades dos Materiais Utilizados em Engenharia</span><span style=\" font-size:10pt;\">. Dispon\u00edvel em: http://www.profwillian.com/materiais/propriedades.asp. Acesso em: 17 fev. 2021.</span></p>\n"
"<p style=\"-qt-paragraph-typ"
                        "e:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.twd_windows.setTabText(self.twd_windows.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

