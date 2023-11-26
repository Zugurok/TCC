import os
import sys

from ui_teste import Ui_MainWindow

from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtChart import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Main(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super(Main, self).__init__()
        #Definindo variáveis fundamentais
        self.historico = []
        self.tarifas = []
        #self.modtar = QComboBox
        self.meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        #self.graphics = Graphics(self.historico, self.tarifas)
        

        # Importar o arquivo .ui
        loadUi(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\teste_V3.ui", self)

        # Definindo a tela principal
        self.reg_historico()

        # Definir o tamanho minimo da tela
        #self.setSizePolicy(1800, 800)
        self.setMinimumSize(1920, 1080)

        # Retirar Window Flag da pagina
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
        #Definindo Conexão as telas do stackedWidget
        self.pushButton_0.clicked.connect(lambda: self.reg_historico())
        self.pushButton_1.clicked.connect(lambda: self.reg_tarifas())
        self.pushButton_2.clicked.connect(lambda: self.comp_economica())
        self.pushButton_3.clicked.connect(lambda: self.graficos())

        # Aplicando o funcionamento dos botões nav
        self.window_flag()

        self.show()
        
    def window_flag(self):
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())
        self.pushButton_8.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\Icons\minus_disabled.png"))
        
        self.pushButton_7.clicked.connect(lambda: self.bt_maximize())
        self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\Icons\maximize-2_disabled.png"))
        
        self.pushButton_9.clicked.connect(lambda: self.close())
        self.pushButton_9.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\Icons\x_disabled.png"))

    def bt_maximize(self):
        if ui_window.isMaximized() == True:
            self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\Icons\maximize-2_disabled.png"))
            self.showNormal()

        elif ui_window.isMaximized() == False:
            self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_MVC\teste\Icons\minimize-2_disabled.png"))
            self.showMaximized()

    def reg_historico(self):
        self.stackedWidget.setCurrentIndex(0)
        self.label_9.setText("Registre o Histórico da UC")

        subgrupo = getattr(self, "comboBox", None)
        modtar = getattr(self, "comboBox_2", None)
        
        subgrupo.currentIndexChanged.connect(lambda: self.update_subgrupo())
        modtar.currentIndexChanged.connect(lambda: self.update_modtar())
        self.pushButton_5.clicked.connect(lambda: self.att_historico())

    def update_subgrupo(self):
        subgrupo = getattr(self, "comboBox", None)
        modtar = getattr(self, "comboBox_2", None)
        condicional_modtar = {"A1 (≥ 230 kV)": ["Horo-sazonal Azul"], "A2 (88 kV a 138 kV)": ["Horo-sazonal Azul"], "A3 (69 kV)": ["Horo-sazonal Azul"], 
                              "A3a (30 kV a 44 kV)": ["Horo-sazonal Azul", "Horo-sazonal Verde", "Convencional Binômia"], 
                              "A4 (2.3 a 25 kV)": ["Horo-sazonal Azul", "Horo-sazonal Verde", "Convencional Binômia"], 
                              "AS (≤ 2.3 kV subterrâneo)": ["Horo-sazonal Azul", "Horo-sazonal Verde", "Convencional Binômia"]}
        modtar.clear()
        current_selection = subgrupo.currentText()

        for item in condicional_modtar[current_selection]:
            modtar.addItem(item)

    def update_modtar(self):
        self.modtar = getattr(self, "comboBox_2", None).currentText()

        if self.modtar == "Horo-sazonal Verde":
            getattr(self, "doubleSpinBox_30", None).setEnabled(False) # Demanda Medida Janeiro
            getattr(self, "doubleSpinBox_29", None).setEnabled(False)
            getattr(self, "doubleSpinBox_22", None).setEnabled(False)
            getattr(self, "doubleSpinBox_37", None).setEnabled(False)
            getattr(self, "doubleSpinBox_34", None).setEnabled(False)
            getattr(self, "doubleSpinBox_28", None).setEnabled(False)
            getattr(self, "doubleSpinBox_36", None).setEnabled(False)
            getattr(self, "doubleSpinBox_31", None).setEnabled(False)
            getattr(self, "doubleSpinBox_35", None).setEnabled(False)
            getattr(self, "doubleSpinBox_33", None).setEnabled(False)
            getattr(self, "doubleSpinBox_21", None).setEnabled(False)
            getattr(self, "doubleSpinBox_32", None).setEnabled(False) # Demanda Medida Dezembro
            getattr(self, "SpinBox_DCp_18", None).setEnabled(False) # Demanda Contratada Ponta
        
        elif self.modtar == "Convencional Binômia":
            getattr(self, "doubleSpinBox_30", None).setEnabled(False) # DemandaP Medida Janeiro
            getattr(self, "doubleSpinBox_29", None).setEnabled(False)
            getattr(self, "doubleSpinBox_22", None).setEnabled(False)
            getattr(self, "doubleSpinBox_37", None).setEnabled(False)
            getattr(self, "doubleSpinBox_34", None).setEnabled(False)
            getattr(self, "doubleSpinBox_28", None).setEnabled(False)
            getattr(self, "doubleSpinBox_36", None).setEnabled(False)
            getattr(self, "doubleSpinBox_31", None).setEnabled(False)
            getattr(self, "doubleSpinBox_35", None).setEnabled(False)
            getattr(self, "doubleSpinBox_33", None).setEnabled(False)
            getattr(self, "doubleSpinBox_21", None).setEnabled(False)
            getattr(self, "doubleSpinBox_32", None).setEnabled(False) # Demanda Medida Dezembro
            getattr(self, "SpinBox_DCp_18", None).setEnabled(False) # Demanda Contratada Ponta

            getattr(self, "doubleSpinBox_51", None).setEnabled(False) # ConsumoP Janeiro
            getattr(self, "doubleSpinBox_60", None).setEnabled(False)
            getattr(self, "doubleSpinBox_58", None).setEnabled(False)
            getattr(self, "doubleSpinBox_55", None).setEnabled(False)
            getattr(self, "doubleSpinBox_47", None).setEnabled(False)
            getattr(self, "doubleSpinBox_49", None).setEnabled(False)
            getattr(self, "doubleSpinBox_41", None).setEnabled(False)
            getattr(self, "doubleSpinBox_43", None).setEnabled(False)
            getattr(self, "doubleSpinBox_59", None).setEnabled(False)
            getattr(self, "doubleSpinBox_46", None).setEnabled(False)
            getattr(self, "doubleSpinBox_50", None).setEnabled(False)
            getattr(self, "doubleSpinBox_53", None).setEnabled(False) # ConsumoP Dezembro

    def att_historico(self):
        demContratada_fp = getattr(self, "SpinBox_DCp_17", None).value()
        demContratada_p = getattr(self, "SpinBox_DCp_18", None).value()
        modtar = getattr(self, "comboBox_2", None).currentText()

        dem_jan_fp = getattr(self, "doubleSpinBox", None).value()
        dem_fev_fp = getattr(self, "doubleSpinBox_2", None).value()
        dem_mar_fp = getattr(self, "doubleSpinBox_3", None).value()
        dem_apr_fp = getattr(self, "doubleSpinBox_4", None).value()
        dem_mai_fp = getattr(self, "doubleSpinBox_5", None).value()
        dem_jun_fp = getattr(self, "doubleSpinBox_17", None).value()
        dem_jul_fp = getattr(self, "doubleSpinBox_15", None).value()
        dem_ago_fp = getattr(self, "doubleSpinBox_6", None).value()
        dem_set_fp = getattr(self, "doubleSpinBox_13", None).value()
        dem_out_fp = getattr(self, "doubleSpinBox_7", None).value()
        dem_nov_fp = getattr(self, "doubleSpinBox_20", None).value()
        dem_dez_fp = getattr(self, "doubleSpinBox_19", None).value()
        demMed_fp = [dem_jan_fp, dem_fev_fp, dem_mar_fp, 
                    dem_apr_fp, dem_mai_fp, dem_jun_fp,
                    dem_jul_fp, dem_ago_fp, dem_set_fp,
                    dem_out_fp, dem_nov_fp, dem_dez_fp]

        dem_jan_p = getattr(self, "doubleSpinBox_30", None).value()
        dem_fev_p = getattr(self, "doubleSpinBox_29", None).value()
        dem_mar_p = getattr(self, "doubleSpinBox_22", None).value()
        dem_apr_p = getattr(self, "doubleSpinBox_37", None).value()
        dem_mai_p = getattr(self, "doubleSpinBox_34", None).value()
        dem_jun_p = getattr(self, "doubleSpinBox_28", None).value()
        dem_jul_p = getattr(self, "doubleSpinBox_36", None).value()
        dem_ago_p = getattr(self, "doubleSpinBox_31", None).value()
        dem_set_p = getattr(self, "doubleSpinBox_35", None).value()
        dem_out_p = getattr(self, "doubleSpinBox_33", None).value()
        dem_nov_p = getattr(self, "doubleSpinBox_21", None).value()
        dem_dez_p = getattr(self, "doubleSpinBox_32", None).value()
        demMed_p = [dem_jan_p, dem_fev_p, dem_mar_p, 
                    dem_apr_p, dem_mai_p, dem_jun_p,
                    dem_jul_p, dem_ago_p, dem_set_p,
                    dem_out_p, dem_nov_p, dem_dez_p]

        cons_jan_fp = getattr(self, "doubleSpinBox_52", None).value()
        cons_fev_fp = getattr(self, "doubleSpinBox_56", None).value()
        cons_mar_fp = getattr(self, "doubleSpinBox_57", None).value()
        cons_apr_fp = getattr(self, "doubleSpinBox_48", None).value()
        cons_mai_fp = getattr(self, "doubleSpinBox_54", None).value()
        cons_jun_fp = getattr(self, "doubleSpinBox_45", None).value()
        cons_jul_fp = getattr(self, "doubleSpinBox_39", None).value()
        cons_ago_fp = getattr(self, "doubleSpinBox_38", None).value()
        cons_set_fp = getattr(self, "doubleSpinBox_44", None).value()
        cons_out_fp = getattr(self, "doubleSpinBox_42", None).value()
        cons_nov_fp = getattr(self, "doubleSpinBox_61", None).value()
        cons_dez_fp = getattr(self, "doubleSpinBox_40", None).value()
        consFP = [cons_jan_fp, cons_fev_fp, cons_mar_fp, cons_apr_fp, 
                  cons_mai_fp, cons_jun_fp, cons_jul_fp, cons_ago_fp, 
                  cons_set_fp, cons_out_fp, cons_nov_fp, cons_dez_fp]
        
        cons_jan_p = getattr(self, "doubleSpinBox_51", None).value()
        cons_fev_p = getattr(self, "doubleSpinBox_60", None).value()
        cons_mar_p = getattr(self, "doubleSpinBox_58", None).value()
        cons_apr_p = getattr(self, "doubleSpinBox_55", None).value()
        cons_mai_p = getattr(self, "doubleSpinBox_47", None).value()
        cons_jun_p = getattr(self, "doubleSpinBox_49", None).value()
        cons_jul_p = getattr(self, "doubleSpinBox_41", None).value()
        cons_ago_p = getattr(self, "doubleSpinBox_43", None).value()
        cons_set_p = getattr(self, "doubleSpinBox_59", None).value()
        cons_out_p = getattr(self, "doubleSpinBox_46", None).value()
        cons_nov_p = getattr(self, "doubleSpinBox_50", None).value()
        cons_dez_p = getattr(self, "doubleSpinBox_53", None).value()
        consP = [cons_jan_p, cons_fev_p, cons_mar_p, cons_apr_p, 
                 cons_mai_p, cons_jun_p, cons_jul_p, cons_ago_p, 
                 cons_set_p, cons_out_p, cons_nov_p, cons_dez_p]

        historico = []
        historico.append(demMed_fp)
        historico.append(demMed_p)
        historico.append(consFP)
        historico.append(consP)
        historico.append(demContratada_fp)
        historico.append(demContratada_p)
        historico.append(modtar)
        
        return historico

    def reg_tarifas(self):
        self.stackedWidget.setCurrentIndex(1)
        self.label_9.setText("Registre as tarifas")
        self.pushButton.clicked.connect(lambda: self.att_tarifas())
        
    def att_tarifas(self):
        tar_dem_azul_ci_fp = getattr(self, "doubleSpinBox_9", None).value()
        tar_dem_azul_si_fp = getattr(self, "doubleSpinBox_11", None).value()
        tar_dem_azul_ci_p = getattr(self, "doubleSpinBox_10", None).value()
        tar_dem_azul_si_p = getattr(self, "doubleSpinBox_12", None).value()
        tar_cons_azul_fp = getattr(self, "doubleSpinBox_25", None).value()
        tar_cons_azul_p = getattr(self, "doubleSpinBox_26", None).value()
        
        tarifas_azul_si = [tar_dem_azul_si_fp, tar_dem_azul_si_p, tar_cons_azul_fp, tar_cons_azul_p]
        tarifas_azul_ci = [tar_dem_azul_ci_fp, tar_dem_azul_ci_p, tar_cons_azul_fp, tar_cons_azul_p]
        tarifas_azul = [tarifas_azul_si, tarifas_azul_ci]

        tar_dem_verde_ci = getattr(self, "doubleSpinBox_14", None).value()
        tar_dem_verde_si = getattr(self, "doubleSpinBox_8", None).value()
        tar_cons_verde_fp = getattr(self, "doubleSpinBox_24", None).value()
        tar_cons_verde_p = getattr(self, "doubleSpinBox_23", None).value()

        tarifas_verde_si = [tar_dem_verde_si, tar_cons_verde_fp, tar_cons_verde_p]
        tarifas_verde_ci = [tar_dem_verde_ci, tar_cons_verde_fp, tar_cons_verde_p]
        tarifas_verde = [tarifas_verde_si, tarifas_verde_ci]

        tar_dem_convencional_ci = getattr(self, "doubleSpinBox_14", None).value()
        tar_dem_convencional_si = getattr(self, "doubleSpinBox_8", None).value()
        tar_cons_convencional = getattr(self, "doubleSpinBox_24", None).value()

        tarifas_convencional_si = [tar_dem_convencional_si, tar_cons_convencional]
        tarifas_convencional_ci = [tar_dem_convencional_ci, tar_cons_convencional]
        tarifas_convencional = [tarifas_convencional_si, tarifas_convencional_ci]

        tarifas = []
        tarifas.append(tarifas_azul)
        tarifas.append(tarifas_verde)
        tarifas.append(tarifas_convencional)

        return tarifas
    
    def comp_economica(self):
        self.stackedWidget.setCurrentIndex(2)
        self.label_9.setText("Comparação Econômica")

    def graficos(self):
        self.stackedWidget.setCurrentIndex(3)
        self.label_9.setText("Resultados Gráficos")
        historico = self.att_historico()
        
        # Demanda Contratada
        
        # Exibir os gráficos
        # Demanda Medida Atual
        #self.graph_demMed()
        # Demanda Medida Ajustada
        self.graph_demMed_Ajustado()
        

        # Fechar o Canva após gerar os gráficos
        for i in reversed(range(self.verticalLayout_8.count())):
            self.canvas_demMedAtual = self.verticalLayout_8.itemAt(i).widget()
            self.verticalLayout_8.removeWidget(self.canvas_demMedAtual)

    def graph_demMed(self):
        # Criar a imagem
        self.figure_demMedAtual = plt.figure(figsize=(5.7, 4), dpi=90)
        self.canvas_demMedAtual = FigureCanvas(self.figure_demMedAtual)
        self.verticalLayout_8.addWidget(self.canvas_demMedAtual)

        # Inserir o histórico
        historico = self.att_historico()
        modtar = historico[6]

        if modtar == "Horo-sazonal Verde":
            self.demMed_Verde()
            self.label_28.setText(str(historico[4])+str(" kW"))
        
        elif modtar == "Horo-sazonal Azul":
            self.demMed_Azul()
            self.label_28.setText(str("FP: ")+str(historico[4])+str(" kW\n")+str("P:  ")+str(historico[5])+str(" kW"))
            self.label_28.setAlignment(Qt.AlignLeft)
            

        elif modtar == "Convencional Binômia":
            self.demMed_Convencional()
            self.label_28.setText(str(historico[4])+str(" kW"))

        plt.title("Histórico Demanda Medida Atual (kW)")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')

    def demMed_Verde(self):
        self.figure_demMedAtual.clear()
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_dc = [demContratada_fp] * 12
        tolerancia = demContratada_fp * 1.05
        barWidth = 0.4
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # Make the plot
        plt.bar(x_axis - 0.2, demMed_fp, color="blue", label="DM FP", width=barWidth)
        #plt.bar(x_axis + 0.2, dem_medida_p, color="green", label="DM P", width=barWidth)
        plt.hlines(y=lista_dc, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC: {demContratada_fp}")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia}")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        
        self.canvas_demMedAtual.draw()

    def demMed_Azul(self):
        self.figure_demMedAtual.clear()
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_dc_fp = [demContratada_fp] * 12
        tolerancia_fp = demContratada_fp * 1.05
        lista_dc_p = [demContratada_p] * 12
        tolerancia_p = demContratada_p * 1.05
        barWidth = 0.4

        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))

        # Make the plot
        plt.bar(x_axis - 0.2, demMed_fp, color="blue", label="DM FP", width=barWidth)  # DM FP
        plt.bar(x_axis + 0.2, demMed_p, color="green", label="DM P", width=barWidth)  # DM P
        # Fora de Ponta
        plt.hlines(y=lista_dc_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC FP: {demContratada_fp}")  # DC FP
        plt.hlines(y=tolerancia_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância FPonta: {tolerancia_fp}")  # LimTol FP
        # Ponta
        plt.hlines(y=lista_dc_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"DC P: {demContratada_p}")  # DC P
        plt.hlines(y=tolerancia_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='solid',
                   label=f"Tolerância Ponta: {tolerancia_p}")  # LimTol P
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demMedAtual.draw()

    def demMed_Convencional(self):
        self.figure_demMedAtual.clear()
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_dc = [demContratada_fp] * 12
        tolerancia = demContratada_fp * 1.05
        barWidth = 0.4

        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))

        # Make the plot
        plt.bar(x_axis - 0.2, demMed_fp, color="blue", label="DM FP", width=barWidth)
        #plt.bar(x_axis + 0.2, demMed_p, color="green", label="DM P", width=barWidth)
        plt.hlines(y=lista_dc, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC: {float(demContratada_fp)}")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia}")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demMedAtual.draw()

    def demFaturada(self, dem_medida: list, dem_cont: int):
        """

        :param dem_medida:
        :param dem_cont:
        :return:
        """
        tolerancia = dem_cont * 1.05
        lista_tolerancia = [0] * 12
        lista_sobra = [0] * 12
        lista_ultrapassagem = [0] * 12
        dem_medida_sup = dem_medida

        for i in range(0, 12):
            if dem_medida_sup[i] <= dem_cont:
                lista_sobra[i] = dem_cont - dem_medida_sup[i]

            if (dem_medida_sup[i] <= tolerancia) and (dem_medida_sup[i] > dem_cont):
                lista_tolerancia[i] = dem_medida_sup[i] - dem_cont

            if dem_medida_sup[i] > tolerancia:
                lista_ultrapassagem[i] = ((dem_medida_sup[i] - dem_cont) * 2)
                dem_medida_sup[i] = dem_cont

        return lista_ultrapassagem, lista_tolerancia, lista_sobra, dem_medida_sup

    def graph_demMed_Ajustado(self):
        # Criar a imagem
        self.figure_demMedAjustado = plt.figure(figsize=(5.7, 4), dpi=90)
        self.canvas_demMedAjustado = FigureCanvas(self.figure_demMedAjustado)
        self.verticalLayout_8.addWidget(self.canvas_demMedAjustado)

        # Inserir o histórico
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        
        
        if modtar == "Horo-sazonal Verde":
            self.demMed_Verde_Ajustado()
            self.label_28.setText(str(historico[4])+str(" kW"))
        
        elif modtar == "Horo-sazonal Azul":
            self.demMed_Azul_Ajustado()
            self.label_28.setText(str("FP: ")+str(historico[4])+str(" kW\n")+str("P:  ")+str(historico[5])+str(" kW"))
            self.label_28.setAlignment(Qt.AlignLeft)
            

        elif modtar == "Convencional Binômia":
            self.demMed_Convencional_Ajustado()
            self.label_28.setText(str(historico[4])+str(" kW"))

        plt.title("Histórico Demanda Medida Ajustado (kW)")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')

    def demMed_Verde_Ajustado(self):
        self.figure_demMedAjustado.clear()

        # Inserir o histórico
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_ultrapassagem, lista_tolerancia, lista_sobra, demanda_medida = self.demFaturada(demMed_fp, demContratada_fp)
        
        # Config Gráfico
        tolerancia = demContratada_fp * 1.05
        barWidth = 0.4
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot
        plt.bar(x_axis - 0.21, demanda_medida, color="blue", label="DM FPonta", width=barWidth, edgecolor='silver')
        plt.bar(x_axis - 0.21, lista_sobra, bottom=demanda_medida, color="gray", label="DS", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, lista_ultrapassagem, bottom=demanda_medida, color="red", label="DU",
                width=barWidth, edgecolor='silver')
        plt.hlines(y=demContratada_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC: {demContratada_fp} kW")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demMedAjustado.draw()

    def demMed_Azul_Ajustado(self):
        self.figure_demMedAjustado.clear()

        # Inserir o histórico
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_ultrapassagem_fp, lista_tolerancia_fp, lista_sobra_fp, demanda_medida_fp = self.demFaturada(demMed_fp, demContratada_fp)
        lista_ultrapassagem_p, lista_tolerancia_p, lista_sobra_p, demanda_medida_p = self.demFaturada(demMed_p, demContratada_p)
        # Config Gráfico
        tolerancia_fp = demContratada_fp * 1.05
        tolerancia_p = demContratada_p * 1.05
        barWidth = 0.3
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot
        # PLOT FORA DE PONTA
        plt.bar(x_axis - 0.21, demanda_medida_fp, color="blue", label="DM FPonta", width=barWidth, edgecolor='silver',
                capsize=7)
        plt.bar(x_axis - 0.21, lista_sobra_fp, bottom=demanda_medida_fp, color="gray", label="DS", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, lista_ultrapassagem_fp, bottom=demanda_medida_fp, color="red", label="DU", width=barWidth,
                edgecolor='silver')
        plt.hlines(y=demContratada_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC FP: {demContratada_fp} kW")
        plt.hlines(y=tolerancia_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância FPonta: {tolerancia_fp} kW")
        # PLOT PONTA
        plt.bar(x_axis + 0.21, demanda_medida_p, color="green", label="DM Ponta", width=barWidth, edgecolor='silver',
                capsize=7)
        plt.bar(x_axis + 0.21, lista_sobra_p, bottom=demanda_medida_p, color="gray", width=barWidth, edgecolor='silver')
        plt.bar(x_axis + 0.21, lista_ultrapassagem_p, bottom=demanda_medida_p, color="red", width=barWidth,
                edgecolor='silver')
        plt.hlines(y=demContratada_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"DC P: {demContratada_p} kW")
        plt.hlines(y=tolerancia_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='solid',
                   label=f"Tolerância Ponta: {tolerancia_p} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demMedAjustado.draw()

    def demMed_Convencional_Ajustado(self):
        self.figure_demMedAjustado.clear()

        # Inserir o histórico
        historico = self.att_historico()
        [demMed_fp, demMed_p, consFP, consP, 
         demContratada_fp, demContratada_p, modtar] = historico
        lista_ultrapassagem, lista_tolerancia, lista_sobra, demanda_medida = self.demFaturada(demMed_fp, demContratada_fp)
        
        # Config Gráfico
        tolerancia = demContratada_fp * 1.05
        barWidth = 0.4
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))

        # Make the plot
        plt.bar(x_axis, demanda_medida, color="blue", label="DM", width=barWidth, edgecolor='silver')
        plt.bar(x_axis, lista_sobra, bottom=demanda_medida, color="gray", label="DS", width=barWidth, edgecolor='silver')
        plt.bar(x_axis, lista_ultrapassagem, bottom=demanda_medida, color="red", label="DU", width=barWidth,
                edgecolor='silver')
        plt.hlines(y=demContratada_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC: {demContratada_fp} kW")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia: 2f} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        
        # Plotar o Gráfico
        self.canvas_demMedAjustado.draw()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_window = Main()
    ui_window.show()
    sys.exit(app.exec_())
