from PyQt6 import QtCore, QtGui, QtWidgets
import ui_files.resourcesFile


class UI_LogIn(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 421, 521))
        self.widget.setStyleSheet("QPushButton#pushButtonIngresar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop: 1     rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonIngresar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop: 1     rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#pushButtonIngresar:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButtonWhatsApp{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonWhatsApp:hover{\n"
"    color: rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#pushButtonWhatsApp:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    color: rgba(115, 128, 142, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonCloseLogIn{\n"
"    background-color: transparent;\n"
"    color: rgba(255, 255, 255, 210);\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonCloseLogIn:hover{\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButtonCloseLogIn:pressed{\n"
"    background-color: rgba(105, 118, 132, 150);\n"
"}\n"
"\n"
"QPushButton#pushButtonMinimizeLogIn{\n"
"    background-color: transparent;\n"
"    color: rgba(255, 255, 255, 210);\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonMinimizeLogIn:hover{\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButtonMinimizeLogIn:pressed{\n"
"    background-color: rgba(105, 118, 132, 150);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 420))
        self.label.setStyleSheet("border-image: url(:/images/background.png);    \n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 331, 420))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 311, 381))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(110, 80, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditUserName.setGeometry(QtCore.QRect(60, 150, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditUserName.setFont(font)
        self.lineEditUserName.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(150, 168, 182, 255);\n"
"padding-bottom: 7px;")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(60, 210, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(150, 168, 182, 255);\n"
"padding-bottom: 7px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonIngresar = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonIngresar.setGeometry(QtCore.QRect(100, 300, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonIngresar.setFont(font)
        self.pushButtonIngresar.setObjectName("pushButtonIngresar")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(80, 360, 241, 20))
        self.label_5.setStyleSheet("color: rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.pushButtonWhatsApp = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonWhatsApp.setGeometry(QtCore.QRect(70, 390, 35, 35))
        self.pushButtonWhatsApp.setMaximumSize(QtCore.QSize(35, 35))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.pushButtonWhatsApp.setFont(font)
        self.pushButtonWhatsApp.setObjectName("pushButtonWhatsApp")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(108, 396, 91, 20))
        self.label_6.setStyleSheet("color: rgba(255, 255, 255, 140);")
        self.label_6.setObjectName("label_6")
        self.pushButtonCloseLogIn = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonCloseLogIn.setGeometry(QtCore.QRect(310, 30, 26, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButtonCloseLogIn.setFont(font)
        self.pushButtonCloseLogIn.setAutoFillBackground(False)
        self.pushButtonCloseLogIn.setStyleSheet("")
        self.pushButtonCloseLogIn.setObjectName("pushButtonCloseLogIn")
        self.pushButtonMinimizeLogIn = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonMinimizeLogIn.setGeometry(QtCore.QRect(280, 30, 26, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.pushButtonMinimizeLogIn.setFont(font)
        self.pushButtonMinimizeLogIn.setAutoFillBackground(False)
        self.pushButtonMinimizeLogIn.setStyleSheet("")
        self.pushButtonMinimizeLogIn.setObjectName("pushButtonMinimizeLogIn")
        self.checkBoxShowPassword = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBoxShowPassword.setGeometry(QtCore.QRect(60, 260, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBoxShowPassword.setFont(font)
        self.checkBoxShowPassword.setStyleSheet("color: rgba(255, 255, 255, 140);")
        self.checkBoxShowPassword.setObjectName("checkBoxShowPassword")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(234, 221, 186, 100)))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Iniciar Sesión"))
        self.lineEditUserName.setText(_translate("Form", "Nombre de Usuario/Correo Institucional"))
        self.lineEditPassword.setText(_translate("Form", "Password"))
        self.pushButtonIngresar.setText(_translate("Form", "Ingresar"))
        self.label_5.setText(_translate("Form", "¿Olvidó su nombre de usuario o contraseña?"))
        self.pushButtonWhatsApp.setText(_translate("Form", "L"))
        self.label_6.setText(_translate("Form", "Contáctanos"))
        self.pushButtonCloseLogIn.setText(_translate("Form", "x"))
        self.pushButtonMinimizeLogIn.setText(_translate("Form", "-"))
        self.checkBoxShowPassword.setText(_translate("Form", "Mostrar contraseña"))
