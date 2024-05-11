from PyQt6 import QtCore, QtGui, QtWidgets
import ui_files.resourcesFile


class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color:#1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"    background-color:#16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-ledt-radius: 10px;\n"
"    border-bottom-left-raidus: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(parent=self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonMenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonMenu.setStyleSheet("")
        self.pushButtonMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMenu.setIcon(icon)
        self.pushButtonMenu.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonMenu.setObjectName("pushButtonMenu")
        self.horizontalLayout_2.addWidget(self.pushButtonMenu)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButtonInicio = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButtonInicio.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonInicio.setIcon(icon1)
        self.pushButtonInicio.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonInicio.setObjectName("pushButtonInicio")
        self.verticalLayout_4.addWidget(self.pushButtonInicio)
        self.pushButtonAsistencia = QtWidgets.QPushButton(parent=self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/user-check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAsistencia.setIcon(icon2)
        self.pushButtonAsistencia.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAsistencia.setObjectName("pushButtonAsistencia")
        self.verticalLayout_4.addWidget(self.pushButtonAsistencia)
        self.pushButtonReporte = QtWidgets.QPushButton(parent=self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReporte.setIcon(icon3)
        self.pushButtonReporte.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonReporte.setObjectName("pushButtonReporte")
        self.verticalLayout_4.addWidget(self.pushButtonReporte)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(parent=self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButtonConfiguracion = QtWidgets.QPushButton(parent=self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonConfiguracion.setIcon(icon4)
        self.pushButtonConfiguracion.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonConfiguracion.setObjectName("pushButtonConfiguracion")
        self.verticalLayout_5.addWidget(self.pushButtonConfiguracion)
        self.pushButtonInformacion = QtWidgets.QPushButton(parent=self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonInformacion.setIcon(icon5)
        self.pushButtonInformacion.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonInformacion.setObjectName("pushButtonInformacion")
        self.verticalLayout_5.addWidget(self.pushButtonInformacion)
        self.pushButtonAyuda = QtWidgets.QPushButton(parent=self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAyuda.setIcon(icon6)
        self.pushButtonAyuda.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonAyuda.setObjectName("pushButtonAyuda")
        self.verticalLayout_5.addWidget(self.pushButtonAyuda)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.leftMenuSubContainer)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.centerMenuContainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(parent=self.centerMenuContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("background-color: rgb(85, 85, 0);")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestión de Asistencia en Aula"))
        self.pushButtonMenu.setToolTip(_translate("MainWindow", "Menú"))
        self.pushButtonInicio.setToolTip(_translate("MainWindow", "Inicio"))
        self.pushButtonInicio.setText(_translate("MainWindow", "Inicio"))
        self.pushButtonAsistencia.setToolTip(_translate("MainWindow", "Tomar la asistencia"))
        self.pushButtonAsistencia.setText(_translate("MainWindow", "Asistencia"))
        self.pushButtonReporte.setToolTip(_translate("MainWindow", "Ver reporte de asistencia"))
        self.pushButtonReporte.setText(_translate("MainWindow", "Reporte"))
        self.pushButtonConfiguracion.setToolTip(_translate("MainWindow", "Ir a configuración"))
        self.pushButtonConfiguracion.setText(_translate("MainWindow", "Configuración"))
        self.pushButtonInformacion.setToolTip(_translate("MainWindow", "Ver información"))
        self.pushButtonInformacion.setText(_translate("MainWindow", "Información"))
        self.pushButtonAyuda.setToolTip(_translate("MainWindow", "Ver la ayuda"))
        self.pushButtonAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
