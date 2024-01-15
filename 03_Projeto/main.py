import os
import sys
from ui_projeto_V6 import Ui_MainWindow
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
#from PyQt5.QtChart import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
#import pandas as pd


class Main(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super(Main, self).__init__()
        #Definindo variáveis fundamentais
        self.historico = []
        self.tarifas = []
        self.meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        loadUi(r"C:\Users\Vinicius\Documents\GitHub\TCC\03_Projeto\Projeto_V6.ui", self)
        self.reg_historico()
        self.setMinimumSize(1920, 1080)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
        self.pushButton_0.clicked.connect(lambda: self.reg_historico())
        self.pushButton_5.clicked.connect(lambda: self.att_historico())
        self.pushButton_1.clicked.connect(lambda: self.reg_tarifas())
        self.pushButton_3.clicked.connect(lambda: self.comparacao_economica())
        self.window_flag()
        self.show()
        
    def window_flag(self):
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())
        self.pushButton_8.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\02_Image\minus_disabled.png"))
        
        self.pushButton_7.clicked.connect(lambda: self.bt_maximize())
        self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\02_Image\maximize-2_disabled.png"))
        
        self.pushButton_9.clicked.connect(lambda: self.close())
        self.pushButton_9.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\02_Image\x_disabled.png"))

    def bt_maximize(self):
        if ui_window.isMaximized() == True:
            self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\02_Image\maximize-2_disabled.png"))
            self.showNormal()

        elif ui_window.isMaximized() == False:
            self.pushButton_7.setIcon(QIcon(r"C:\Users\Vinicius\Documents\GitHub\TCC\02_Image\minimize-2_disabled.png"))
            self.showMaximized()

    def reg_historico(self):
        self.stackedWidget.setCurrentIndex(0)
        self.label_9.setText("Registre o Histórico da UC")
        self.pushButton_0.setStyleSheet("background-color: rgb(138, 203, 250); color: white;")
        self.pushButton_0.setCursor(Qt.PointingHandCursor)
        self.pushButton_1.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")
        self.pushButton_1.setCursor(Qt.PointingHandCursor)
        self.pushButton_3.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")
        self.pushButton_3.setCursor(Qt.PointingHandCursor)

        subgrupo = getattr(self, "comboBox", None)
        modtar = getattr(self, "comboBox_2", None)
        
        subgrupo.currentIndexChanged.connect(lambda: self.update_subgrupo())
        modtar.currentIndexChanged.connect(lambda: self.update_modtar())
        self.pushButton_5.clicked.connect(lambda: self.att_historico())

    def update_subgrupo(self):
        subgrupo = getattr(self, "comboBox", None)
        modtar = getattr(self, "comboBox_2", None)
        condicional_modtar = {"A1 (≥ 230 kV)": ["Horária Azul"], "A2 (88 kV a 138 kV)": ["Horária Azul"], "A3 (69 kV)": ["Horária Azul"], 
                              "A3a (30 kV a 44 kV)": ["Horária Azul", "Horária Verde"], 
                              "A4 (2.3 a 25 kV)": ["Horária Azul", "Horária Verde"], 
                              "AS (≤ 2.3 kV subterrâneo)": ["Horária Azul", "Horária Verde"]}
        modtar.clear()
        current_selection = subgrupo.currentText()

        for item in condicional_modtar[current_selection]:
            modtar.addItem(item)

    def update_modtar(self):
        self.modtar = getattr(self, "comboBox_2", None).currentText()

        if self.modtar == "Horária Verde":
            getattr(self, "SpinBox_DCp_18", None).setEnabled(False) # Demanda Contratada Ponta

        else:
            getattr(self, "SpinBox_DCp_18", None).setEnabled(True) # Demanda Contratada Ponta
        
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
        
        historico = {"DemMedida_fp": demMed_fp, "DemMedida_p": demMed_p, "ConsumoFP": consFP, 
                   "ConsumoP": consP, "DemContratada_fp": demContratada_fp, 
                   "DemContratada_p": demContratada_p, "ModTar": modtar}

        return historico

    def reg_tarifas(self):
        self.stackedWidget.setCurrentIndex(1) # Abrir a janela do registro de tarifas
        self.label_9.setText("Registre as tarifas") # Mudar o título do software
        self.pushButton_1.setStyleSheet("background-color: rgb(138, 203, 250); color: white;")
        self.pushButton_0.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")
        self.pushButton_3.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")

        self.pushButton.clicked.connect(lambda: self.att_tarifas()) # Pressionando o botão atualizar
        
    def att_tarifas(self):
        # Modalidade tarifária Azul: 
        tar_dem_azul_ci_fp = getattr(self, "doubleSpinBox_9", None).value()
        tar_dem_azul_si_fp = getattr(self, "doubleSpinBox_11", None).value()
        tar_dem_azul_ci_p = getattr(self, "doubleSpinBox_10", None).value()
        tar_dem_azul_si_p = getattr(self, "doubleSpinBox_12", None).value()
        tar_cons_azul_tusd_fp = getattr(self, "doubleSpinBox_25", None).value()
        tar_cons_azul_tusd_p = getattr(self, "doubleSpinBox_26", None).value()
        tar_cons_azul_te_fp = getattr(self, "doubleSpinBox_16", None).value()
        tar_cons_azul_te_p = getattr(self, "doubleSpinBox_18", None).value()
        
        tarifas_azul_si = [tar_dem_azul_si_fp, tar_dem_azul_si_p, tar_cons_azul_tusd_fp, 
                           tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p]
        tarifas_azul_ci = [tar_dem_azul_ci_fp, tar_dem_azul_ci_p, tar_cons_azul_tusd_fp, 
                           tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p]
        tarifas_azul = [tarifas_azul_si, tarifas_azul_ci]

        # Modalidade tarifária Verde
        tar_dem_verde_ci = getattr(self, "doubleSpinBox_14", None).value()
        tar_dem_verde_si = getattr(self, "doubleSpinBox_8", None).value()
        tar_cons_verde_tusd_fp = getattr(self, "doubleSpinBox_24", None).value()
        tar_cons_verde_tusd_p = getattr(self, "doubleSpinBox_23", None).value()
        tar_cons_verde_te_fp = getattr(self, "doubleSpinBox_27", None).value()
        tar_cons_verde_te_p = getattr(self, "doubleSpinBox_62", None).value()

        tarifas_verde_si = [tar_dem_verde_si, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p]
        tarifas_verde_ci = [tar_dem_verde_ci, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p]
        tarifas_verde = [tarifas_verde_si, tarifas_verde_ci]

        tarifas = []
        tarifas.append(tarifas_azul)
        tarifas.append(tarifas_verde)

        return tarifas
    
    def comparacao_economica(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.label_9.setText("Comparação Econômica")
        self.pushButton_3.setStyleSheet("background-color: rgb(138, 203, 250); color: white;")
        self.pushButton_0.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")
        self.pushButton_1.setStyleSheet("background-color: rgba(33, 43, 51, 100); color: silver;")
        

        
        self.graph_demMed_Ajustado()
        self.graph_demOtima_Ajustado()
        self.graph_FatxDem()
        self.criar_tabela()
       
        # Fechar o Canva após gerar os gráficos
        for i in reversed(range(self.verticalLayout_8.count())):
            self.canvas_demOtimaAjustado = self.verticalLayout_8.itemAt(i).widget()
            self.verticalLayout_8.removeWidget(self.canvas_demOtimaAjustado)

        for i in reversed(range(self.verticalLayout_12.count())):
            self.canvas_demMedAtual = self.verticalLayout_12.itemAt(i).widget()
            self.verticalLayout_12.removeWidget(self.canvas_demMedAtual)

        for i in reversed(range(self.verticalLayout_11.count())):
            self.canvas_Fat_x_Dem_fp = self.verticalLayout_11.itemAt(i).widget()
            self.verticalLayout_11.removeWidget(self.canvas_Fat_x_Dem_fp)

        for i in reversed(range(self.verticalLayout_13.count())):
            self.canvas_Fat_x_Dem_p = self.verticalLayout_13.itemAt(i).widget()
            self.verticalLayout_13.removeWidget(self.canvas_Fat_x_Dem_p)

    def demFaturada(self, demMed, demCont):
        tolerancia = demCont * 1.05
        listaTolerancia = [0] * 12
        listaSobra = [0] * 12
        listaUltrapassagem = [0] * 12
        demMedfp = demMed

        for i in range(0, 12):
            if demMedfp[i] <= demCont:
                listaSobra[i] = demCont - demMedfp[i]

            elif (demMedfp[i] <= tolerancia) and (demMedfp[i] > demCont):
                listaTolerancia[i] = demMedfp[i] - demCont


            elif demMedfp[i] > tolerancia:
                listaUltrapassagem[i] = ((demMedfp[i] - demCont) * 2)
              
        demFaturada = sum(listaUltrapassagem) + sum(listaSobra) + sum(demMedfp)
        tupla = listaUltrapassagem, listaTolerancia, listaSobra, demMedfp, demFaturada

        return tupla

    def faturaDemanda(self, demCont_fp=0.0, demCont_p=0.0):
        tarifas_azul, tarifas_verde = self.att_tarifas()

        tarifas_azul_si, tarifas_azul_ci = tarifas_azul
        tar_dem_azul_si_fp, tar_dem_azul_si_p, tar_cons_azul_tusd_fp, tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p = tarifas_azul_si
        tar_dem_azul_ci_fp, tar_dem_azul_ci_p, tar_cons_azul_tusd_fp, tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p = tarifas_azul_ci
        
        tarifas_verde_si, tarifas_verde_ci = tarifas_verde
        tar_dem_verde_si, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p = tarifas_verde_si
        tar_dem_verde_ci, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p = tarifas_verde_ci

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Demanda Medida Atual
        demFat_fp = self.demFaturada(demMed=demMed_fp, demCont=demCont_fp)
        demFat_p = self.demFaturada(demMed=demMed_p, demCont=demCont_p)
        listaUltrapassagem_fp, listaTolerancia_fp, listaSobra_fp, demMedfp, demFaturada_fp = demFat_fp
        listaUltrapassagem_p, listaTolerancia_p, listaSobra_p, demMedp, demFaturada_p = demFat_p
        
        faturasVerde = []
        faturasAzul = []
        faturasAzul_fp =[]
        faturasAzul_p =[]

        for i in range(0, 12, 1):
            faturaVerde = ((listaUltrapassagem_fp[i] + demMedfp[i]) * tar_dem_verde_ci) + (listaSobra_fp[i] * tar_dem_verde_si)
            faturasVerde.append(faturaVerde)

        for i in range(0, 12, 1):
            faturaAzul_fp = (((listaUltrapassagem_fp[i] + demMedfp[i]) * tar_dem_azul_ci_fp) + (listaSobra_fp[i] * tar_dem_azul_si_fp))
            faturaAzul_p = (((listaUltrapassagem_p[i] + demMedp[i]) * tar_dem_azul_ci_p) + (listaSobra_p[i] * tar_dem_azul_si_p))
            faturasAzul_fp.append(faturaAzul_fp)
            faturasAzul_p.append(faturaAzul_p)
            fatura = faturaAzul_fp + faturaAzul_p
            faturasAzul.append(fatura)

        
        return faturasAzul, faturasVerde, faturasAzul_fp, faturasAzul_p
    
    def faturaConsumo(self):
        tarifas_azul, tarifas_verde = self.att_tarifas()

        tarifas_azul_si, tarifas_azul_ci = tarifas_azul
        tar_dem_azul_si_fp, tar_dem_azul_si_p, tar_cons_azul_tusd_fp, tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p = tarifas_azul_si
        tar_dem_azul_ci_fp, tar_dem_azul_ci_p, tar_cons_azul_tusd_fp, tar_cons_azul_tusd_p, tar_cons_azul_te_fp, tar_cons_azul_te_p = tarifas_azul_ci
        
        tarifas_verde_si, tarifas_verde_ci = tarifas_verde
        tar_dem_verde_si, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p = tarifas_verde_si
        tar_dem_verde_ci, tar_cons_verde_tusd_fp, tar_cons_verde_tusd_p, tar_cons_verde_te_fp, tar_cons_verde_te_p = tarifas_verde_ci

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores

        fatConsVerde_fp = sum(consFP) * (tar_cons_verde_te_fp + tar_cons_verde_tusd_fp)
        fatConsVerde_p = sum(consP) * (tar_cons_verde_te_p + tar_cons_verde_tusd_p)
        fatConsVerde = fatConsVerde_fp + fatConsVerde_p

        fatConsAzul_fp = sum(consFP) * (tar_cons_azul_te_fp + tar_cons_azul_tusd_fp)
        fatConsAzul_p = sum(consP) * (tar_cons_azul_te_p + tar_cons_azul_tusd_p)
        fatConsAzul = fatConsAzul_fp + fatConsAzul_p

        return fatConsVerde, fatConsAzul, fatConsVerde_fp, fatConsVerde_p, fatConsAzul_fp, fatConsAzul_p

    def faturaOtima(self):
        range_dem_fp = np.arange(0, 1000, 1)
        range_dem_p = np.arange(0, 1000, 1)
        lista_faturaVerde = []
        lista_faturaAzul = []
        lista_faturaAzul_fp = []
        lista_faturaAzul_p = []

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        
        for demContVerde in range_dem_fp:
            faturasAzul, faturasVerde, faturasAzul_fp, faturasAzul_p = self.faturaDemanda(demCont_fp=demContVerde)
            lista_faturaVerde.append(sum(faturasVerde))

        demContratadaVerde = dict(zip(range_dem_fp, lista_faturaVerde))

        demOtimaVerde, fatOtimaVerde = min(demContratadaVerde.items(), key=lambda x: x[1])
            
        demFatVerde = self.demFaturada(demMed_fp, demOtimaVerde)
        listaUltrapassagemVerde_fp, listaToleranciaVerde_fp, listaSobraVerde_fp, demMedVerde_fp, faturadaOtimaVerde = demFatVerde
        
        
        for demContAzul_fp in range_dem_fp:
            faturasAzul, faturasVerde, faturasAzul_fp, faturasAzul_p = self.faturaDemanda(demCont_fp=demContAzul_fp, demCont_p=demContratada_p)
            lista_faturaAzul_fp.append(sum(faturasAzul_fp))
            lista_faturaAzul.append(faturasAzul)

        for demContAzul_p in range_dem_p:
            faturasAzul, faturasVerde, faturasAzul_fp, faturasAzul_p = self.faturaDemanda(demCont_fp=demContratada_fp, demCont_p=demContAzul_p)
            lista_faturaAzul_p.append(sum(faturasAzul_p))
            lista_faturaAzul.append(faturasAzul)

        demContratadaAzul_fp = dict(zip(range_dem_fp, lista_faturaAzul_fp))
        demContratadaAzul_p = dict(zip(range_dem_p, lista_faturaAzul_p))

        demOtimaAzul_fp, fatOtimaAzul_fp = min(demContratadaAzul_fp.items(), key=lambda x: x[1])
        demOtimaAzul_p, fatOtimaAzul_p = min(demContratadaAzul_p.items(), key=lambda x: x[1])
            
        demFatAzul_fp = self.demFaturada(demMed_fp, demOtimaAzul_fp)
        demFatAzul_p = self.demFaturada(demMed_p, demOtimaAzul_p)
        listaUltrapassagemAzul_fp, listaToleranciaAzul_fp, listaSobraAzul_fp, demMedAzul_fp, faturadaOtimaAzul_fp = demFatAzul_fp
        listaUltrapassagemAzul_p, listaToleranciaAzul_p, listaSobraAzul_p, demMedAzul_p, faturadaOtimaAzul_p = demFatAzul_p
            
        return demOtimaVerde, fatOtimaVerde, lista_faturaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, lista_faturaAzul_fp, lista_faturaAzul_p

    def graph_demOtima_Ajustado(self):
        self.figure_demOtimaAjustado = plt.figure(figsize=(5.7, 4), dpi=85)
        self.canvas_demOtimaAjustado = FigureCanvas(self.figure_demOtimaAjustado)
        self.verticalLayout_12.addWidget(self.canvas_demOtimaAjustado)

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        if modtar == "Horária Verde":
            self.demOtimaAjustado_Verde()
        
        elif modtar == "Horária Azul":
            self.demOtimaAjustado_Azul()
            
        plt.title("Gráfico 2 - Registro de demanda para a DC Ótima")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')

    def demOtimaAjustado_Verde(self):
        self.figure_demOtimaAjustado.clear()

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Fatura Otima
        demOtimaVerde, fatOtimaVerde, faturadaOtimaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, faturadaOtimaAzul_fp, faturadaOtimaAzul_p = self.faturaOtima()
        
        # Demanda Faturada Ótima
        demFatVerde = self.demFaturada(demMed_fp, demOtimaVerde)
        listaUltrapassagemVerde_fp, listaToleranciaVerde_fp, listaSobraVerde_fp, demMedVerde_fp, faturadaOtimaVerde = demFatVerde

        # Config Gráfico
        tolerancia = demOtimaVerde * 1.05
        barWidth = 0.4
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot
        plt.bar(x_axis - 0.21, demMedVerde_fp, color="blue", label="DM FPonta", width=barWidth, edgecolor='silver')
        plt.bar(x_axis - 0.21, listaSobraVerde_fp, bottom=demMedVerde_fp, color="gray", label="DS", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, listaUltrapassagemVerde_fp, bottom=demMedVerde_fp, color="red", label="DU",
                width=barWidth, edgecolor='silver')
        plt.hlines(y=demOtimaVerde, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"DC: {demOtimaVerde} kW")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demOtimaAjustado.draw()

    def demOtimaAjustado_Azul(self):
        self.figure_demOtimaAjustado.clear()

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Fatura Otima
        demOtimaVerde, fatOtimaVerde, faturadaOtimaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, faturadaOtimaAzul_fp, faturadaOtimaAzul_p = self.faturaOtima()
        
        # Demanda Faturada Ótima
        demFatAzul_fp = self.demFaturada(demMed_fp, demOtimaAzul_fp)
        demFatAzul_p = self.demFaturada(demMed_p, demOtimaAzul_p)
        listaUltrapassagemAzul_fp, listaToleranciaAzul_fp, listaSobraAzul_fp, demMedAzul_fp, faturadaOtimaAzul_fp = demFatAzul_fp
        listaUltrapassagemAzul_p, listaToleranciaAzul_p, listaSobraAzul_p, demMedAzul_p, faturadaOtimaAzul_p = demFatAzul_p
        
        # Config Gráfico
        tolerancia_fp = demOtimaAzul_fp * 1.05
        tolerancia_p = demOtimaAzul_p * 1.05
        barWidth = 0.3
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot FP
        plt.bar(x_axis - 0.21, demMedAzul_fp, color="blue", label="D Medida FP", width=barWidth, edgecolor='silver')
        plt.bar(x_axis - 0.21, listaSobraAzul_fp, bottom=demMedAzul_fp, color="gray", label="D Sobra", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, listaUltrapassagemAzul_fp, bottom=demMedAzul_fp, color="red", label="D Ult FP",
                width=barWidth, edgecolor='silver')
        plt.hlines(y=demOtimaAzul_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"D Ótima FP: {demOtimaAzul_fp} kW")
        plt.hlines(y=tolerancia_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância FP: {tolerancia_fp} kW")
        
        # Make the plot P
        plt.bar(x_axis + 0.21, demMedAzul_p, color="green", label="D Medida P", width=barWidth, edgecolor='silver')
        plt.bar(x_axis + 0.21, listaSobraAzul_p, bottom=demMedAzul_p, color="gray", label="D Sobra P", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis + 0.21, listaUltrapassagemAzul_p, bottom=demMedAzul_p, color="red", label="D Ult P",
                width=barWidth, edgecolor='silver')
        plt.hlines(y=demOtimaAzul_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"D Ótima P: {demOtimaAzul_p} kW")
        plt.hlines(y=tolerancia_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância P: {tolerancia_p} kW") 
        
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demOtimaAjustado.draw()

    def graph_FatxDem(self):
        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        if modtar == "Horária Verde":
            self.figure_Fat_x_Dem_fp = plt.figure(figsize=(5.7, 4), dpi=85)
            self.canvas_Fat_x_Dem_fp = FigureCanvas(self.figure_Fat_x_Dem_fp)
            self.verticalLayout_11.addWidget(self.canvas_Fat_x_Dem_fp)
            self.graph_FatxDem_Verde()

            self.figure_Fat_x_Dem_p = plt.figure(figsize=(5.7, 4), dpi=85)
            self.canvas_Fat_x_Dem_p = FigureCanvas(self.figure_Fat_x_Dem_p)
            self.verticalLayout_13.addWidget(self.canvas_Fat_x_Dem_p)
            self.graph_FatxDem_Azulp()
        
        elif modtar == "Horária Azul":
            self.figure_Fat_x_Dem_fp = plt.figure(figsize=(5.7, 4), dpi=85)
            self.canvas_Fat_x_Dem_fp = FigureCanvas(self.figure_Fat_x_Dem_fp)
            self.verticalLayout_11.addWidget(self.canvas_Fat_x_Dem_fp)
            self.graph_FatxDem_Azulfp()
            self.figure_Fat_x_Dem_p = plt.figure(figsize=(5.7, 4), dpi=85)
            self.canvas_Fat_x_Dem_p = FigureCanvas(self.figure_Fat_x_Dem_p)
            self.verticalLayout_13.addWidget(self.canvas_Fat_x_Dem_p)
            self.graph_FatxDem_Azulp()
            
    def graph_FatxDem_Verde(self):
        self.figure_Fat_x_Dem_fp.clear()
        range_dem = list(np.arange(0, 1000, 1))
        demOtimaVerde, fatOtimaVerde, lista_faturaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, lista_faturaAzul_fp, lista_faturaAzul_p = self.faturaOtima()

        
        plt.plot(range_dem, lista_faturaVerde, label="Curva de Demanda Ótima")
        plt.vlines(x=demOtimaVerde, ymin=0, ymax=fatOtimaVerde, colors='black', linestyle='dashed',
                   label=f"Demanda Ótima: {demOtimaVerde:.2f}")
        plt.hlines(y=fatOtimaVerde, xmin=0, xmax=demOtimaVerde, colors='red', linestyle='dashed',
                   label=f"Faturamento Ótimo: R${fatOtimaVerde:.2f}")
        plt.xlim(demOtimaVerde / 2, demOtimaVerde * 2)
        plt.ylim(fatOtimaVerde / 2, fatOtimaVerde * 2)
        plt.plot(demOtimaVerde, fatOtimaVerde, marker="o", color="black")
        plt.legend(loc=3)
        plt.title("Gráfico 3 - Identificação da DC Ótima - Fora de Ponta")
        plt.xlabel('Demanda Contratada (kW)')
        plt.ylabel('Fatura (R$)')

    def graph_FatxDem_Azulfp(self):
        self.figure_Fat_x_Dem_fp.clear()
        range_dem = list(np.arange(0, 1000, 1))
        demOtimaVerde, fatOtimaVerde, lista_faturaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, lista_faturaAzul_fp, lista_faturaAzul_p = self.faturaOtima()

        
        plt.plot(range_dem, lista_faturaAzul_fp, label="Curva de Demanda Ótima")
        plt.vlines(x=demOtimaAzul_fp, ymin=0, ymax=fatOtimaAzul_fp, colors='black', linestyle='dashed',
                   label=f"Demanda Ótima: {demOtimaAzul_fp:.2f}")
        plt.hlines(y=fatOtimaAzul_fp, xmin=0, xmax=demOtimaAzul_fp, colors='red', linestyle='dashed',
                   label=f"Faturamento Ótimo: R${fatOtimaAzul_fp:.2f}")
        plt.xlim(demOtimaAzul_fp / 2, demOtimaAzul_fp * 2)
        plt.ylim(fatOtimaAzul_fp / 2, fatOtimaAzul_fp * 2)
        plt.plot(demOtimaAzul_fp, fatOtimaAzul_fp, marker="o", color="black")
        plt.legend(loc=3)
        plt.title("Gráfico 3 - Identificação da DC Ótima - Fora de Ponta")
        plt.xlabel('Demanda Contratada (kW)')
        plt.ylabel('Fatura (R$)')

    def graph_FatxDem_Azulp(self):
        self.figure_Fat_x_Dem_p.clear()
        range_dem = list(np.arange(0, 1000, 1))
        demOtimaVerde, fatOtimaVerde, lista_faturaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, lista_faturaAzul_fp, lista_faturaAzul_p = self.faturaOtima()

        
        plt.plot(range_dem, lista_faturaAzul_p, label="Curva de Demanda Ótima")
        plt.vlines(x=demOtimaAzul_p, ymin=0, ymax=fatOtimaAzul_p, colors='black', linestyle='dashed',
                   label=f"Demanda Ótima: {demOtimaAzul_p:.2f}")
        plt.hlines(y=fatOtimaAzul_p, xmin=0, xmax=demOtimaAzul_p, colors='red', linestyle='dashed',
                   label=f"Faturamento Ótimo: R${fatOtimaAzul_p:.2f}")
        plt.xlim(demOtimaAzul_p / 2, demOtimaAzul_p * 2)
        plt.ylim(fatOtimaAzul_p / 2, fatOtimaAzul_p * 2)
        plt.plot(demOtimaAzul_p, fatOtimaAzul_p, marker="o", color="black")
        plt.legend(loc=3)
        plt.title("Gráfico 4 - Identificação da DC Ótima - Ponta")
        plt.xlabel('Demanda Contratada (kW)')
        plt.ylabel('Fatura (R$)')

    def graph_demMed_Ajustado(self):
        # Criar a figura / canvas
        self.figure_demMedAjustado = plt.figure(figsize=(5.7, 4), dpi=85)
        self.canvas_demMedAjustado = FigureCanvas(self.figure_demMedAjustado)
        self.verticalLayout_8.addWidget(self.canvas_demMedAjustado)

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Gráfico a ser plotado:
        if modtar == "Horária Verde":
            self.demMed_Verde_Ajustado()
        
        elif modtar == "Horária Azul":
            self.demMed_Azul_Ajustado()

        # Configuração do gráfico
        plt.title("Gráfico 1 - Registro de demanda para a DC atual")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')

    def demMed_Verde_Ajustado(self):
        self.figure_demMedAjustado.clear()

        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Demanda Faturada Atual
        demFat_fp = self.demFaturada(demMed_fp, demContratada_fp)
        demFat_p = self.demFaturada(demMed_p, demContratada_p)
        
        listaUltrapassagem_fp, listaTolerancia_fp, listaSobra_fp, demMedfp, demFaturada_fp = demFat_fp
        listaUltrapassagem_p, listaTolerancia_p, listaSobra_p, demMedp, demFaturada_p = demFat_p

        # Config Gráfico
        tolerancia = demContratada_fp * 1.05
        barWidth = 0.4
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot
        plt.bar(x_axis - 0.21, demMedfp, color="blue", label="DM FPonta", width=barWidth, edgecolor='silver')
        plt.bar(x_axis - 0.21, listaSobra_fp, bottom=demMedfp, color="gray", label="DS", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, listaUltrapassagem_fp, bottom=demMedfp, color="red", label="DU",
                width=barWidth, edgecolor='silver')
        plt.hlines(y=demContratada_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
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
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores
        
        # Demanda Faturada Atual
        demFat_fp = self.demFaturada(demMed_fp, demContratada_fp)
        demFat_p = self.demFaturada(demMed_p, demContratada_p)
        
        listaUltrapassagem_fp, listaTolerancia_fp, listaSobra_fp, demMedfp, demFaturada_fp = demFat_fp
        listaUltrapassagem_p, listaTolerancia_p, listaSobra_p, demMedp, demFaturada_p = demFat_p

        # Config Gráfico
        tolerancia_fp = demContratada_fp * 1.05
        tolerancia_p = demContratada_p * 1.05
        barWidth = 0.3
        
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        
        # Make the plot
        # PLOT FORA DE PONTA
        plt.bar(x_axis - 0.21, demMedfp, color="blue", label="D Med FP", width=barWidth, edgecolor='silver',
                capsize=7)
        plt.bar(x_axis - 0.21, listaSobra_fp, bottom=demMedfp, color="gray", label="D Sobra FP", width=barWidth,
                edgecolor='silver')
        plt.bar(x_axis - 0.21, listaUltrapassagem_fp, bottom=demMedfp, color="red", label="D Ult FP", width=barWidth,
                edgecolor='silver')
        plt.hlines(y=demContratada_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"D Cont FP: {demContratada_fp} kW")
        plt.hlines(y=tolerancia_fp, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância FP: {tolerancia_fp} kW")
        # PLOT PONTA
        plt.bar(x_axis + 0.21, demMedp, color="green", label="D Med P", width=barWidth, edgecolor='silver',
                capsize=7)
        plt.bar(x_axis + 0.21, listaSobra_p, bottom=demMedp, color="gray", label="D Sobra P", width=barWidth, edgecolor='silver')
        plt.bar(x_axis + 0.21, listaUltrapassagem_p, bottom=demMedp, color="red", width=barWidth,
                edgecolor='silver')
        plt.hlines(y=demContratada_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='solid',
                   label=f"D Cont P: {demContratada_p} kW")
        plt.hlines(y=tolerancia_p, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância P: {tolerancia_p} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)

        # Plotar o Gráfico
        self.canvas_demMedAjustado.draw()
        
    def criar_tabela(self):
        # Inserir o histórico
        hist_uc = self.att_historico()
        valores = list(hist_uc.values())
        [demMed_fp, demMed_p, consFP, consP, demContratada_fp, demContratada_p, modtar] = valores

        # Importar valores da demanda ótima
        demOtimaVerde, fatOtimaVerde, lista_faturaVerde, demOtimaAzul_fp, demOtimaAzul_p, fatOtimaAzul_fp, fatOtimaAzul_p, lista_faturaAzul_fp, lista_faturaAzul_p = self.faturaOtima()

        # Importar valores de consumo
        fatConsVerde, fatConsAzul, fatConsVerde_fp, fatConsVerde_p, fatConsAzul_fp, fatConsAzul_p = self.faturaConsumo()

        # Importar valores de demanda atual
        faturasAzul_atual, faturasVerde_atual, faturasAzul_fp, faturasAzul_p = self.faturaDemanda(demCont_fp=demContratada_fp, demCont_p=demContratada_p)

        # Calcular total para Atual
        totalAtual_Verde = fatConsVerde + float(sum(faturasVerde_atual)) 
        totalAtual_Azul = fatConsAzul + float(sum(faturasAzul_atual))
        # Calcular total para Ótima
        totalOtimo_Verde = fatConsVerde + fatOtimaVerde
        totalOtimo_Azul = fatConsAzul + (fatOtimaAzul_p + fatOtimaAzul_fp)

        # Calcular economia
        # Considerando que a atual é verde, a comparação é em cima de totalAtual_Verde
        economiaVerde_reais_V = totalAtual_Verde - totalOtimo_Verde
        economiaVerde_porce_V = (economiaVerde_reais_V / totalAtual_Verde) * 100
        # Considerando que a atual é azul, a comparação é em cima de totalAtual_Azul
        economiaVerde_reais_A = totalAtual_Azul - totalOtimo_Verde
        economiaVerde_porce_A = (economiaVerde_reais_A / totalAtual_Azul) * 100
        # Considerando que a atual é verde, a comparação é em cima de totalAtual_Verde
        economiaAzul_reais_V = totalAtual_Verde - totalOtimo_Azul
        economiaAzul_porce_V = (economiaAzul_reais_V / totalAtual_Verde) * 100
        # Considerando que a atual é azul, a comparação é em cima de totalAtual_Azul
        economiaAzul_reais_A = totalAtual_Azul - totalOtimo_Azul
        economiaAzul_porce_A = (economiaAzul_reais_A / totalAtual_Azul) * 100

        # Inserir os valores de Consumo Verde
        self.label_120.setText(f"R$ {fatConsVerde_fp:.2f}") # Verde FP
        self.label_55.setText(f"R$ {fatConsVerde_p:.2f}") # Verde P
        self.label_118.setText(f"R$ {fatConsVerde:.2f}") # Total Verde
        # Inserir os valores de Consumo Azul
        self.label_122.setText(f"R$ {fatConsAzul_fp:.2f}") # Azul FP
        self.label_54.setText(f"R$ {fatConsAzul_p:.2f}") # Azul P
        self.label_119.setText(f"R$ {fatConsAzul:.2f}") # Total Azul
        # Inserir os valores de Demanda Ótima Verde (R$)
        self.label_123.setText(f"R$ {fatOtimaVerde:.2f}") # Fatura Ótima Verde FP
        self.label_124.setText("-") # Fatura Ótima Verde P
        self.label_133.setText(f"R$ {fatOtimaVerde:.2f}") # Fatura Ótima Verde Total
        # Inserir os valores de Demanda Ótima Azul (R$)
        self.label_130.setText(f"R$ {fatOtimaAzul_fp:.2f}") # Fatura Ótima Azul FP
        self.label_131.setText(f"R$ {fatOtimaAzul_p:.2f}") # Fatura Ótima Azul P
        self.label_128.setText(f"R$ {(fatOtimaAzul_fp + fatOtimaAzul_p):.2f}") # Fatura Ótima Azul Total
        # Inserir os valores de Despesa Total Verde (R$)
        self.label_138.setText(f"R$ {totalOtimo_Verde:.2f}") # Despesa Total Verde
        # Inserir os valores de Despesa Total Azul (R$)
        self.label_136.setText(f"R$ {totalOtimo_Azul:.2f}") # Despesa Total Azul
        
        if modtar == "Horária Verde":
            # Inserir os valores de Consumo Atual
            self.label_121.setText(f"R$ {fatConsVerde_fp:.2f}") # Verde FP
            self.label_57.setText(f"R$ {fatConsVerde_p:.2f}") # Verde P
            self.label_62.setText(f"R$ {fatConsVerde:.2f}") # Verde Total
            # Inserir os valores de Demanda Atual
            self.label_132.setText(f"R$ {float(sum(faturasVerde_atual)):.2f}") # Atual Verde FP
            self.label_125.setText("-") # Atual Verde P
            self.label_127.setText(f"R$ {float(sum(faturasVerde_atual)):.2f}") # Atual Verde Total
            # Inserir valores de despesa total
            self.label_137.setText(f"R$ {totalAtual_Verde:.2f}") # Despesa Total Atual Verde
            # Inserir os valores de Economia
            self.label_144.setText(f"R$ {economiaVerde_reais_V:.2f}") # Economia em reais Verde
            self.label_146.setText(f"{economiaVerde_porce_V:.2f}%") # Economia em porcentagem Verde
            self.label_145.setText(f"R$ {economiaAzul_reais_V:.2f}") # Economia em reais Azul
            self.label_147.setText(f"{economiaAzul_porce_V:.2f}%") # Economia em porcentagem Azul

            if economiaVerde_reais_V < 0:
                self.label_144.setStyleSheet("color: red")
                self.label_146.setStyleSheet("color: red")

            elif economiaVerde_reais_V == 0:
                self.label_144.setStyleSheet("color: #3d8ec9")
                self.label_146.setStyleSheet("color: #3d8ec9")

            elif economiaVerde_reais_V > 0:
                self.label_144.setStyleSheet("color: green")
                self.label_146.setStyleSheet("color: green")

            if economiaAzul_reais_V < 0:
                self.label_145.setStyleSheet("color: red")
                self.label_147.setStyleSheet("color: red")

            elif economiaAzul_reais_V == 0:
                self.label_145.setStyleSheet("color: #3d8ec9")
                self.label_147.setStyleSheet("color: #3d8ec9")

            elif economiaAzul_reais_V > 0:
                self.label_145.setStyleSheet("color: green")
                self.label_147.setStyleSheet("color: green")

        elif modtar == "Horária Azul":
            # Inserir os valores de Consumo Atual
            self.label_121.setText(f"R$ {fatConsAzul_fp:.2f}")
            self.label_57.setText(f"R$ {fatConsAzul_p:.2f}")
            self.label_62.setText(f"R$ {fatConsAzul:.2f}")
            # Inserir os valores de Demanda Atual
            self.label_132.setText(f"R$ {float(sum(faturasAzul_fp)):.2f}") # Atual Azul FP
            self.label_125.setText(f"R$ {float(sum(faturasAzul_p)):.2f}") # Atual Azul P
            self.label_127.setText(f"R$ {float(sum(faturasAzul_atual)):.2f}") # Atual Azul Total
            # Inserir valores de despesa total
            self.label_137.setText(f"R$ {totalAtual_Azul:.2f}") # Despesa Total Atual Azul
            # Inserir os valores de Economia
            self.label_144.setText(f"R$ {economiaVerde_reais_A:.2f}") # Economia em reais Verde
            self.label_146.setText(f"{economiaVerde_porce_A:.2f}%") # Economia em porcentagem Verde
            self.label_145.setText(f"R$ {economiaAzul_reais_A:.2f}") # Economia em reais Azul
            self.label_147.setText(f"{economiaAzul_porce_A:.2f}%") # Economia em porcentagem Azul

            if economiaVerde_reais_A < 0:
                self.label_144.setStyleSheet("color: red")
                self.label_146.setStyleSheet("color: red")

            elif economiaVerde_reais_A == 0:
                self.label_144.setStyleSheet("color: #3d8ec9")
                self.label_146.setStyleSheet("color: #3d8ec9")

            elif economiaVerde_reais_A > 0:
                self.label_144.setStyleSheet("color: green")
                self.label_146.setStyleSheet("color: green")

            if economiaAzul_reais_A < 0:
                self.label_145.setStyleSheet("color: red")
                self.label_147.setStyleSheet("color: red")

            elif economiaAzul_reais_A == 0:
                self.label_145.setStyleSheet("color: #3d8ec9")
                self.label_147.setStyleSheet("color: #3d8ec9")

            elif economiaAzul_reais_A > 0:
                self.label_145.setStyleSheet("color: green")
                self.label_147.setStyleSheet("color: green")
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_window = Main()
    ui_window.show()
    sys.exit(app.exec_())
