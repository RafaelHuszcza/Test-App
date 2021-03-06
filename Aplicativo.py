# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aplicativo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(589, 317)
        self.centralwidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(False)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        JanelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JanelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu_Principal = QtWidgets.QMenu(self.menubar)
        self.menuMenu_Principal.setObjectName("menuMenu_Principal")
        JanelaPrincipal.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(JanelaPrincipal)
        self.actionSair.setObjectName("actionSair")
        self.actionAbrir = QtWidgets.QAction(JanelaPrincipal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSobre = QtWidgets.QAction(JanelaPrincipal)
        self.actionSobre.setObjectName("actionSobre")
        self.menuMenu_Principal.addAction(self.actionSair)
        self.menuMenu_Principal.addAction(self.actionAbrir)
        self.menuMenu_Principal.addAction(self.actionSobre)
        self.menubar.addAction(self.menuMenu_Principal.menuAction())

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "MainWindow"))
        self.label_2.setText(_translate("JanelaPrincipal", "Polinomio Gerado"))
        self.label.setText(_translate("JanelaPrincipal", "TextLabel"))
        self.menuMenu_Principal.setTitle(_translate("JanelaPrincipal", "Menu Principal"))
        self.actionSair.setText(_translate("JanelaPrincipal", "Sair"))
        self.actionAbrir.setText(_translate("JanelaPrincipal", "Abrir"))
        self.actionSobre.setText(_translate("JanelaPrincipal", "Sobre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(JanelaPrincipal)
    JanelaPrincipal.show()
    sys.exit(app.exec_())
