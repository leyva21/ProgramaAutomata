import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow
from ventana import Ui_MainWindow

abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num=["0","1","2","3","4","5","6","7","8","9"]
guion=["-"]

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.verificar_cadena)
        self.ui.pushButton_2.clicked.connect(self.reset_window)
        self.reset_window()
    def verificar_cadena(self):
        cadena = self.ui.lineEdit.text()
        cad = list(cadena)
        if(len(cad)== 9):
            self.estado0(cad)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)   
    #C
    def estado0(self, cad):
        if(cad[0]==abc[2]):
            self.estado1(cad)
            resultado = f"Q0"
            self.ui.label_2.setText(resultado)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)
    #E...L
    def estado1(self, cad):
        if cad[1] in abc[4:12]:
            self.estado2(cad)
            resultado2 = f"->Q1"
            self.ui.label_3.setText(resultado2)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)
    #  -          
    def estado2(self, cad):
        if(cad[2]==guion[0]):
            self.estado3(cad)
            resultado3 = f"->Q2"
            self.ui.label_4.setText(resultado3)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)
    # 0
    def estado3(self, cad):
        if(cad[3]==num[0]):
            self.estado4(cad)
            resultado4 = f"->Q3"
            self.ui.label_5.setText(resultado4)
        else:
            for i in range(1, 10):
                if(cad[3]==num[i]):
                    self.estado10(cad)
                    break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
                print("aqui esta el error")
    # 0
    def estado4(self, cad):
        
        if(cad[4]==num[0]):
            self.estado5(cad)
            resultado5 = f"->Q4"
            self.ui.label_6.setText(resultado5)
        else:
            for i in range(1, 10):
                if(cad[4]==num[i]):
                    self.estado11(cad)
                    break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
    # 0
    def estado5(self, cad):
        if(cad[5]==num[0]):
            resultado6 = f"->Q5"
            self.ui.label_7.setText(resultado6)
            self.estado6(cad)
        else:
            for i in range(1, 10):
                if(cad[5]==num[i]): 
                    self.estado12(cad)
                    break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
    # 1-9
    def estado6(self, cad):
        for i in range(1, 10):
            if(cad[6]==num[i]):
                resultado7 = f"->Q6"
                self.ui.label_8.setText(resultado7)
                self.estado7(cad)
                break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
    # -
    def estado7(self, cad):
        if(cad[7]==guion[0]):
            resultado8 = f"->Q7"
            self.ui.label_9.setText(resultado8)
            self.estado8(cad)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)
    #A...Z
    def estado8(self, cad):
        if cad[8] in abc[0:26]:
            resultado9 = f"->Q11"
            self.ui.label_10.setText(resultado9)
            self.estado9(cad)
        else:
            resultado = f"Cadena no valida"
            self.ui.label_14.setText(resultado)
    #Final
    def estado9(self, cad):
        resultado10 = f"->Q12"
        self.ui.label_11.setText(resultado10)   
    def estado10(self, cad):
        for i in range(0, 10):
            if(cad[4]==num[i]):
                resultado11 = f"->Q8"
                self.ui.label_5.setText(resultado11)
                resultado12 = f"->Q3"
                self.ui.label_15.setText(resultado12)
                self.estado11(cad)
                break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
    def estado11(self, cad):
        for i in range(0, 10):
            if(cad[5]==num[i]):
                resultado12 = f"->Q9"
                self.ui.label_6.setText(resultado12)
                self.estado12(cad)
                break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado) 
    def estado12(self, cad):
        for i in range(0, 10):
            if(cad[6]==num[i]):
                resultado13 = f"->Q10"
                self.ui.label_7.setText(resultado13)
                self.estado7(cad)
                break
            else:
                resultado = f"Cadena no valida"
                self.ui.label_14.setText(resultado)
    def reset_window(self):
        self.ui.lineEdit.clear()
        self.ui.label_2.setText("")
        self.ui.label_3.setText("")
        self.ui.label_4.setText("")
        self.ui.label_5.setText("")
        self.ui.label_6.setText("")
        self.ui.label_7.setText("")
        self.ui.label_8.setText("")
        self.ui.label_9.setText("")
        self.ui.label_10.setText("")
        self.ui.label_11.setText("")
        self.ui.label_15.setText("")
        self.ui.label_14.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec_())
