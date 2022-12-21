# Import Libraries
import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QHeaderView, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize, QAbstractAnimation
from PyQt5.QtGui import *
from PyQt5 import uic, QtWidgets


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Carregando a janela .ui
        self.janela = uic.loadUi(r'C:\Users\Vinicius\PycharmProjects\TCC\03_MVC\View_V2.ui', self)

        # Define os Widgets
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.central_window = self.findChild(QFrame, "Central_Side_Pages")
        self.button_home = self.findChild(QPushButton, "Button_Hamburguer")
        self.button_modtar = self.findChild(QPushButton, "Button_ModTar")
        self.button_resultados = self.findChild(QPushButton, "Button_Resultado")
        self.button_settings = self.findChild(QPushButton, "Button_Settings")
        self.button_consatual = self.findChild(QPushButton, "Button_ConsumoAtual")
        self.botoes = [self.button_consatual, self.button_home, self.button_modtar, self.button_settings, self.button_resultados]
        self.nome_botoes = ["Consumo Atual", "Menu", "Modalidade Tarifária", "Configurações", "Resultados"]

        # Configuração dos Botões
        self.bt_home()
        self.bt_modtarifario()
        self.bt_resultado()
        self.bt_settings()
        self.bt_consatual()

        # Tela e Botão de Inicialização
        self.stackedWidget.setCurrentIndex(4)
        self.button_home.setFocus()

    def menu_hamburguer(self):
        #self.button_home.clearFocus()
        width = self.button_home.width()
        botao = 0

        if width == 50: self.menu_hamburguer_max()

        else: self.menu_hamburguer_min()

    def menu_hamburguer_max(self):
        newWidth = 150
        newIconsize = QSize(100, 100)
        for i, botao in enumerate(self.botoes):
            botao.setFixedWidth(newWidth)
            botao.setIconSize(newIconsize)
            botao.setText(self.nome_botoes[i])
            self.button_home.setIcon(QIcon(r"C:\Users\Vinicius\PycharmProjects\TCC\02_Image\cil-arrow-left.png"))
        self.central_window.setGeometry(150, 0, 640, 386)

    def menu_hamburguer_min(self):
        newWidth = 50
        newIconsize = QSize(100, 100)

        for i, botao in enumerate(self.botoes):
            botao.setFixedWidth(newWidth)
            botao.setIconSize(newIconsize)
            botao.setText("")
            botao.setToolTip(f"{self.nome_botoes[i]}")
            self.button_home.setIcon(QIcon(r"C:\Users\Vinicius\PycharmProjects\TCC\02_Image\cil-arrow-right.png"))
        self.central_window.setGeometry(50, 0, 740, 386)

    def bt_modtarifario(self):
        self.button_modtar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def bt_resultado(self):
        self.button_resultados.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def bt_settings(self):
        self.button_settings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

    def bt_home(self):
        self.button_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

    def bt_consatual(self):
        self.button_consatual.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_window = Main()
    ui_window.show()
    sys.exit(app.exec_())
