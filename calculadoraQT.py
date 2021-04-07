# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from action import *
# from calculadoraApp import Func





    
# QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it(""))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 494)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Display_output_label = QLabel(self.centralwidget)
        self.Display_output_label.setGeometry(QRect(10, 20, 311, 61))
        font = QFont()
        font.setPointSize(28)
        self.Display_output_label.setFont(font)
        self.Display_output_label.setFrameShape(QFrame.Box)
        self.Display_output_label.setFrameShadow(QFrame.Raised)
        self.Display_output_label.setLineWidth(2)
        self.Display_output_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Display_output_label.setObjectName("Display_output_label")

        self.botao_0  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("0") )
        self.botao_1  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("1") )
        self.botao_2  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("2") )
        self.botao_3  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("3") )
        self.botao_4  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("4") )
        self.botao_5  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("5") )
        self.botao_6  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("6") )
        self.botao_7  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("7") )
        self.botao_8  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("8") )
        self.botao_9  = QPushButton(self.centralwidget, clicked = lambda: self.press_it("9") )

        self.soma = QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.subtracao = QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.divisao = QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.multiplicacao = QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.potencia = QPushButton(self.centralwidget, clicked = lambda: self.press_it("^"))
        self.porcentagem = QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.fatorial = QPushButton(self.centralwidget, clicked = lambda: self.press_it("!"))
        self.igual = QPushButton(self.centralwidget, clicked = lambda: self.operacoes())

        self.ponto = QPushButton(self.centralwidget, clicked = lambda: self.press_dot() )
        self.parenteses_esq = QPushButton(self.centralwidget, clicked = lambda: self.press_it(")") )
        self.voltar_casa_dec = QPushButton(self.centralwidget, clicked = lambda: self.remove() )
        self.parenteses = QPushButton(self.centralwidget, clicked = lambda: self.press_it("(") )
        self.limpar = QPushButton(self.centralwidget, clicked = lambda: self.press_it("C") )
        self.positivo_negativo = QPushButton(self.centralwidget, clicked = lambda: self.neg_pos() )

        # self.botao_0 = QPushButton(self.centralwidget, clicked = lambda: self.press_it("0") )
        self.botao_0.setGeometry(QRect(100, 400, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_0.setFont(font)
        self.botao_0.setObjectName("botao_0")

        # self.botao_1 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("1"))
        self.botao_1.setGeometry(QRect(30, 340, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_1.setFont(font)
        self.botao_1.setObjectName("botao_1")

        # self.botao_2 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("2"))
        self.botao_2.setGeometry(QRect(100, 340, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_2.setFont(font)
        self.botao_2.setObjectName("botao_2")

        # self.botao_3 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("3"))
        self.botao_3.setGeometry(QRect(170, 340, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_3.setFont(font)
        self.botao_3.setObjectName("botao_3")

        # self.botao_4 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("4"))
        self.botao_4.setGeometry(QRect(30, 280, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_4.setFont(font)
        self.botao_4.setObjectName("botao_4")

        # self.botao_5 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("5"))
        self.botao_5.setGeometry(QRect(100, 280, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_5.setFont(font)
        self.botao_5.setObjectName("botao_5")

        # self.botao_6 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("6"))
        self.botao_6.setGeometry(QRect(170, 280, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_6.setFont(font)
        self.botao_6.setObjectName("botao_6")

        # self.botao_7 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("7"))
        self.botao_7.setGeometry(QRect(30, 220, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_7.setFont(font)
        self.botao_7.setObjectName("botao_7")

        # self.botao_8 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("8"))
        self.botao_8.setGeometry(QRect(100, 220, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_8.setFont(font)
        self.botao_8.setObjectName("botao_8")

        # self.botao_9 = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("9"))
        self.botao_9.setGeometry(QRect(170, 220, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.botao_9.setFont(font)
        self.botao_9.setObjectName("botao_9")

        # self.igual = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("="))
        self.igual.setGeometry(QRect(240, 400, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.igual.setFont(font)
        self.igual.setObjectName("igual")

        # self.porcentagem = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("%"))
        self.porcentagem.setGeometry(QRect(170, 100, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.porcentagem.setFont(font)
        self.porcentagem.setObjectName("porcentagem")

        # self.soma = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("+"))
        self.soma.setGeometry(QRect(240, 340, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.soma.setFont(font)
        self.soma.setObjectName("soma")

        # self.subtracao = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("-"))
        self.subtracao.setGeometry(QRect(240, 280, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.subtracao.setFont(font)
        self.subtracao.setObjectName("subtracao")

        # self.multiplicacao = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("*"))
        self.multiplicacao.setGeometry(QRect(240, 220, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.multiplicacao.setFont(font)
        self.multiplicacao.setObjectName("multiplicacao")

        # self.fatorial = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("!"))
        self.fatorial.setGeometry(QRect(240, 100, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.fatorial.setFont(font)
        self.fatorial.setObjectName("fatorial")

        # self.potencia = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("^"))
        self.potencia.setGeometry(QRect(100, 100, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.potencia.setFont(font)
        self.potencia.setObjectName("potencia")

        # self.limpar = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("C"))
        self.limpar.setGeometry(QRect(30, 100, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.limpar.setFont(font)
        self.limpar.setObjectName("limpar")

        # self.ponto = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("."))
        self.ponto.setGeometry(QRect(170, 400, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.ponto.setFont(font)
        self.ponto.setObjectName("ponto")

        # self.positivo_negativo = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("+/-"))
        self.positivo_negativo.setGeometry(QRect(30, 400, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.positivo_negativo.setFont(font)
        self.positivo_negativo.setObjectName("positivo_negativo")

        

        # self.voltar_casa_dec = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("<<"))
        self.voltar_casa_dec.setGeometry(QRect(100, 160, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.voltar_casa_dec.setFont(font)
        self.voltar_casa_dec.setObjectName("voltar_casa_dec")

        # self.parenteses_esq = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it(","))
        self.parenteses_esq.setGeometry(QRect(170, 160, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.parenteses_esq.setFont(font)
        self.parenteses_esq.setObjectName("parenteses_esq")

        # self.divisao = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("/"))
        self.divisao.setGeometry(QRect(240, 160, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.divisao.setFont(font)
        self.divisao.setObjectName("divisao")

        # self.parenteses = QPushButton(self.centralwidget, clicked = lambda: Funcoes.press_it("()"))
        self.parenteses.setGeometry(QRect(30, 160, 61, 51))
        font = QFont()
        font.setPointSize(17)
        self.parenteses.setFont(font)
        self.parenteses.setObjectName("parenteses")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_1.setText(_translate("MainWindow", "1"))
        self.botao_2.setText(_translate("MainWindow", "2"))
        self.botao_3.setText(_translate("MainWindow", "3"))
        self.botao_5.setText(_translate("MainWindow", "5"))
        self.botao_6.setText(_translate("MainWindow", "6"))
        self.botao_4.setText(_translate("MainWindow", "4"))
        self.botao_8.setText(_translate("MainWindow", "8"))
        self.botao_9.setText(_translate("MainWindow", "9"))
        self.botao_7.setText(_translate("MainWindow", "7"))
        self.botao_0.setText(_translate("MainWindow", "0"))
        self.igual.setText(_translate("MainWindow", "="))
        self.porcentagem.setText(_translate("MainWindow", "%"))
        self.soma.setText(_translate("MainWindow", "+"))
        self.subtracao.setText(_translate("MainWindow", "-"))
        self.multiplicacao.setText(_translate("MainWindow", "*"))
        self.fatorial.setText(_translate("MainWindow", "!"))
        self.potencia.setText(_translate("MainWindow", "^"))
        self.limpar.setText(_translate("MainWindow", "C"))
        self.ponto.setText(_translate("MainWindow", "."))
        self.positivo_negativo.setText(_translate("MainWindow", "+/-"))
        self.Display_output_label.setText(_translate("MainWindow", "0"))
        self.voltar_casa_dec.setText(_translate("MainWindow", "<<"))
        self.parenteses_esq.setText(_translate("MainWindow", ")"))
        self.divisao.setText(_translate("MainWindow", "/"))
        self.parenteses.setText(_translate("MainWindow", "("))

    def operacoes(self):
        scr = self.Display_output_label.text()        
        try:    
            answ = eval(calculate(scr))
            self.Display_output_label.setText(str(answ))
        except:
            self.Display_output_label.setText("ERRO!!!")

    def neg_pos(self):
        scr = self.Display_output_label.text()
        if "-" == scr:
            self.Display_output_label.setText(scr.replace("-", ""))
        else:
            self.Display_output_label.setText(f'-{scr}')

    def remove(self):
        scr = self.Display_output_label.text()
        scr = scr[:-1]
        self.Display_output_label.setText(scr)

    def press_dot(self):
        scr = self.Display_output_label.text()
        if scr[-1] == ".":
            pass
        else:
            self.Display_output_label.setText(f'{scr}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.Display_output_label.setText("0")
        else:
            if self.Display_output_label.text() == "0":
                self.Display_output_label.setText("")
            self.Display_output_label.setText(f'{self.Display_output_label.text()}{pressed}')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())