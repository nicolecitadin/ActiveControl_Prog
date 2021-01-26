import numpy as np
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
        self.ui.sbx_aposft.setMaximum(60)
        self.ui.sbx_rposft.setMaximum(60)
        self.ui.box_time.setDisplayFormat("mm:ss")

        # Beam Settings - Default Values
        npoints = 60
        width = 0.05
        thickness = 0.00575
        lenght = 0.58
        density = 7900
        elasticmod = 2e11
        Tsampling = 0.004

        # Cantilever Beam Initialization
        self.beam = CantileverBeam(npoints, width, thickness, lenght, density, elasticmod, Tsampling)
        self.beam.reset()

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

        # Connections
        self.ui.rbt_default.toggled.connect(self.settingsEnable)
        self.ui.btn_set.clicked.connect(self.settingsUpdate)
        self.ui.rbt_pulseft.toggled.connect(self.enableInputs)
        self.ui.btn_update.clicked.connect(self.updateValues)

    def settingsEnable(self):
        """
        This function resets the labels to default values
        and disables the settings box when 'Default' is selected.
        When 'Insert' is selected, the settings box is enabled.
        """

        if self.ui.rbt_default.isChecked():
            self.ui.gbx_beamset.setDisabled(True)
            self.beam.elasticmod = 200
            self.beam.npoints = 60
            self.beam.width = 0.05
            self.beam.thickness = 0.00575
            self.beam.length = 0.58
            self.beam.density = 7900
            self.ui.lbl_29.setText("Steel")
            self.ui.lbl_30.setText(str(self.beam.elasticmod))
            self.ui.lbl_23.setText(str(self.beam.npoints))
            self.ui.lbl_25.setText(str(self.beam.width))
            self.ui.lbl_26.setText(str(self.beam.thickness))
            self.ui.lbl_27.setText(str(self.beam.length))
            self.ui.lbl_28.setText(str(self.beam.density))
        else:
            self.ui.gbx_beamset.setDisabled(False)

    def settingsUpdate(self):
        """
        This function recieves the settings for the beam
        and updates the 'Current Values' box on the GUI's
        """
        material = self.ui.cbx_material.currentText()
        self.beam.elasticmod = self.ui.dbx_elastm.value()
        self.beam.npoints = self.ui.sbx_ndiv.value()
        self.beam.width = self.ui.dbx_width.value()
        self.beam.thickness = self.ui.dbx_thickn.value()
        self.beam.length = self.ui.dbx_length.value()
        self.beam.density = self.ui.dbx_density.value()
        self.ui.lbl_29.setText(material)
        self.ui.lbl_30.setText(str(self.beam.elasticmod))
        self.ui.lbl_23.setText(str(self.beam.npoints))
        self.ui.lbl_25.setText(str(self.beam.width))
        self.ui.lbl_26.setText(str(self.beam.thickness))
        self.ui.lbl_27.setText(str(self.beam.length))
        self.ui.lbl_28.setText(str(self.beam.density))

    def enableInputs(self):
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

    def updateValues(self):
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
