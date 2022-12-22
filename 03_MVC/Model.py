import matplotlib.pyplot as plt
import numpy as np


class Methods:
    def __init__(self, dem_contfp=0, dem_contp=0, dem_med_fponta=None, dem_med_ponta=None, consumo_fponta=None, consumo_ponta=None,
                 tarifa_dem_fponta_ct=None, tarifa_dem_fponta_st=None, tarifa_dem_ponta_ct=None, elev_carga=None,
                 tarifa_dem_ponta_st=None, tarifa_cons_fponta=None, tarifa_cons_ponta=None, mod_tar="", subgrupo=""):

        # DECLARAÇÃO DE PARÂMETROS
        # MEDIÇÃO
        self.dem_contfp = dem_contfp
        self.dem_contp = dem_contp
        self.dem_med_fponta = dem_med_fponta
        self.dem_med_ponta = dem_med_ponta
        self.consumo_fponta = consumo_fponta
        self.consumo_ponta = consumo_ponta
        self.elev_carga = elev_carga
        self.mod_tar = mod_tar
        self.subgrupo = subgrupo
        # TARIFAS
        # Com tributos (ct)
        self.tarifa_dem_ponta_ct = tarifa_dem_ponta_ct
        self.tarifa_cons_ponta_ct = tarifa_cons_ponta
        self.tarifa_cons_fponta_ct = tarifa_cons_fponta
        self.tarifa_dem_fponta_ct = tarifa_dem_fponta_ct
        # Sem tributos (st)
        self.tarifa_dem_ponta_st = tarifa_dem_ponta_st
        self.tarifa_dem_fponta_st = tarifa_dem_fponta_st
        # DECLARAÇÃO DE VARIÁVEIS
        self.meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        self.fatura = None
        self.lista_Dcfp = [dem_contfp] * 12
        self.lista_Dcp = [dem_contp] * 12
        self.lista_ultrapassagem = [0] * 12
        self.lista_sobra = [0] * 12
        self.toleranciafp = dem_contfp * 1.05
        self.toleranciap = dem_contp * 1.05
        self.lista_tolerancia = [0] * 12
        self.multa = [0] * 12
        self.dem_graf = [0] * 12
        self.dem_fat = [0] * 12
        self.piscofins = 0.05
        self.icms = 0.18
        # BANDEIRAS
        self.band_verde = 0
        self.band_amarela = 0
        self.band_vermelha1 = 0
        self.band_vermelha2 = 0
        self.crise_hidrica = 0

    def dem_faturada(self, dem_medida, dem_cont):
        """
        Nome da função não definido.
        :param dem_medida: demanda medida
        :param dem_cont: demanda contratada
        :return: utilizado para calcular a demanda faturada, utilizando o método de omização do contrato de demanda,
        de acordo com as informações inseridas como parâmetros do método.
        """
        tolerancia = dem_cont * 1.05
        lista_tolerancia = [0] * 12
        lista_sobra = [0] * 12
        lista_ultrapassagem = [0] * 12

        for i in range(0, 12):
            if dem_medida[i] <= dem_cont:
                lista_sobra[i] = dem_cont - dem_medida[i]

            if (dem_medida[i] <= tolerancia) and (dem_medida[i] > dem_cont):
                lista_tolerancia[i] = dem_medida[i] - dem_cont

            if dem_medida[i] > tolerancia:
                lista_ultrapassagem[i] = (dem_medida[i] - dem_cont) * 2

        return lista_ultrapassagem, lista_tolerancia, lista_sobra

    def fat_tol(self):
        fatura = 0
        dm = self.dem_med_fponta

        for i in range(0, 12):
            if (dm[i] <= self.toleranciafp) and (dm[i] > self.dem_contfp):
                fatura += dm[i] * self.tarifa_dem_fponta_ct
        return fatura

    def fat_n_con(self):
        fatura = 0
        dm = self.dem_med_fponta

        for i in range(0, 12):
            if dm[i] <= self.dem_contfp:
                fatura += dm[i] * self.tarifa_dem_fponta_ct + (self.dem_contfp - dm[i]) * self.tarifa_dem_fponta_st
        return fatura

    def fat_ult(self):
        fatura = 0
        dm = self.dem_med_fponta

        for i in range(0, 12):
            if dm[i] > self.toleranciafp:
                fatura += dm[i] * self.tarifa_dem_fponta_ct + (2 * (dm[i] - self.dem_contfp) * self.tarifa_dem_fponta_ct)
        return fatura

    def fat_tot(self):
        fatura = Methods.fat_ult(self) + Methods.fat_tol(self) + Methods.fat_n_con(self)
        return fatura

    def lista_fatura_otima(self):
        range_dem = np.arange(75, 2501, 1)
        fatura = 0
        lista_fatura = []

        for dem_cont in range_dem:
            dem_tol = dem_cont * 1.05
            for i in range(0, 12):
                if (self.dem_med_fponta[i] <= dem_tol) and (self.dem_med_fponta[i] >= dem_cont):
                    fatura += self.dem_med_fponta[i] * self.tarifa_dem_fponta_ct

                elif self.dem_med_fponta[i] < dem_cont:
                    fatura += self.dem_med_fponta[i] * self.tarifa_dem_fponta_ct + (dem_cont - self.dem_med_fponta[i]) * self.tarifa_dem_fponta_st

                elif self.dem_med_fponta[i] > dem_tol:
                    fatura += self.dem_med_fponta[i] * self.tarifa_dem_fponta_ct + (2 * (self.dem_med_fponta[i] - dem_cont) * self.tarifa_dem_fponta_ct)

            lista_fatura.append(fatura)
            fatura = 0

        return lista_fatura

    def fatura_otima(self):
        lista_fatura = Methods.lista_fatura_otima(self)
        fatura_otima = min(lista_fatura)
        return fatura_otima

    def dem_otima(self):
        fat_otimo = Methods.lista_fatura_otima(self)
        range_dem = np.arange(75, 2501, 1)
        otima = 10 ** 7
        var = 0

        for i in range(0, len(fat_otimo)):
            if fat_otimo[i] < otima:
                otima = fat_otimo[i]
                var = i

        return range_dem[var]

    def graf_otima(self):
        range_dem = list(np.arange(75, 2501, 1))
        lista_fat = Methods.lista_fatura_otima(self)
        fat_otima = Methods.fatura_otima(self)
        dem_otima = Methods.dem_otima(self)

        plt.figure(2, figsize=(12, 6))
        plt.plot(range_dem, lista_fat, label="Curva de Demanda Ótima")
        plt.vlines(x=dem_otima, ymin=0, ymax=fat_otima, colors='black', linestyle='dashed',
                   label=f"Demanda Ótima: {dem_otima:.2f}")
        plt.hlines(y=fat_otima, xmin=0, xmax=dem_otima, colors='red', linestyle='dashed',
                   label=f"Faturamento Ótimo: R${fat_otima:.2f}")
        plt.xlim(dem_otima / 2, dem_otima * 2)
        plt.ylim(fat_otima / 2, fat_otima * 2)
        plt.plot(dem_otima, fat_otima, marker="o", color="black")
        # plt.title("Curva Demanda Ótima (R$)")
        plt.xlabel('Demanda Contratada (kW)')
        plt.ylabel('Fatura (R$)')
        plt.legend(loc=3)
        plt.show()

    def graf_otima_ajust(self):
        dem_med = self.dem_med_fponta
        dem_otima = Methods.dem_otima(self)
        sobra = [0] * 12
        tol = [0] * 12
        ultrapassagem = [0] * 12
        multa = [0] * 12

        for i in range(0, 12):
            if dem_med[i] <= dem_otima:  # Calculo para demanda não consumida
                sobra[i] = dem_otima - dem_med[i]

            elif (dem_med[i] <= dem_otima * 1.05) and (dem_med[i] > dem_otima):  # Calculo para faixa de tolerância
                tol[i] = dem_med[i] - dem_otima

            elif dem_med[i] > dem_otima * 1.05:  # Calculo para encontrar demanda de ultrapassagem
                ultrapassagem[i] = dem_med[i] - dem_otima
                dem_med[i] = dem_otima
                multa[i] = ultrapassagem[i] * 2

        plt.figure(3, figsize=(12, 6))
        plt.bar(self.meses, dem_med, color="blue", label="DM - Demanda Medida")
        plt.bar(self.meses, sobra, bottom=dem_med, color="gray", label="DS - Demanda não utilizada")
        plt.bar(self.meses, multa, bottom=dem_med, color="red", label="DU - Demanda de Ultrapassagem")
        plt.hlines(y=dem_otima, xmin=self.meses[0], xmax=self.meses[11], colors='black', linestyle='dashed',
                   label=f"Demanda contratada: {dem_otima:.2f}")
        plt.hlines(y=(dem_otima * 1.05), xmin=self.meses[0], xmax=self.meses[11], colors='orange', linestyle='dashed',
                   label=f"Tolerância de ultrapassagem {dem_otima * 1.05:.2f}")
        plt.legend()
        # plt.title("Histórico de Consumo pela Demanda Ótima")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        plt.show()


class Graphics(Methods):
    def __init__(self, dmfp=None, dmp=None, dcfp=0, dcp=0):
        super(Methods).__init__()
        self.meses = metodos.meses
        self.dmfp = dmfp
        self.dcfp = dcfp
        self.lista_dcfp = [dcfp] * 12
        self.toleranciafp = dcfp * 1.05
        self.dmp = dmp
        self.dcp = dcp
        self.lista_dcp = [dcp] * 12
        self.toleranciap = dcp * 1.05

    def dem_medida_atual_convencional(self, dem_medida_fp, dem_medida_p, dem_cont):
        lista_dc = [dem_cont] * 12
        tolerancia = dem_cont * 1.05
        barWidth = 0.4
        # set width bar
        plt.figure(figsize=(12, 8))
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # Make the plot
        plt.bar(x_axis - 0.2, dem_medida_fp, color="blue", label="DM FP", width=barWidth)
        plt.bar(x_axis + 0.2, dem_medida_p, color="green", label="DM P", width=barWidth)
        plt.hlines(y=lista_dc, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='black', linestyle='dashed',
                       label=f"DC - Demanda Contratada: {float(dem_cont)}")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='orange', linestyle='dashed',
                       label=f"Lim. Tolerância: {tolerancia}")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        return plt.show()

    def dem_medida_atual_verde(self, dem_medida_fp, dem_medida_p, dem_cont):
        lista_dc = [dem_cont] * 12
        tolerancia = dem_cont * 1.05
        barWidth = 0.4
        # set width bar
        plt.figure(figsize=(12, 8))
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # Make the plot
        plt.bar(x_axis - 0.2, dem_medida_fp, color="blue", label="DM FP", width=barWidth)
        plt.bar(x_axis + 0.2, dem_medida_p, color="green", label="DM P", width=barWidth)
        plt.hlines(y=lista_dc, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='black', linestyle='dashed',
                   label=f"DC - Demanda Contratada: {float(dem_cont)}")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='orange', linestyle='dashed',
                   label=f"Lim. Tolerância: {tolerancia}")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        return plt.show()

    def dem_medida_atual_azul(self):
        barWidth = 0.4
        # set width bar
        plt.figure(figsize=(12, 8))
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # Make the plot
        plt.bar(x_axis - 0.2, self.dmfp, color="blue", label="DM FP", width=barWidth)  # DM FP
        plt.bar(x_axis + 0.2, self.dmp, color="green", label="DM P", width=barWidth)  # DM P
        # Fora de Ponta
        plt.hlines(y=self.lista_dcfp, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='black', linestyle='dashed',
                       label=f"DC FP: {float(self.dcfp)}")  # DC FP
        plt.hlines(y=self.toleranciafp, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='orange', linestyle='dashed',
                       label=f"Lim. Tolerância: {self.toleranciafp}")  # LimTol FP
        # Ponta
        plt.hlines(y=self.lista_dcp, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='black', linestyle='solid',
                       label=f"DC P: {float(self.dcp)}")  # DC P
        plt.hlines(y=self.toleranciap, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='orange', linestyle='solid',
                       label=f"Lim. Tolerância: {self.toleranciap}")  # LimTol P
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        return plt.show()

    def graf_ajuste_convencional(self, dem_medida, dem_cont):
        lista_tolerancia, lista_ultrapassagem, lista_sobra = metodos.dem_faturada(dem_medida, dem_cont)
        tolerancia = dem_cont * 1.05
        barWidth = 0.4

        for i in range(0, 12):
            if dem_medida[i] <= dem_cont:
                lista_sobra[i] = dem_cont - dem_medida[i]
            elif (dem_medida[i] <= tolerancia) and (dem_medida[i] > dem_cont):
                lista_tolerancia[i] = dem_medida[i] - dem_cont
            elif dem_medida[i] > tolerancia:  # Calculo para encontrar demanda de ultrapassagem
                lista_ultrapassagem[i] = dem_medida[i] - dem_cont

        # set width bar
        plt.figure(figsize=(12, 8))
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # Make the plot
        plt.bar(x_axis, dem_medida, color="blue", label="DM - Demanda Medida", width=barWidth)
        plt.bar(x_axis, lista_sobra, bottom=dem_medida, color="gray", label="DS - Demanda não utilizada", width=barWidth)
        plt.bar(x_axis, lista_ultrapassagem, bottom=dem_medida, color="red", label="DU - Demanda Ultrapassada", width=barWidth)
        plt.hlines(y=dem_cont, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='black', linestyle='dashed',
                   label=f"DC - Demanda Contratada: {dem_cont} kW")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 1, xmax=x_axis[11] + 1, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        # plt.title("Histórico de consumo por mês")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        plt.show()

    def graf_ajuste_verde(self, dem_medida_fp, dem_medida_p, dem_cont):
        lista_tolerancia_fp, lista_ultrapassagem_fp, lista_sobra_fp = metodos.dem_faturada(dem_medida_fp, dem_cont)
        lista_tolerancia_p, lista_ultrapassagem_p, lista_sobra_p = metodos.dem_faturada(dem_medida_p, dem_cont)
        tolerancia = dem_cont * 1.05
        barWidth = 0.3

        # DEMANDA CONTRATADA FORA DE PONTA
        for i in range(0, 12):
            if dem_medida_fp[i] <= dem_cont:
                lista_sobra_fp[i] = dem_cont - dem_medida_fp[i]
            elif (dem_medida_fp[i] <= tolerancia) and (dem_medida_fp[i] > dem_cont):
                lista_tolerancia_fp[i] = dem_medida_fp[i] - dem_cont
            elif dem_medida_fp[i] > tolerancia:  # Calculo para encontrar demanda de ultrapassagem
                lista_ultrapassagem_fp[i] = dem_medida_fp[i] - dem_cont

        # DEMANDA CONTRATADA PONTA
        for i in range(0, 12):
            if dem_medida_p[i] <= dem_cont:
                lista_sobra_p[i] = dem_cont - dem_medida_p[i]
            elif (dem_medida_p[i] <= tolerancia) and (dem_medida_p[i] > dem_cont):
                lista_tolerancia_p[i] = dem_medida_p[i] - dem_cont
            elif dem_medida_p[i] > tolerancia:  # Calculo para encontrar demanda de ultrapassagem
                lista_ultrapassagem_p[i] = dem_medida_p[i] - dem_cont
        # set width bar
        plt.figure(figsize=(12, 8))
        # set position of bar on X axis
        x_axis = np.arange(len(self.meses))
        # PLOT FORA DE PONTA
        plt.bar(x_axis - 0.21, dem_medida_fp, color="blue", label="DM FPonta", width=barWidth, edgecolor='black')
        plt.bar(x_axis - 0.21, lista_sobra_fp, bottom=dem_medida_fp, color="gray", label="DS", width=barWidth)
        plt.bar(x_axis - 0.21, lista_ultrapassagem_fp, bottom=dem_medida_fp, color="red", label="DU", width=barWidth)
        # PLOT PONTA
        plt.bar(x_axis + 0.21, dem_medida_p, color="green", label="DM Ponta", width=barWidth, edgecolor='black', capsize=7)
        plt.bar(x_axis + 0.21, lista_sobra_p, bottom=dem_medida_p, color="gray", width=barWidth)
        plt.bar(x_axis + 0.21, lista_ultrapassagem_p, bottom=dem_medida_p, color="red", width=barWidth)
        plt.hlines(y=dem_cont, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='black', linestyle='dashed',
                   label=f"DC: {dem_cont} kW")
        plt.hlines(y=tolerancia, xmin=x_axis[0] - 0.5, xmax=x_axis[11] + 0.5, colors='orange', linestyle='dashed',
                   label=f"Tolerância: {tolerancia} kW")
        plt.xticks(x_axis, self.meses)
        plt.legend(loc=3)
        # plt.title("Histórico de consumo por mês")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        plt.show()

##  PROXIMO GRAFICO: GRAF_AJUSTE_AZUL

if __name__ == "__main__":
    # DECLARANDO AS VARIÁVEIS - DM
    dem_medp = [21.25, 25.78, 29.32, 70.45, 46.44, 81.08, 53.72, 12.2, 68.09, 0, 39.75, 40.54]
    dem_medfp = [105.87, 89.93, 86, 86.59, 91.31, 112.76, 131.46, 146.61, 137.95, 155.47, 115.32, 98.79]
    # DECLARANDO AS VARIÁVEIS - DC
    dem_cont_fp = 170
    dem_cont_p = 50
    # DECLARANDO AS VARIÁVEIS - TARIFAS FP - COM TRIBUTO
    tar_dem_fp_ct = 21.127798
    tar_dem_p_ct = None
    tar_cons_fp = 0.33929
    tar_cons_p = 1.287010
    # DECLARANDO AS VARIÁVEIS - TARIFAS FP - SEM TRIBUTO
    tar_dem_fp_st = 14.615313
    tar_dem_p_st = None
    # ESTRUTURA TARIFÁRIA
    mod_tar = "convencional"
    subgrupo = "a4"
    # INSTANCIANDO OS OBJETOS
    metodos = Methods(dem_contfp=dem_cont_fp, dem_contp=dem_cont_p, dem_med_fponta=dem_medfp,
                      tarifa_dem_fponta_ct=tar_dem_fp_ct, tarifa_dem_fponta_st=tar_dem_fp_st,
                      tarifa_cons_fponta=tar_cons_fp, dem_med_ponta=dem_medp, tarifa_cons_ponta=tar_cons_p,
                      tarifa_dem_ponta_ct=tar_dem_p_ct, tarifa_dem_ponta_st=tar_dem_p_st,
                      mod_tar=mod_tar, subgrupo=subgrupo)

    graficos = Graphics(dmfp=dem_medfp, dmp=dem_medp, dcfp=170, dcp=50)
    # APLICANDO OS MÉTODOS
    #graficos.dem_medida_atual_convencional(dem_medida_fp=dem_medfp, dem_medida_p=dem_medp, dem_cont=dem_cont_fp)
    #graficos.dem_medida_atual_verde(dem_medida_fp=dem_medfp, dem_medida_p=dem_medp, dem_cont=dem_cont_fp)
    #graficos.graf_ajuste_convencional(dem_medfp, 170)
    #graficos.graf_ajuste_verde(dem_medfp, dem_medp, dem_cont_fp)
