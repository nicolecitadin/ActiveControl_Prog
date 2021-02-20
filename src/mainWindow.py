import numpy as np
import pyqtgraph as pg
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QVBoxLayout
from src.ui.mainWindow2_ui import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from cantileverBeam import CantileverBeam


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Input Boxes Settings
        self.ui.gbx_speedsm.setDisabled(True)
        self.ui.dbx_elastic.setMaximum(100000)
        self.ui.sbx_ndiv.setMaximum(1000)
        self.ui.dbx_width.setMaximum(1000)
        self.ui.dbx_length.setMaximum(100000)
        self.ui.dbx_density.setMaximum(1000000)
        self.ui.dbx_elastic.setDecimals(3)
        self.ui.dbx_width.setDecimals(3)
        self.ui.dbx_thickn.setDecimals(6)
        self.ui.dbx_length.setDecimals(3)
        self.ui.dbx_density.setDecimals(3)
        self.ui.box_time.setDisplayFormat("mm:ss")
        self.ui.hsl_force.setMaximum(500)
        self.ui.hsl_freq.setMaximum(1000)
        self.ui.dbx_elastic.setValue(200)

        # Cantilever Beam Initialization
        npoints = 60
        width = 0.05
        thickness = 0.00575
        lenght = 0.58
        density = 7900
        elasticmod = 2e11
        Tsampling = 0.004
        nmodes = 5
        damp = [0.002, 0.002, 0.001, 0.001, 0.001]
        forcescaler = 1
        noisestd = 0

        self.beam = CantileverBeam(npoints, width, thickness, lenght, density,
                                   elasticmod, Tsampling, nmodes, damp,
                                   forcescaler, noisestd)
        self.beam.reset()
        self.prev_material = "Titânio Ti-6A1-4V"

        # Boxes configuration with default number of points
        self.ui.sbx_aposft.setMaximum(self.beam.npoints - 1)
        self.ui.sbx_rposft.setMaximum(self.beam.npoints - 1)

        # Fixed Time Initialization - 'Force x Time' chart
        layout_fft = QVBoxLayout(self.ui.wdg_forceft)
        static_canvas1 = FigureCanvas(Figure(figsize=(6, 4)))
        layout_fft.addWidget(static_canvas1)
        self.static_ax1 = static_canvas1.figure.subplots()
        self.static_ax1.set_title("Force", fontsize=16)
        self.static_ax1.set_xlabel("Time (s)")
        self.static_ax1.set_ylabel("Force (N)")

        # Fixed Time Initialization - 'Accelaration x Time' chart
        layout_aft = QVBoxLayout(self.ui.wdg_accetf)
        static_canvas2 = FigureCanvas(Figure(figsize=(6, 4)))
        layout_aft.addWidget(static_canvas2)
        self.static_ax2 = static_canvas2.figure.subplots()
        self.static_ax2.set_title("Acceleration", fontsize=16)
        self.static_ax2.set_xlabel("Time (s)")
        self.static_ax2.set_ylabel("Acceleration ($m/s^2$)")

        # Real Time Charts - Color Setup
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # Real Time Initialization - 'Force x Time' chart
        layout_frt = QVBoxLayout(self.ui.wdg_forcert)
        dynamic_can1 = pg.GraphicsWindow()
        layout_frt.addWidget(dynamic_can1)
        self.dynamic_ax1 = dynamic_can1.addPlot(title="Force")
        self.dynamic_ax1.setLabel('left', "Force (N)")
        self.dynamic_ax1.setLabel('bottom', "Time (s)")
        self.curve1 = self.dynamic_ax1.plot()

        # Real Time Initialization - 'Accelaration x Time' chart
        layout_art = QVBoxLayout(self.ui.wdg_accert)
        dynamic_canvas2 = pg.GraphicsWindow()
        layout_art.addWidget(dynamic_canvas2)
        self.dynamic_ax2 = dynamic_canvas2.addPlot(title="Acceleration")
        self.dynamic_ax2.setLabel('left', "Acceleration (m/s²)")
        self.dynamic_ax2.setLabel('bottom', "Time (s)")
        self.curve2 = self.dynamic_ax2.plot()

        # Connections
        self.ui.rbt_default.toggled.connect(self.settingsEnable)
        self.ui.cbx_material.currentTextChanged.connect(self.settingsMaterial)
        self.ui.btn_set.clicked.connect(self.settingsUpdate)
        self.ui.rbt_pulseft.toggled.connect(self.enableFixed)
        self.ui.btn_update.clicked.connect(self.updateFixed)
        self.ui.hsl_force.valueChanged.connect(self.updateBars)
        self.ui.hsl_freq.valueChanged.connect(self.updateBars)
        self.ui.rbt_normalrt.toggled.connect(self.enableSpeed)
        self.ui.rbt_pulsert.toggled.connect(self.enableReal)
        # self.ui.btn_startrt.clicked.connect(self.updateReal)

    def settingsEnable(self):
        """
        This function resets the labels to default values
        and disables the settings box when 'Default' is selected.
        When 'Insert' is selected, the settings box is enabled.
        """

        if self.ui.rbt_default.isChecked():
            self.ui.gbx_beamset.setDisabled(True)
            npoints = 60
            width = 0.05
            thickness = 0.00575
            length = 0.58
            density = 7900
            elasticmod = 2e11
            Tsampling = 0.004
            nmodes = 5
            damp = [0.002, 0.002, 0.001, 0.001, 0.001]
            forcescaler = 1
            noisestd = 0

            # Creates a new beam with the updated values
            self.beam = CantileverBeam(npoints, width, thickness, length,
                                       density, elasticmod, Tsampling,
                                       nmodes, damp, forcescaler, noisestd)
            self.beam.reset()

            self.ui.sbx_aposft.setMaximum(self.beam.npoints - 1)
            self.ui.sbx_rposft.setMaximum(self.beam.npoints - 1)
            self.ui.lbl_29.setText("Steel")
            self.ui.lbl_30.setText(str(200))
            self.ui.lbl_23.setText(str(self.beam.npoints))
            self.ui.lbl_25.setText(str(self.beam.width))
            self.ui.lbl_26.setText(str(self.beam.thickness))
            self.ui.lbl_27.setText(str(self.beam.length))
            self.ui.lbl_28.setText(str(self.beam.density))
        else:
            self.ui.gbx_beamset.setDisabled(False)

    def settingsMaterial(self):
        """
        This function receives the chosen material from the comboBox
        and then updates the elastic modulus box based on the material.
        However, the user may still change the elasticmod value.
        The automatic value is only a sugestion for simulation.
        """
        material = self.ui.cbx_material.currentText()

        if (material == 'Aço Estrutural A-36'):
            self.ui.dbx_elastic.setValue(200)
        if (material == 'Aço-ferramenta L2'):
            self.ui.dbx_elastic.setValue(200)
        elif (material == 'Aço Inoxidável 304'):
            self.ui.dbx_elastic.setValue(193)
        elif (material == 'Alumínio Forjado 2014-T6'):
            self.ui.dbx_elastic.setValue(73.1)
        elif (material == 'Alumínio Forjado 6061-T6'):
            self.ui.dbx_elastic.setValue(68.9)
        elif (material == 'Cobre Bronze C86100'):
            self.ui.dbx_elastic.setValue(103)
        elif (material == 'Cobre Latão Vermelho C83400'):
            self.ui.dbx_elastic.setValue(101)
        elif (material == 'Concreto Alta Resistência'):
            self.ui.dbx_elastic.setValue(29)
        elif (material == 'Concreto Baixa Resistência'):
            self.ui.dbx_elastic.setValue(22.1)
        elif (material == 'Ferro Fundido Cinza ASTM 20'):
            self.ui.dbx_elastic.setValue(67)
        elif (material == 'Ferro Fundido Maleável ASTM A-197'):
            self.ui.dbx_elastic.setValue(172)
        elif (material == 'Madeira Estrutural Abeto Douglas'):
            self.ui.dbx_elastic.setValue(13.1)
        elif (material == 'Madeira Estrutual Abeto Branco'):
            self.ui.dbx_elastic.setValue(9.65)
        elif (material == 'Magnésio Am 1004-T61'):
            self.ui.dbx_elastic.setValue(44.7)
        elif (material == 'Plástico Reforçado Keviar 49'):
            self.ui.dbx_elastic.setValue(131)
        elif (material == 'Plástico Reforçado 30% Vidro'):
            self.ui.dbx_elastic.setValue(72.4)
        elif (material == 'Titânio Ti-6A1-4V'):
            self.ui.dbx_elastic.setValue(120)

    def settingsUpdate(self):
        """
        This function recieves the settings for the beam
        and updates the 'Current Values' box on the GUI's
        """

        if self.ui.rbt_insert.isChecked():
            material = self.ui.cbx_material.currentText()
            elasticmod = (float(self.ui.dbx_elastic.value()) * (10 ** 9))
            npoints = int(self.ui.sbx_ndiv.value())
            width = float(self.ui.dbx_width.value())
            thickness = float(self.ui.dbx_thickn.value())
            length = float(self.ui.dbx_length.value())
            density = float(self.ui.dbx_density.value())
            Tsampling = 0.004
            nmodes = 5
            damp = [0.002, 0.002, 0.001, 0.001, 0.001]
            forcescaler = 1
            noisestd = 0

            # Creates a new beam with the updated values
            self.beam = CantileverBeam(npoints, width, thickness, length,
                                       density, elasticmod, Tsampling,
                                       nmodes, damp, forcescaler, noisestd)
            self.beam.reset()

            self.ui.sbx_aposft.setMaximum(self.beam.npoints - 1)
            self.ui.sbx_rposft.setMaximum(self.beam.npoints - 1)
            self.ui.lbl_29.setText(material)
            self.ui.lbl_30.setText(str(self.ui.dbx_elastic.value()))
            self.ui.lbl_23.setText(str(self.beam.npoints))
            self.ui.lbl_25.setText(str(self.beam.width))
            self.ui.lbl_26.setText(str(self.beam.thickness))
            self.ui.lbl_27.setText(str(self.beam.length))
            self.ui.lbl_28.setText(str(self.beam.density))
            self.prev_material = material

    def enableFixed(self):
        """
        This function changes the enabled lables and input boxes,
        depending on the selected type of disturbance.
        """

        if self.ui.rbt_harft.isChecked():
            # Harmonic Force Mode
            self.ui.lbl_13.setDisabled(False)
            self.ui.lbl_freqft.setDisabled(False)
            self.ui.lbl_14.setDisabled(False)
            self.ui.dbx_freqft.setDisabled(False)
            self.ui.lbl_1.setDisabled(True)
            self.ui.lbl_forceft.setDisabled(True)
            self.ui.lbl_5.setDisabled(True)
            self.ui.dbx_forceft.setDisabled(True)
        else:
            # Single Pulse Mode
            self.ui.lbl_1.setDisabled(False)
            self.ui.lbl_forceft.setDisabled(False)
            self.ui.lbl_5.setDisabled(False)
            self.ui.dbx_forceft.setDisabled(False)
            self.ui.lbl_13.setDisabled(True)
            self.ui.lbl_freqft.setDisabled(True)
            self.ui.lbl_14.setDisabled(True)
            self.ui.dbx_freqft.setDisabled(True)

    def updateFixed(self):
        """
        This function receives values for the fixed time simulation.
        The updated values are shown on the GUI's 'Current Values' box.
        The new inputs update the fixed time chart
        when the push button is clicked.
        """

        # Receives values
        force_ft = self.ui.dbx_forceft.value()
        time_ft = self.ui.box_time.time()
        time_ftprint = time_ft.toString("mm:ss")
        apos_ft = self.ui.sbx_aposft.value()
        rpos_ft = self.ui.sbx_rposft.value()
        freq_ft = self.ui.dbx_freqft.value()

        # Shows new values on screen
        self.ui.lbl_forceft.setText(str(force_ft))
        self.ui.lbl_timeft.setText(time_ftprint)
        self.ui.lbl_aposft.setText(str(apos_ft))
        self.ui.lbl_rposft.setText(str(rpos_ft))
        self.ui.lbl_freqft.setText(str(freq_ft))

        # Sets parameters
        seconds = QtCore.QTime(0, 0, 0).secsTo(time_ft)
        periods = seconds / 0.004  # (Tsampling = 0.004)
        acceleration = np.zeros(int(periods))
        t = np.arange(0, seconds, 0.004)

        # Different paths based on the selected type of disturbance
        # Single Pulse
        if self.ui.rbt_pulseft.isChecked():
            self.beam.setforce(apos_ft, force_ft)
            self.beam.update()
            self.beam.setforce(apos_ft, 0)

            for k in range(int(periods)):
                acceleration[k] = self.beam.getaccelms2(rpos_ft)
                self.beam.update()

        # Harmonic Force
        else:
            F_disturb = np.sin(2 * np.pi * freq_ft * t)
            self.beam.reset()

            for j in range(int(periods)):
                self.beam.setforce(apos_ft, F_disturb[j])
                acceleration[j] = self.beam.getaccelms2(rpos_ft)
                self.beam.update()

        # Reseting Charts
        self.static_ax1.clear()
        self.static_ax1.set_title("Force", fontsize=16)
        self.static_ax1.set_xlabel("Time (s)")
        self.static_ax1.set_ylabel("Force (N)")
        self.static_ax2.clear()
        self.static_ax2.set_title("Acceleration", fontsize=16)
        self.static_ax2.set_xlabel("Time (s)")
        self.static_ax2.set_ylabel("Acceleration ($m/s^2$)")

        # Ploting 'Force x Time' chart
        if self.ui.rbt_pulseft.isChecked():
            F_disturb = 0 * t
            F_disturb[0] = force_ft

        self.static_ax1.plot(t, F_disturb)
        self.static_ax1.figure.canvas.draw()

        # Ploting 'Acceleration x Time' chart
        self.static_ax2.plot(t, acceleration)
        self.static_ax2.figure.canvas.draw()

    def updateBars(self):
        """
        This function updates the labels with the current values
        of the force and frequency slide bars.
        """
        self.ui.lbl_forcert.setText(str(self.ui.hsl_force.value()))
        self.ui.lbl_freqrt.setText(str(self.ui.hsl_freq.value()))

    def enableSpeed(self):
        """
        This function enables or disables the radio buttons
        based on the selected time speed.
        """

        if self.ui.rbt_smotionrt.isChecked():
            # Slow motion
            self.ui.gbx_speedsm.setDisabled(False)
        else:
            # Normal time
            self.ui.gbx_speedsm.setDisabled(True)

    def enableReal(self):
        """
        This function enables or disables the input boxes
        on the Real Time page, based on the selected disturbance.
        """

        if self.ui.rbt_pulsert.isChecked():
            # Single Pulse Mode
            self.ui.lbl_11.setDisabled(False)
            self.ui.hsl_force.setDisabled(False)
            self.ui.lbl_forcert.setDisabled(False)
            self.ui.lbl_12.setDisabled(True)
            self.ui.hsl_freq.setDisabled(True)
            self.ui.lbl_freqrt.setDisabled(True)
        else:
            # Harmonic Force mode
            self.ui.lbl_11.setDisabled(True)
            self.ui.hsl_force.setDisabled(True)
            self.ui.lbl_forcert.setDisabled(True)
            self.ui.lbl_12.setDisableded(False)
            self.ui.hsl_freq.setDisabl(False)
            self.ui.lbl_freqrt.setDisabled(False)

    def updateReal(self):
        """
        This function recieves the new values for the Real Time
        simulation and plots the dynamic chart.
        """
