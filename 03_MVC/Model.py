import matplotlib.pyplot as plt
import numpy as np


class Methods:
    def __init__(self, dem_contfp=0, dem_contp=0, dem_med_fponta=None, dem_med_ponta=None, consumo_fponta=None, consumo_ponta=None,
                 tarifa_dem_fponta_ct=None, tarifa_dem_fponta_st=None, tarifa_dem_ponta_ct=None, elev_carga=None,
                 tarifa_dem_ponta_st=None, tarifa_cons_fponta=None, tarifa_cons_ponta=None, mod_tar=""):

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
        self.ultrapassagem = [0] * 12
        self.sobra = [0] * 12
        self.toleranciafp = dem_contfp * 1.05
        self.toleranciap = dem_contp * 1.05
        self.lista_tolerancia = [0] * 12
        self.multafp = [0] * 12
        self.multap = [0] * 12
        self.dem_graf = [0] * 12
        self.dem_fat = [0] * 12
        self.piscofins = 0.05
        self.icms = 0.18

    def graf_inicial(self):
        dm = self.dem_med_fponta
        meses = self.meses
        lista_dc = self.lista_Dcfp
        dcfp = self.dem_contfp

        plt.figure(figsize=(12, 6))
        plt.bar(meses, dm, color="blue", label="DM - Demanda Medida")
        plt.hlines(y=lista_dc, xmin=meses[0], xmax=meses[11], colors='black', linestyle='dashed',
                   label=f"DC - Demanda Contratada: {float(dcfp)}")
        plt.hlines(y=self.toleranciafp, xmin=meses[0], xmax=meses[11], colors='orange', linestyle='dashed',
                   label=f"Tolerância: {self.toleranciafp}")
        plt.legend(loc=3)
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        return plt.show()

    def dem_n_con(self):
        dem_medida = self.dem_med_fponta

        for i in range(0, 12):
            if dem_medida[i] <= self.dem_contfp:
                self.sobra[i] = self.dem_contfp - dem_medida[i]
        return self.sobra

    def dem_tol(self):
        dem_medida = self.dem_med_fponta

        for i in range(0, 12):
            if (dem_medida[i] <= self.toleranciafp) and (dem_medida[i] > self.dem_contfp):
                self.lista_tolerancia[i] = dem_medida[i] - self.dem_contfp
        return self.lista_tolerancia

    def dem_ult(self):
        dem_medida = self.dem_med_fponta

        for i in range(0, 12):
            if dem_medida[i] > self.toleranciafp:
                self.ultrapassagem[i] = dem_medida[i] - self.dem_contfp
                dem_medida[i] = self.dem_contfp
                self.multafp[i] = self.ultrapassagem[i] * 2
        return self.multafp

    def graf_ajust(self):
        dem_medida = self.dem_med_fponta
        lista_sobra = [0] * 12
        lista_ultrapassagem = [0] * 12
        lista_multa = [0] * 12
        lista_tolerancia = [0] * 12

        for i in range(0, 12):
            if dem_medida[i] <= self.dem_contfp:
                lista_sobra[i] = self.dem_contfp - dem_medida[i]
            elif (dem_medida[i] <= self.toleranciafp) and (dem_medida[i] > self.dem_contfp):
                lista_tolerancia[i] = dem_medida[i] - self.dem_contfp
            elif dem_medida[i] > self.toleranciafp:  # Calculo para encontrar demanda de ultrapassagem
                lista_ultrapassagem[i] = dem_medida[i] - self.dem_contfp
                dem_medida[i] = self.dem_contfp
                lista_multa[i] = lista_ultrapassagem[i] * 2

        plt.figure(figsize=(12, 6))
        plt.bar(self.meses, dem_medida, color="blue", label="DM - Demanda Medida")
        plt.bar(self.meses, lista_sobra, bottom=dem_medida, color="gray", label="DS - Demanda não utilizada")
        plt.bar(self.meses, lista_multa, bottom=dem_medida, color="red", label="DU - Demanda de Ultrapassagem")
        plt.hlines(y=self.dem_contfp, xmin=self.meses[0], xmax=self.meses[11], colors='black', linestyle='dashed',
                   label=f"DC - Demanda Contratada: {self.dem_contfp} kW")
        plt.hlines(y=self.toleranciafp, xmin=self.meses[0], xmax=self.meses[11], colors='orange', linestyle='dashed',
                   label=f"Tolerância: {self.toleranciafp} kW")
        plt.legend()
        # plt.title("Histórico de consumo por mês")
        plt.xlabel('Ano (Meses)')
        plt.ylabel('Demanda Medida (kW)')
        plt.show()

    def fat_tol(self):
        """
        Faturamento da demanda medida no limite tolerância
        :return:
        """
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
    def __init__(self):
        super(Methods).__init__()

    def demanda_medida(self):
        dmfp = metodos.dem_med_fponta
        dmp = metodos.dem_med_ponta
        meses = metodos.meses
        lista_dcfp = metodos.lista_Dcfp
        lista_dcp = metodos.lista_Dcp
        dcfp = metodos.dem_contfp
        dcp = metodos.dem_contp
        mod_tar = metodos.mod_tar
        toleranciafp = metodos.toleranciafp
        toleranciap = metodos.toleranciap
        barWidth = 0.4

        if mod_tar == "convencional":
            # set width bar
            plt.figure(figsize=(12, 6))

            # set position of bar on X axis
            x_axis = np.arange(len(meses))

            # Make the plot
            plt.bar(x_axis - 0.2, dmfp, color="blue", label="DM FP", width=barWidth)
            plt.bar(x_axis + 0.2, dmp, color="green", label="DM P", width=barWidth)
            plt.hlines(y=lista_dcfp, xmin=x_axis[0], xmax=x_axis[11], colors='black', linestyle='dashed',
                       label=f"DC - Demanda Contratada: {float(dcfp)}")
            plt.hlines(y=toleranciafp, xmin=x_axis[0], xmax=x_axis[11], colors='orange', linestyle='dashed',
                       label=f"Lim. Tolerância: {toleranciafp}")
            plt.xticks(x_axis, meses)
            plt.legend(loc=3)
            plt.xlabel('Ano (Meses)')
            plt.ylabel('Demanda Medida (kW)')
            return plt.show()

        elif mod_tar == "verde":
            # set width bar
            plt.figure(figsize=(12, 6))

            # set position of bar on X axis
            x_axis = np.arange(len(meses))

            # Make the plot
            plt.bar(x_axis - 0.2, dmfp, color="blue", label="DM FP", width=barWidth)
            plt.bar(x_axis + 0.2, dmp, color="green", label="DM P", width=barWidth)
            plt.hlines(y=lista_dcfp, xmin=x_axis[0], xmax=x_axis[11], colors='black', linestyle='dashed',
                       label=f"DC - Demanda Contratada: {float(dcfp)}")
            plt.hlines(y=toleranciafp, xmin=x_axis[0], xmax=x_axis[11], colors='orange', linestyle='dashed',
                       label=f"Lim. Tolerância: {toleranciafp}")
            plt.xticks(x_axis, meses)
            plt.legend(loc=3)
            plt.xlabel('Ano (Meses)')
            plt.ylabel('Demanda Medida (kW)')
            return plt.show()

        elif mod_tar == "azul":
            # set width bar
            plt.figure(figsize=(12, 6))

            # set position of bar on X axis
            x_axis = np.arange(len(meses))

            # Make the plot
            plt.bar(x_axis - 0.2, dmfp, color="blue", label="DM FP", width=barWidth)  # DM FP
            plt.bar(x_axis + 0.2, dmp, color="green", label="DM P", width=barWidth)  # DM P
            # Fora de Ponta
            plt.hlines(y=lista_dcfp, xmin=x_axis[0], xmax=x_axis[11], colors='black', linestyle='dashed',
                       label=f"DC FP: {float(dcfp)}")  # DC FP
            plt.hlines(y=toleranciafp, xmin=x_axis[0], xmax=x_axis[11], colors='orange', linestyle='dashed',
                       label=f"Lim. Tolerância: {toleranciafp}")  # LimTol FP
            # Ponta
            plt.hlines(y=lista_dcp, xmin=x_axis[0], xmax=x_axis[11], colors='black', linestyle='solid',
                       label=f"DC P: {float(dcp)}")  # DC P
            plt.hlines(y=toleranciap, xmin=x_axis[0], xmax=x_axis[11], colors='orange', linestyle='solid',
                       label=f"Lim. Tolerância: {toleranciap}")  # LimTol P
            plt.xticks(x_axis, meses)
            plt.legend(loc=3)
            plt.xlabel('Ano (Meses)')
            plt.ylabel('Demanda Medida (kW)')
            return plt.show()

        else:
            print("Modalidade Tarifária Inválida")


if __name__ == "__main__":
    dem_medp = [21.25, 25.78, 29.32, 70.45, 46.44, 81.08, 53.72, 12.2, 68.09, 0, 39.75, 40.54]
    dem_medfp = [105.87, 89.93, 86, 86.59, 91.31, 112.76, 131.46, 146.61, 137.95, 155.47, 115.32, 98.79]
    metodos = Methods(dem_contfp=170, dem_contp=50, dem_med_fponta=dem_medfp, tarifa_dem_fponta_ct=21.127798,
                      tarifa_dem_fponta_st=14.615313, tarifa_cons_fponta=0.33929, dem_med_ponta=dem_medp,
                      tarifa_cons_ponta=1.287010, mod_tar="convencional")
    graficos = Graphics()
    graficos.demanda_medida()
