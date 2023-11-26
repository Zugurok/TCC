import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QWidget


class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        # Matplotlib script

        t = np.arange(0, 2, 0.01)
        s = -1 + np.sin(2 * np.pi * t)

        self.ax.plot(t, s)
        self.ax.set(xlabel='time(s)', ylabel='voltage(mV)',
               title='About as simple as it gets, folks')
        self.ax.grid()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)

        chart = Canvas(self)


appr = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(appr.exec_())


app = Tk()
app.title("Análise")

# Resolução da janela Tk
largura = 1800
altura = 900

# Resolução da tela do computador
largura_screen = int(app.winfo_screenwidth())
altura_screen = int(app.winfo_screenheight())

# Posição da janela na tela = Centro
posx = int(largura_screen/2 - largura/2)
posy = int(altura_screen/2 - altura/2 - 30)

# Definir Geometry da tela e local de abertura
app.geometry(f"{largura}x{altura}+{posx}+{posy}")

# Criar figura
figura = plt.Figure(figsize={8, 4}, dpi=60)
ax = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, app)
canva.get_tk_widget().grid(row=0, column=0)







app.mainloop()
