#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from std_msgs.msg import Float64
from snake_panel.msg import gaitparam

global amplitude, frequency, hor_amplitude, phi, nu, gait

amplitude = 0
frequency = 0
hor_amplitude = 0
phi = 0
nu = 0
gait = "None"

amplitude_limit = 20
frequency_limit = 2.0
phi_limit = 0.2
nu_limit = 0.2

amplitude_gain = amplitude_limit/20.0
frequency_gain = frequency_limit/20.0
phi_gain = phi_limit/20.0
nu_gain = nu_limit/20.0

class Ui_GaitControl(object):
    def setupUi(self, GaitControl):
        GaitControl.setObjectName("GaitControl")
        GaitControl.resize(673, 357)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 611, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.Rolling = QtWidgets.QWidget()
        self.Rolling.setObjectName("Rolling")
        self.rolling_freq_label = QtWidgets.QLabel(self.Rolling)
        self.rolling_freq_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.rolling_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rolling_freq_label.setObjectName("rolling_freq_label")
        self.rolling_freq = QtWidgets.QSlider(self.Rolling)
        self.rolling_freq.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.rolling_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rolling_freq.setMouseTracking(False)
        self.rolling_freq.setMaximum(20)
        self.rolling_freq.setPageStep(4)
        self.rolling_freq.setOrientation(QtCore.Qt.Horizontal)
        self.rolling_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rolling_freq.setTickInterval(0)
        self.rolling_freq.setObjectName("rolling_freq")
        self.rolling_amp_plus = QtWidgets.QPushButton(self.Rolling)
        self.rolling_amp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.rolling_amp_plus.setIconSize(QtCore.QSize(14, 14))
        self.rolling_amp_plus.setObjectName("rolling_amp_plus")
        self.rolling_freq_plus = QtWidgets.QPushButton(self.Rolling)
        self.rolling_freq_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.rolling_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.rolling_freq_plus.setObjectName("rolling_freq_plus")
        self.rolling_amp_minus = QtWidgets.QPushButton(self.Rolling)
        self.rolling_amp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.rolling_amp_minus.setIconSize(QtCore.QSize(14, 14))
        self.rolling_amp_minus.setObjectName("rolling_amp_minus")
        self.label_12 = QtWidgets.QLabel(self.Rolling)
        self.label_12.setGeometry(QtCore.QRect(70, 80, 81, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Rolling)
        self.label_13.setGeometry(QtCore.QRect(70, 30, 81, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.rolling_amp = QtWidgets.QSlider(self.Rolling)
        self.rolling_amp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.rolling_amp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rolling_amp.setMouseTracking(False)
        self.rolling_amp.setMaximum(20)
        self.rolling_amp.setPageStep(4)
        self.rolling_amp.setOrientation(QtCore.Qt.Horizontal)
        self.rolling_amp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rolling_amp.setTickInterval(0)
        self.rolling_amp.setObjectName("rolling_amp")
        self.rolling_freq_minus = QtWidgets.QPushButton(self.Rolling)
        self.rolling_freq_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.rolling_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.rolling_freq_minus.setObjectName("rolling_freq_minus")
        self.rolling_amp_label = QtWidgets.QLabel(self.Rolling)
        self.rolling_amp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.rolling_amp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rolling_amp_label.setObjectName("rolling_amp_label")
        self.tabWidget.addTab(self.Rolling, "")
        self.Sidewinding = QtWidgets.QWidget()
        self.Sidewinding.setObjectName("Sidewinding")
        self.side_freq_label = QtWidgets.QLabel(self.Sidewinding)
        self.side_freq_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.side_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.side_freq_label.setObjectName("side_freq_label")
        self.side_amp_label = QtWidgets.QLabel(self.Sidewinding)
        self.side_amp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.side_amp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.side_amp_label.setObjectName("side_amp_label")
        self.label_23 = QtWidgets.QLabel(self.Sidewinding)
        self.label_23.setGeometry(QtCore.QRect(70, 80, 81, 20))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.side_freq_minus = QtWidgets.QPushButton(self.Sidewinding)
        self.side_freq_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.side_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.side_freq_minus.setObjectName("side_freq_minus")
        self.side_amp_minus = QtWidgets.QPushButton(self.Sidewinding)
        self.side_amp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.side_amp_minus.setIconSize(QtCore.QSize(14, 14))
        self.side_amp_minus.setObjectName("side_amp_minus")
        self.label_25 = QtWidgets.QLabel(self.Sidewinding)
        self.label_25.setGeometry(QtCore.QRect(70, 30, 81, 20))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.side_freq = QtWidgets.QSlider(self.Sidewinding)
        self.side_freq.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.side_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.side_freq.setMouseTracking(False)
        self.side_freq.setMaximum(20)
        self.side_freq.setPageStep(4)
        self.side_freq.setOrientation(QtCore.Qt.Horizontal)
        self.side_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.side_freq.setTickInterval(0)
        self.side_freq.setObjectName("side_freq")
        self.side_amp = QtWidgets.QSlider(self.Sidewinding)
        self.side_amp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.side_amp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.side_amp.setMouseTracking(False)
        self.side_amp.setMaximum(20)
        self.side_amp.setPageStep(4)
        self.side_amp.setOrientation(QtCore.Qt.Horizontal)
        self.side_amp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.side_amp.setTickInterval(0)
        self.side_amp.setObjectName("side_amp")
        self.side_freq_plus = QtWidgets.QPushButton(self.Sidewinding)
        self.side_freq_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.side_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.side_freq_plus.setObjectName("side_freq_plus")
        self.side_amp_plus = QtWidgets.QPushButton(self.Sidewinding)
        self.side_amp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.side_amp_plus.setIconSize(QtCore.QSize(14, 14))
        self.side_amp_plus.setObjectName("side_amp_plus")
        self.tabWidget.addTab(self.Sidewinding, "")
        self.Vertical = QtWidgets.QWidget()
        self.Vertical.setObjectName("Vertical")
        self.ver_freq = QtWidgets.QSlider(self.Vertical)
        self.ver_freq.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.ver_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ver_freq.setMouseTracking(False)
        self.ver_freq.setMaximum(20)
        self.ver_freq.setPageStep(4)
        self.ver_freq.setOrientation(QtCore.Qt.Horizontal)
        self.ver_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ver_freq.setTickInterval(0)
        self.ver_freq.setObjectName("ver_freq")
        self.ver_freq_plus = QtWidgets.QPushButton(self.Vertical)
        self.ver_freq_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.ver_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.ver_freq_plus.setObjectName("ver_freq_plus")
        self.ver_amp_minus = QtWidgets.QPushButton(self.Vertical)
        self.ver_amp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.ver_amp_minus.setIconSize(QtCore.QSize(14, 14))
        self.ver_amp_minus.setObjectName("ver_amp_minus")
        self.label_27 = QtWidgets.QLabel(self.Vertical)
        self.label_27.setGeometry(QtCore.QRect(70, 80, 81, 20))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.ver_amp = QtWidgets.QSlider(self.Vertical)
        self.ver_amp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.ver_amp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ver_amp.setMouseTracking(False)
        self.ver_amp.setMaximum(20)
        self.ver_amp.setPageStep(4)
        self.ver_amp.setOrientation(QtCore.Qt.Horizontal)
        self.ver_amp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ver_amp.setTickInterval(0)
        self.ver_amp.setObjectName("ver_amp")
        self.ver_freq_minus = QtWidgets.QPushButton(self.Vertical)
        self.ver_freq_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.ver_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.ver_freq_minus.setObjectName("ver_freq_minus")
        self.ver_amp_label = QtWidgets.QLabel(self.Vertical)
        self.ver_amp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.ver_amp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ver_amp_label.setObjectName("ver_amp_label")
        self.ver_amp_plus = QtWidgets.QPushButton(self.Vertical)
        self.ver_amp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.ver_amp_plus.setIconSize(QtCore.QSize(14, 14))
        self.ver_amp_plus.setObjectName("ver_amp_plus")
        self.label_29 = QtWidgets.QLabel(self.Vertical)
        self.label_29.setGeometry(QtCore.QRect(70, 30, 81, 20))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.ver_freq_label = QtWidgets.QLabel(self.Vertical)
        self.ver_freq_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.ver_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ver_freq_label.setObjectName("ver_freq_label")
        self.tabWidget.addTab(self.Vertical, "")
        self.Pipe = QtWidgets.QWidget()
        self.Pipe.setObjectName("Pipe")
        self.pipe_phi_minus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_phi_minus.setGeometry(QtCore.QRect(174, 130, 21, 21))
        self.pipe_phi_minus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_phi_minus.setObjectName("pipe_phi_minus")
        self.pipe_amp_minus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_amp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.pipe_amp_minus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_amp_minus.setObjectName("pipe_amp_minus")
        self.pipe_amp_label = QtWidgets.QLabel(self.Pipe)
        self.pipe_amp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.pipe_amp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pipe_amp_label.setObjectName("pipe_amp_label")
        self.pipe_phi_plus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_phi_plus.setGeometry(QtCore.QRect(454, 130, 21, 21))
        self.pipe_phi_plus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_phi_plus.setObjectName("pipe_phi_plus")
        self.label_16 = QtWidgets.QLabel(self.Pipe)
        self.label_16.setGeometry(QtCore.QRect(70, 80, 81, 20))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.pipe_phi_label = QtWidgets.QLabel(self.Pipe)
        self.pipe_phi_label.setGeometry(QtCore.QRect(484, 130, 31, 17))
        self.pipe_phi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pipe_phi_label.setObjectName("pipe_phi_label")
        self.pipe_phi = QtWidgets.QSlider(self.Pipe)
        self.pipe_phi.setGeometry(QtCore.QRect(204, 120, 241, 41))
        self.pipe_phi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pipe_phi.setMouseTracking(False)
        self.pipe_phi.setMaximum(20)
        self.pipe_phi.setPageStep(4)
        self.pipe_phi.setOrientation(QtCore.Qt.Horizontal)
        self.pipe_phi.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.pipe_phi.setTickInterval(0)
        self.pipe_phi.setObjectName("pipe_phi")
        self.pipe_freq_label = QtWidgets.QLabel(self.Pipe)
        self.pipe_freq_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.pipe_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pipe_freq_label.setObjectName("pipe_freq_label")
        self.pipe_nu_label = QtWidgets.QLabel(self.Pipe)
        self.pipe_nu_label.setGeometry(QtCore.QRect(484, 180, 31, 17))
        self.pipe_nu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pipe_nu_label.setObjectName("pipe_nu_label")
        self.label_20 = QtWidgets.QLabel(self.Pipe)
        self.label_20.setGeometry(QtCore.QRect(70, 180, 81, 20))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pipe_freq = QtWidgets.QSlider(self.Pipe)
        self.pipe_freq.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.pipe_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pipe_freq.setMouseTracking(False)
        self.pipe_freq.setMaximum(20)
        self.pipe_freq.setPageStep(4)
        self.pipe_freq.setOrientation(QtCore.Qt.Horizontal)
        self.pipe_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.pipe_freq.setTickInterval(0)
        self.pipe_freq.setObjectName("pipe_freq")
        self.pipe_nu = QtWidgets.QSlider(self.Pipe)
        self.pipe_nu.setGeometry(QtCore.QRect(204, 170, 241, 41))
        self.pipe_nu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pipe_nu.setMouseTracking(False)
        self.pipe_nu.setMaximum(20)
        self.pipe_nu.setPageStep(4)
        self.pipe_nu.setOrientation(QtCore.Qt.Horizontal)
        self.pipe_nu.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.pipe_nu.setTickInterval(0)
        self.pipe_nu.setObjectName("pipe_nu")
        self.pipe_amp = QtWidgets.QSlider(self.Pipe)
        self.pipe_amp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.pipe_amp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pipe_amp.setMouseTracking(False)
        self.pipe_amp.setMaximum(20)
        self.pipe_amp.setPageStep(4)
        self.pipe_amp.setOrientation(QtCore.Qt.Horizontal)
        self.pipe_amp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.pipe_amp.setTickInterval(0)
        self.pipe_amp.setObjectName("pipe_amp")
        self.pipe_freq_minus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_freq_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.pipe_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_freq_minus.setObjectName("pipe_freq_minus")
        self.label_21 = QtWidgets.QLabel(self.Pipe)
        self.label_21.setGeometry(QtCore.QRect(70, 130, 81, 20))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.pipe_amp_plus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_amp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.pipe_amp_plus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_amp_plus.setObjectName("pipe_amp_plus")
        self.pipe_nu_plus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_nu_plus.setGeometry(QtCore.QRect(454, 180, 21, 21))
        self.pipe_nu_plus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_nu_plus.setObjectName("pipe_nu_plus")
        self.pipe_nu_minus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_nu_minus.setGeometry(QtCore.QRect(174, 180, 21, 21))
        self.pipe_nu_minus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_nu_minus.setObjectName("pipe_nu_minus")
        self.pipe_freq_plus = QtWidgets.QPushButton(self.Pipe)
        self.pipe_freq_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.pipe_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.pipe_freq_plus.setObjectName("pipe_freq_plus")
        self.label_22 = QtWidgets.QLabel(self.Pipe)
        self.label_22.setGeometry(QtCore.QRect(70, 30, 81, 20))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.Pipe, "")
        self.Sinuslifting = QtWidgets.QWidget()
        self.Sinuslifting.setObjectName("Sinuslifting")
        self.sinus_freq_label = QtWidgets.QLabel(self.Sinuslifting)
        self.sinus_freq_label.setGeometry(QtCore.QRect(484, 130, 31, 17))
        self.sinus_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sinus_freq_label.setObjectName("sinus_freq_label")
        self.sinus_freq = QtWidgets.QSlider(self.Sinuslifting)
        self.sinus_freq.setGeometry(QtCore.QRect(204, 120, 241, 41))
        self.sinus_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sinus_freq.setMouseTracking(False)
        self.sinus_freq.setMaximum(20)
        self.sinus_freq.setPageStep(4)
        self.sinus_freq.setOrientation(QtCore.Qt.Horizontal)
        self.sinus_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sinus_freq.setTickInterval(0)
        self.sinus_freq.setObjectName("sinus_freq")
        self.sinus_veramp_label = QtWidgets.QLabel(self.Sinuslifting)
        self.sinus_veramp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.sinus_veramp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sinus_veramp_label.setObjectName("sinus_veramp_label")
        self.sinus_freq_plus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_freq_plus.setGeometry(QtCore.QRect(454, 130, 21, 21))
        self.sinus_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_freq_plus.setObjectName("sinus_freq_plus")
        self.sinus_veramp = QtWidgets.QSlider(self.Sinuslifting)
        self.sinus_veramp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.sinus_veramp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sinus_veramp.setMouseTracking(False)
        self.sinus_veramp.setMaximum(20)
        self.sinus_veramp.setPageStep(4)
        self.sinus_veramp.setOrientation(QtCore.Qt.Horizontal)
        self.sinus_veramp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sinus_veramp.setTickInterval(0)
        self.sinus_veramp.setObjectName("sinus_veramp")
        self.sinus_veramp_minus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_veramp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.sinus_veramp_minus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_veramp_minus.setObjectName("sinus_veramp_minus")
        self.sinus_veramp_plus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_veramp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.sinus_veramp_plus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_veramp_plus.setObjectName("sinus_veramp_plus")
        self.label_31 = QtWidgets.QLabel(self.Sinuslifting)
        self.label_31.setGeometry(QtCore.QRect(70, 130, 81, 20))
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.sinus_freq_minus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_freq_minus.setGeometry(QtCore.QRect(174, 130, 21, 21))
        self.sinus_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_freq_minus.setObjectName("sinus_freq_minus")
        self.label_33 = QtWidgets.QLabel(self.Sinuslifting)
        self.label_33.setGeometry(QtCore.QRect(74, 37, 71, 20))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.sinus_horamp_label = QtWidgets.QLabel(self.Sinuslifting)
        self.sinus_horamp_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.sinus_horamp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sinus_horamp_label.setObjectName("sinus_horamp_label")
        self.sinus_horamp = QtWidgets.QSlider(self.Sinuslifting)
        self.sinus_horamp.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.sinus_horamp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sinus_horamp.setMouseTracking(False)
        self.sinus_horamp.setMaximum(20)
        self.sinus_horamp.setPageStep(4)
        self.sinus_horamp.setOrientation(QtCore.Qt.Horizontal)
        self.sinus_horamp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sinus_horamp.setTickInterval(0)
        self.sinus_horamp.setObjectName("sinus_horamp")
        self.sinus_horamp_minus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_horamp_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.sinus_horamp_minus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_horamp_minus.setObjectName("sinus_horamp_minus")
        self.sinus_horamp_plus = QtWidgets.QPushButton(self.Sinuslifting)
        self.sinus_horamp_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.sinus_horamp_plus.setIconSize(QtCore.QSize(14, 14))
        self.sinus_horamp_plus.setObjectName("sinus_horamp_plus")
        self.label_36 = QtWidgets.QLabel(self.Sinuslifting)
        self.label_36.setGeometry(QtCore.QRect(74, 87, 71, 20))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.Sinuslifting)
        self.label_37.setGeometry(QtCore.QRect(74, 23, 71, 20))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.Sinuslifting)
        self.label_38.setGeometry(QtCore.QRect(74, 73, 71, 20))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.tabWidget.addTab(self.Sinuslifting, "")
        self.Rotating = QtWidgets.QWidget()
        self.Rotating.setObjectName("Rotating")
        self.rot_veramp_label = QtWidgets.QLabel(self.Rotating)
        self.rot_veramp_label.setGeometry(QtCore.QRect(484, 30, 31, 17))
        self.rot_veramp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rot_veramp_label.setObjectName("rot_veramp_label")
        self.rot_freq = QtWidgets.QSlider(self.Rotating)
        self.rot_freq.setGeometry(QtCore.QRect(204, 120, 241, 41))
        self.rot_freq.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rot_freq.setMouseTracking(False)
        self.rot_freq.setMaximum(20)
        self.rot_freq.setPageStep(4)
        self.rot_freq.setOrientation(QtCore.Qt.Horizontal)
        self.rot_freq.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rot_freq.setTickInterval(0)
        self.rot_freq.setObjectName("rot_freq")
        self.rot_veramp = QtWidgets.QSlider(self.Rotating)
        self.rot_veramp.setGeometry(QtCore.QRect(204, 20, 241, 41))
        self.rot_veramp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rot_veramp.setMouseTracking(False)
        self.rot_veramp.setMaximum(20)
        self.rot_veramp.setPageStep(4)
        self.rot_veramp.setOrientation(QtCore.Qt.Horizontal)
        self.rot_veramp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rot_veramp.setTickInterval(0)
        self.rot_veramp.setObjectName("rot_veramp")
        self.rot_freq_plus = QtWidgets.QPushButton(self.Rotating)
        self.rot_freq_plus.setGeometry(QtCore.QRect(454, 130, 21, 21))
        self.rot_freq_plus.setIconSize(QtCore.QSize(14, 14))
        self.rot_freq_plus.setObjectName("rot_freq_plus")
        self.rot_veramp_minus = QtWidgets.QPushButton(self.Rotating)
        self.rot_veramp_minus.setGeometry(QtCore.QRect(174, 30, 21, 21))
        self.rot_veramp_minus.setIconSize(QtCore.QSize(14, 14))
        self.rot_veramp_minus.setObjectName("rot_veramp_minus")
        self.rot_veramp_plus = QtWidgets.QPushButton(self.Rotating)
        self.rot_veramp_plus.setGeometry(QtCore.QRect(454, 30, 21, 21))
        self.rot_veramp_plus.setIconSize(QtCore.QSize(14, 14))
        self.rot_veramp_plus.setObjectName("rot_veramp_plus")
        self.rot_horamp_label = QtWidgets.QLabel(self.Rotating)
        self.rot_horamp_label.setGeometry(QtCore.QRect(484, 80, 31, 17))
        self.rot_horamp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rot_horamp_label.setObjectName("rot_freq_label")
        self.label_41 = QtWidgets.QLabel(self.Rotating)
        self.label_41.setGeometry(QtCore.QRect(74, 23, 71, 20))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.Rotating)
        self.label_42.setGeometry(QtCore.QRect(70, 130, 81, 20))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.rot_horamp_plus = QtWidgets.QPushButton(self.Rotating)
        self.rot_horamp_plus.setGeometry(QtCore.QRect(454, 80, 21, 21))
        self.rot_horamp_plus.setIconSize(QtCore.QSize(14, 14))
        self.rot_horamp_plus.setObjectName("rot_horamp_plus")
        self.label_43 = QtWidgets.QLabel(self.Rotating)
        self.label_43.setGeometry(QtCore.QRect(74, 73, 71, 20))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.rot_freq_minus = QtWidgets.QPushButton(self.Rotating)
        self.rot_freq_minus.setGeometry(QtCore.QRect(174, 130, 21, 21))
        self.rot_freq_minus.setIconSize(QtCore.QSize(14, 14))
        self.rot_freq_minus.setObjectName("rot_freq_minus")
        self.label_44 = QtWidgets.QLabel(self.Rotating)
        self.label_44.setGeometry(QtCore.QRect(74, 37, 71, 20))
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.rot_freq_label = QtWidgets.QLabel(self.Rotating)
        self.rot_freq_label.setGeometry(QtCore.QRect(484, 130, 31, 17))
        self.rot_freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rot_freq_label.setObjectName("rot_horamp_label")
        self.rot_horamp = QtWidgets.QSlider(self.Rotating)
        self.rot_horamp.setGeometry(QtCore.QRect(204, 70, 241, 41))
        self.rot_horamp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rot_horamp.setMouseTracking(False)
        self.rot_horamp.setMaximum(20)
        self.rot_horamp.setPageStep(4)
        self.rot_horamp.setOrientation(QtCore.Qt.Horizontal)
        self.rot_horamp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rot_horamp.setTickInterval(0)
        self.rot_horamp.setObjectName("rot_horamp")
        self.rot_horamp_minus = QtWidgets.QPushButton(self.Rotating)
        self.rot_horamp_minus.setGeometry(QtCore.QRect(174, 80, 21, 21))
        self.rot_horamp_minus.setIconSize(QtCore.QSize(14, 14))
        self.rot_horamp_minus.setObjectName("rot_horamp_minus")
        self.label_46 = QtWidgets.QLabel(self.Rotating)
        self.label_46.setGeometry(QtCore.QRect(74, 87, 71, 20))
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.tabWidget.addTab(self.Rotating, "")
        self.apply = QtWidgets.QPushButton(self.dockWidgetContents)
        self.apply.setGeometry(QtCore.QRect(30, 290, 89, 25))
        self.apply.setObjectName("apply")
        self.quit = QtWidgets.QPushButton(self.dockWidgetContents)
        self.quit.setGeometry(QtCore.QRect(540, 290, 89, 25))
        self.quit.setObjectName("quit")
        self.stretch = QtWidgets.QPushButton(self.dockWidgetContents)
        self.stretch.setGeometry(QtCore.QRect(130, 290, 89, 25))
        self.stretch.setObjectName("stretch")
        self.Reset = QtWidgets.QPushButton(self.dockWidgetContents)
        self.Reset.setGeometry(QtCore.QRect(230, 290, 89, 25))
        self.Reset.setObjectName("Reset")
        GaitControl.setWidget(self.dockWidgetContents)

        self.retranslateUi(GaitControl)
        self.tabWidget.setCurrentIndex(0)



        self.rolling_amp.valueChanged['int'].connect(self.rolling_amp_label.setNum)
        self.rolling_freq.valueChanged['int'].connect(self.rol_freq_setNum)
        self.side_amp.valueChanged['int'].connect(self.side_amp_label.setNum)
        self.side_freq.valueChanged['int'].connect(self.side_freq_setNum)
        self.ver_amp.valueChanged['int'].connect(self.ver_amp_label.setNum)
        self.ver_freq.valueChanged['int'].connect(self.ver_freq_setNum)
        self.pipe_amp.valueChanged['int'].connect(self.pipe_amp_label.setNum)
        self.pipe_freq.valueChanged['int'].connect(self.pipe_freq_setNum)
        self.pipe_phi.valueChanged['int'].connect(self.pipe_phi_setNum)
        self.pipe_nu.valueChanged['int'].connect(self.pipe_nu_setNum)
        self.sinus_veramp.valueChanged['int'].connect(self.sinus_veramp_label.setNum)
        self.sinus_horamp.valueChanged['int'].connect(self.sinus_horamp_label.setNum)
        self.sinus_freq.valueChanged['int'].connect(self.sinus_freq_setNum)
        self.rot_veramp.valueChanged['int'].connect(self.rot_veramp_label.setNum)
        self.rot_horamp.valueChanged['int'].connect(self.rot_horamp_label.setNum)
        self.rot_freq.valueChanged['int'].connect(self.rot_freq_setNum)

        self.rolling_amp.valueChanged['int'].connect(self.update_amp)
        self.rolling_freq.valueChanged['int'].connect(self.update_freq)
        self.side_amp.valueChanged['int'].connect(self.update_amp)
        self.side_freq.valueChanged['int'].connect(self.update_freq)
        self.ver_amp.valueChanged['int'].connect(self.update_amp)
        self.ver_freq.valueChanged['int'].connect(self.update_freq)
        self.pipe_amp.valueChanged['int'].connect(self.update_amp)
        self.pipe_freq.valueChanged['int'].connect(self.update_freq)
        self.pipe_phi.valueChanged['int'].connect(self.update_phi)
        self.pipe_nu.valueChanged['int'].connect(self.update_nu)
        self.sinus_veramp.valueChanged['int'].connect(self.update_amp)
        self.sinus_horamp.valueChanged['int'].connect(self.update_hor_amp)
        self.sinus_freq.valueChanged['int'].connect(self.update_freq)
        self.rot_veramp.valueChanged['int'].connect(self.update_amp)
        self.rot_horamp.valueChanged['int'].connect(self.update_hor_amp)
        self.rot_freq.valueChanged['int'].connect(self.update_freq)

        self.functions(GaitControl)
        self.buttonUi(GaitControl)

        QtCore.QMetaObject.connectSlotsByName(GaitControl)




    def retranslateUi(self, GaitControl):
        _translate = QtCore.QCoreApplication.translate
        GaitControl.setWindowTitle(_translate("GaitControl", "GaitControl"))
        self.rolling_freq_label.setText(_translate("GaitControl", "0"))
        self.rolling_amp_plus.setText(_translate("GaitControl", "+"))
        self.rolling_freq_plus.setText(_translate("GaitControl", "+"))
        self.rolling_amp_minus.setText(_translate("GaitControl", "-"))
        self.label_12.setText(_translate("GaitControl", "Frequency"))
        self.label_13.setText(_translate("GaitControl", "Amplitude"))
        self.rolling_freq_minus.setText(_translate("GaitControl", "-"))
        self.rolling_amp_label.setText(_translate("GaitControl", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Rolling), _translate("GaitControl", "Rolling"))
        self.side_freq_label.setText(_translate("GaitControl", "0"))
        self.side_amp_label.setText(_translate("GaitControl", "0"))
        self.label_23.setText(_translate("GaitControl", "Frequency"))
        self.side_freq_minus.setText(_translate("GaitControl", "-"))
        self.side_amp_minus.setText(_translate("GaitControl", "-"))
        self.label_25.setText(_translate("GaitControl", "Amplitude"))
        self.side_freq_plus.setText(_translate("GaitControl", "+"))
        self.side_amp_plus.setText(_translate("GaitControl", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sidewinding), _translate("GaitControl", "Sidewinding"))
        self.ver_freq_plus.setText(_translate("GaitControl", "+"))
        self.ver_amp_minus.setText(_translate("GaitControl", "-"))
        self.label_27.setText(_translate("GaitControl", "Frequency"))
        self.ver_freq_minus.setText(_translate("GaitControl", "-"))
        self.ver_amp_label.setText(_translate("GaitControl", "0"))
        self.ver_amp_plus.setText(_translate("GaitControl", "+"))
        self.label_29.setText(_translate("GaitControl", "Amplitude"))
        self.ver_freq_label.setText(_translate("GaitControl", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vertical), _translate("GaitControl", "Vertical"))
        self.pipe_phi_minus.setText(_translate("GaitControl", "-"))
        self.pipe_amp_minus.setText(_translate("GaitControl", "-"))
        self.pipe_amp_label.setText(_translate("GaitControl", "0"))
        self.pipe_phi_plus.setText(_translate("GaitControl", "+"))
        self.label_16.setText(_translate("GaitControl", "Frequency"))
        self.pipe_phi_label.setText(_translate("GaitControl", "0"))
        self.pipe_freq_label.setText(_translate("GaitControl", "0"))
        self.pipe_nu_label.setText(_translate("GaitControl", "0"))
        self.label_20.setText(_translate("GaitControl", "Nu"))
        self.pipe_freq_minus.setText(_translate("GaitControl", "-"))
        self.label_21.setText(_translate("GaitControl", "Phi"))
        self.pipe_amp_plus.setText(_translate("GaitControl", "+"))
        self.pipe_nu_plus.setText(_translate("GaitControl", "+"))
        self.pipe_nu_minus.setText(_translate("GaitControl", "-"))
        self.pipe_freq_plus.setText(_translate("GaitControl", "+"))
        self.label_22.setText(_translate("GaitControl", "Amplitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pipe), _translate("GaitControl", "Pipe-Crawling"))
        self.sinus_freq_label.setText(_translate("GaitControl", "0"))
        self.sinus_veramp_label.setText(_translate("GaitControl", "0"))
        self.sinus_freq_plus.setText(_translate("GaitControl", "+"))
        self.sinus_veramp_minus.setText(_translate("GaitControl", "-"))
        self.sinus_veramp_plus.setText(_translate("GaitControl", "+"))
        self.label_31.setText(_translate("GaitControl", "Frequency"))
        self.sinus_freq_minus.setText(_translate("GaitControl", "-"))
        self.label_33.setText(_translate("GaitControl", "Amplitude"))
        self.sinus_horamp_label.setText(_translate("GaitControl", "0"))
        self.sinus_horamp_minus.setText(_translate("GaitControl", "-"))
        self.sinus_horamp_plus.setText(_translate("GaitControl", "+"))
        self.label_36.setText(_translate("GaitControl", "Amplitude"))
        self.label_37.setText(_translate("GaitControl", "Vertical"))
        self.label_38.setText(_translate("GaitControl", "Horizontal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sinuslifting), _translate("GaitControl", "Sinuslifting"))
        self.rot_veramp_label.setText(_translate("GaitControl", "0"))
        self.rot_freq_plus.setText(_translate("GaitControl", "+"))
        self.rot_veramp_minus.setText(_translate("GaitControl", "-"))
        self.rot_veramp_plus.setText(_translate("GaitControl", "+"))
        self.rot_freq_label.setText(_translate("GaitControl", "0"))
        self.label_41.setText(_translate("GaitControl", "Vertical"))
        self.label_42.setText(_translate("GaitControl", "Frequency"))
        self.rot_horamp_plus.setText(_translate("GaitControl", "+"))
        self.label_43.setText(_translate("GaitControl", "Horizontal"))
        self.rot_freq_minus.setText(_translate("GaitControl", "-"))
        self.label_44.setText(_translate("GaitControl", "Amplitude"))
        self.rot_horamp_label.setText(_translate("GaitControl", "0"))
        self.rot_horamp_minus.setText(_translate("GaitControl", "-"))
        self.label_46.setText(_translate("GaitControl", "Amplitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Rotating), _translate("GaitControl", "Rotating"))
        self.apply.setText(_translate("GaitControl", "Apply"))
        self.quit.setText(_translate("GaitControl", "Quit"))
        self.stretch.setText(_translate("GaitControl", "Stretch"))
        self.Reset.setText(_translate("GaitControl", "Reset"))

    def functions(self, GaitControl):
        ## Widget
        self.quit.clicked.connect(self.quit_button)
        self.Reset.clicked.connect(self.reset_button)
        self.apply.clicked.connect(self.current_idx)
        self.tabWidget.currentChanged.connect(self.current_idx)

    def rol_freq_setNum(self, value):
        self.rolling_freq_label.setNum(value * frequency_gain)

    def side_freq_setNum(self, value):
        self.side_freq_label.setNum(value * frequency_gain)

    def ver_freq_setNum(self, value):
        self.ver_freq_label.setNum(value * frequency_gain)

    def pipe_freq_setNum(self, value):
        self.pipe_freq_label.setNum(value * frequency_gain)

    def sinus_freq_setNum(self, value):
        self.sinus_freq_label.setNum(value * frequency_gain)

    def rot_freq_setNum(self, value):
        self.rot_freq_label.setNum(value * frequency_gain)

    def pipe_nu_setNum(self, value):
        self.pipe_nu_label.setNum(value * nu_gain)

    def pipe_phi_setNum(self, value):
        self.pipe_phi_label.setNum(value * phi_gain)


    def buttonUi(self, GaitControl):
        self.rolling_amp_plus.clicked.connect(self.amp_plus)
        self.side_amp_plus.clicked.connect(self.amp_plus)
        self.ver_amp_plus.clicked.connect(self.amp_plus)
        self.pipe_amp_plus.clicked.connect(self.amp_plus)
        self.sinus_veramp_plus.clicked.connect(self.amp_plus)
        self.rot_veramp_plus.clicked.connect(self.amp_plus)

        self.rolling_amp_minus.clicked.connect(self.amp_minus)
        self.side_amp_minus.clicked.connect(self.amp_minus)
        self.ver_amp_minus.clicked.connect(self.amp_minus)
        self.pipe_amp_minus.clicked.connect(self.amp_minus)
        self.sinus_veramp_minus.clicked.connect(self.amp_minus)
        self.rot_veramp_minus.clicked.connect(self.amp_minus)

        self.sinus_horamp_plus.clicked.connect(self.hor_amp_plus)
        self.rot_horamp_plus.clicked.connect(self.hor_amp_plus)

        self.sinus_horamp_minus.clicked.connect(self.hor_amp_minus)
        self.rot_horamp_minus.clicked.connect(self.hor_amp_minus)

        self.rolling_freq_plus.clicked.connect(self.freq_plus)
        self.side_freq_plus.clicked.connect(self.freq_plus)
        self.ver_freq_plus.clicked.connect(self.freq_plus)
        self.pipe_freq_plus.clicked.connect(self.freq_plus)
        self.sinus_freq_plus.clicked.connect(self.freq_plus)
        self.rot_freq_plus.clicked.connect(self.freq_plus)

        self.rolling_freq_minus.clicked.connect(self.freq_minus)
        self.side_freq_minus.clicked.connect(self.freq_minus)
        self.ver_freq_minus.clicked.connect(self.freq_minus)
        self.pipe_freq_minus.clicked.connect(self.freq_minus)
        self.sinus_freq_minus.clicked.connect(self.freq_minus)
        self.rot_freq_minus.clicked.connect(self.freq_minus)

        self.pipe_phi_plus.clicked.connect(self.phi_plus)

        self.pipe_phi_minus.clicked.connect(self.phi_minus)

        self.pipe_nu_plus.clicked.connect(self.nu_plus)

        self.pipe_nu_minus.clicked.connect(self.nu_minus)

## Plus and minus button
    def amp_plus(self):
        global amplitude
        temp_amp = amplitude / amplitude_gain
        if temp_amp < 20:
            amplitude = (temp_amp+1)*amplitude_gain
        self.rolling_amp.setValue(amplitude)
        self.side_amp.setValue(amplitude)
        self.ver_amp.setValue(amplitude)
        self.pipe_amp.setValue(amplitude)
        self.sinus_veramp.setValue(amplitude)
        self.rot_veramp.setValue(amplitude)

    def amp_minus(self):
        global amplitude
        temp_amp = amplitude / amplitude_gain
        if int(temp_amp) > 0:
            amplitude = (temp_amp-1)*amplitude_gain
        self.rolling_amp.setValue(amplitude)
        self.side_amp.setValue(amplitude)
        self.ver_amp.setValue(amplitude)
        self.pipe_amp.setValue(amplitude)
        self.sinus_veramp.setValue(amplitude)
        self.rot_veramp.setValue(amplitude)

    def hor_amp_plus(self):
        global hor_amplitude
        temp_amp = hor_amplitude / amplitude_gain
        if temp_amp < 20:
            hor_amplitude = (temp_amp+1)*amplitude_gain
        self.sinus_horamp.setValue(hor_amplitude)
        self.rot_horamp.setValue(hor_amplitude)

    def hor_amp_minus(self):
        global hor_amplitude
        temp_amp = hor_amplitude / amplitude_gain
        if int(temp_amp) > 0:
            hor_amplitude = (temp_amp-1)*amplitude_gain
        self.sinus_horamp.setValue(hor_amplitude)
        self.rot_horamp.setValue(hor_amplitude)

    def freq_plus(self):
        global frequency
        temp_freq = frequency / frequency_gain
        if temp_freq < 20:
            frequency = (temp_freq+1)*frequency_gain
        self.rolling_freq.setValue(frequency/frequency_gain)
        self.side_freq.setValue(frequency/frequency_gain)
        self.ver_freq.setValue(frequency/frequency_gain)
        self.pipe_freq.setValue(frequency/frequency_gain)
        self.sinus_freq.setValue(frequency/frequency_gain)
        self.rot_freq.setValue(frequency/frequency_gain)

    def freq_minus(self):
        global frequency
        temp_freq = frequency / frequency_gain
        if int(temp_freq) > 0:
            frequency = (temp_freq-1)*frequency_gain
        self.rolling_freq.setValue(frequency/frequency_gain)
        self.side_freq.setValue(frequency/frequency_gain)
        self.ver_freq.setValue(frequency/frequency_gain)
        self.pipe_freq.setValue(frequency/frequency_gain)
        self.sinus_freq.setValue(frequency/frequency_gain)
        self.rot_freq.setValue(frequency/frequency_gain)

    def phi_plus(self):
        global phi
        temp_phi = phi / phi_gain
        if temp_phi < 20:
            phi = (temp_phi+1)*phi_gain
        self.pipe_phi.setValue(phi/phi_gain)

    def phi_minus(self):
        global phi
        temp_phi = phi / phi_gain
        if temp_phi > 0:
            phi = (temp_phi-1)*phi_gain
        self.pipe_phi.setValue(phi/phi_gain)

    def nu_plus(self):
        global nu
        temp_nu = nu / nu_gain
        if temp_nu < 20:
            nu = (temp_nu+1)*nu_gain
        self.pipe_nu.setValue(nu/nu_gain)

    def nu_minus(self):
        global nu
        temp_nu = nu / nu_gain
        if temp_nu > 0:
            nu = (temp_nu-1)*nu_gain
        self.pipe_nu.setValue(nu/nu_gain)
        print(nu_gain)




    def quit_button(self):
        QtCore.QCoreApplication.instance().quit()
        rospy.signal_shutdown("Quit the slider")

    def current_idx(self):
        global amplitude, frequency, hor_amplitude, phi, nu, gait
        idx = self.tabWidget.currentIndex()
        if idx == 0:
            gait = "Rolling"
        elif idx == 1:
            gait = "Sidewinding"
        elif idx == 2:
            gait = "Vertical"
        elif idx == 3:
            gait = "Pipe-Crawling"
        elif idx == 4:
            gait = "Sinuslifting"
        elif idx == 5:
            gait = "Rotating"
        else:
            gait = "None"
        self.rolling_amp.setValue(amplitude)
        self.rolling_freq.setValue(frequency/frequency_gain)
        self.side_amp.setValue(amplitude)
        self.side_freq.setValue(frequency/frequency_gain)
        self.ver_amp.setValue(amplitude)
        self.ver_freq.setValue(frequency/frequency_gain)
        self.pipe_amp.setValue(amplitude)
        self.pipe_freq.setValue(frequency/frequency_gain)
        self.pipe_phi.setValue(phi/phi_gain)
        self.pipe_nu.setValue(nu/nu_gain)
        self.sinus_veramp.setValue(amplitude)
        self.sinus_horamp.setValue(hor_amplitude)
        self.sinus_freq.setValue(frequency/frequency_gain)
        self.rot_veramp.setValue(amplitude)
        self.rot_horamp.setValue(hor_amplitude)
        self.rot_freq.setValue(frequency/frequency_gain)

    def reset_button(self):
        global amplitude, frequency, hor_amplitude, phi, nu, gait
        gait = "None"
        amplitude = 0
        frequency = 0
        hor_amplitude = 0
        phi = 0
        nu = 0
        self.rolling_amp.setValue(0)
        self.rolling_freq.setValue(0)
        self.side_amp.setValue(0)
        self.side_freq.setValue(0)
        self.ver_amp.setValue(0)
        self.ver_freq.setValue(0)
        self.pipe_amp.setValue(0)
        self.pipe_freq.setValue(0)
        self.pipe_phi.setValue(0)
        self.pipe_nu.setValue(0)
        self.sinus_veramp.setValue(0)
        self.sinus_horamp.setValue(0)
        self.sinus_freq.setValue(0)
        self.rot_veramp.setValue(0)
        self.rot_horamp.setValue(0)
        self.rot_freq.setValue(0)


    def update_amp(self, value):
        global amplitude
        amplitude = value

    def update_freq(self, value):
        global frequency
        frequency = value * frequency_gain

    def update_hor_amp(self, value):
        global hor_amplitude
        hor_amplitude = value

    def update_phi(self, value):
        global phi
        phi = value * phi_gain

    def update_nu(self, value):
        global nu
        nu = value * nu_gain

def talker():
    pub = rospy.Publisher('gait_param', gaitparam, queue_size=10)
    while not rospy.is_shutdown():
        global amplitude, frequency, hor_amplitude, phi, nu, gait
        params = gaitparam()
        params.amp = float(amplitude)
        params.freq = float(frequency)
        params.hor_amp = float(hor_amplitude)
        params.phi = float(phi)
        params.nu = float(nu)
        params.gait = gait
        pub.publish(params)
        rospy.sleep(0.1)

def talker_thread():
    print('Start to publish Amplitude to ROS core...')
    t_thread = threading.Thread(target = talker)
    t_thread.start()

if __name__ == "__main__":
    import sys
    rospy.init_node('gaitparam_talker')
    talker_thread()
    app = QtWidgets.QApplication(sys.argv)
    GaitControl = QtWidgets.QDockWidget()
    ui = Ui_GaitControl()
    ui.setupUi(GaitControl)
    GaitControl.show()
    sys.exit(app.exec_())
    rospy.signal_shutdown("Quit the slider")
