from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
import sys
import main
from PyQt6.QtWidgets import QDialog, QMessageBox, QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation
from PyQt6.QtGui import QIcon, QFont,QPixmap
import sys

DISCOUNT = 0

if __name__ == "__main__":

    



    class NEWbcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Hi!")
            self.setFixedSize(300,500)
            
            self.label = QLabel("Market mananger tool",self)
            font = QFont("Arial",8, QFont.Weight.Black)
            self.label.setFont(font)
            self.label.setGeometry(86, 0, 200, 23)

            self.btn = QPushButton("Procedure with client",self)
            self.btn.setGeometry(50, 20, 200, 23) 
            self.btn.clicked.connect(self.btn1_handler)
            
            self.btn2 = QPushButton("Watch statistics",self)
            self.btn2.setGeometry(50, 60, 200, 23) 
            self.btn2.clicked.connect(self.btn2_handler)
            
            self.btn3 = QPushButton("Exit",self)
            self.btn3.setGeometry(50, 100, 200, 23) 
            self.btn3.clicked.connect(self.btn3_handler)

            self.label2 = QLabel(self)
            self.label2.setFont(font)
            self.label2.setGeometry(80, 300, 2002, 200)
            
            self.pixmap = QPixmap(r"C:/Users/rulko/Desktop/14-148130_minion-imagenes-de-100x100-pixeles.jpg")
            self.label2.setPixmap(self.pixmap)
            
            self.SecWin  = None

        def btn1_handler(self):
            if self.SecWin is None: 
                self.SecWin = WorkTable()
            self.close()
            self.SecWin.show()
            

        def btn2_handler(self):
            print("fuck")
            
        def btn3_handler(self):
            window.close()

    class Dialog(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Dialog")
                
                self.label1 = QLabel("enter your discount",self)
                self.label1.setGeometry(50,0,300,40)
                
                self.input = QLineEdit(self)
                self.input.setGeometry(50,30,100,20) 
                
                self.btnOK = QPushButton("OK",self)
                self.btnOK.setGeometry(50,50,100,20)
                self.btnOK.clicked.connect(self.end_close)
                
        def end_close(self):
            global DISCOUNT
            if DISCOUNT!= 0:
                try:
                    DISCOUNT = int(self.input.text)
                except UnboundLocalError:
                    print("invalid input")
                    self.end_close()
            self.close()
                
            
    class WorkTable(QMainWindow):
            def __init__(self):
                super().__init__()
                
                self.check = 0
                self.stuff = {100:"apple",200:"tomato",170:"Coke",232:"Cheese",500:"Wine"}
                self.current_choice = self.stuff.get(100)
                self.cost = str(self.check)
                
                self.setWindowTitle("Second window!")
                self.setFixedSize(500,500)
                
                self.label = QLabel("working with table",self)
                font = QFont("Arial",8, QFont.Weight.Black)
                self.label.setFont(font)
                self.label.setGeometry(56, 0, 200, 23)
                
                self.label2 = QLabel("current cost",self)
                font = QFont("Arial",8, QFont.Weight.Black)
                self.label2.setFont(font)
                self.label2.setGeometry(336, 0, 200, 23)
                
                self.label3 = QLabel(self.cost,self)
                font = QFont("Arial",8, QFont.Weight.Black)
                self.label3.setFont(font)
                self.label3.setGeometry(356, 50, 200, 23)
                
                self.combo = QComboBox(self)
                self.combo.addItems(self.stuff.values())
                self.combo.setGeometry(10, 50, 200, 30)
                self.combo.currentIndexChanged.connect(self.on_selection_change)
                
                self.BTN_apply = QPushButton("Add in check",self)
                self.BTN_apply.setGeometry(10,90,200,20)
                self.BTN_apply.clicked.connect(self.add_value)
                
                self.BTN_disc = QPushButton("Add discount",self)
                self.BTN_disc.setGeometry(10,120,200,20)
                self.BTN_disc.clicked.connect(self.add_disc)
                
            def add_disc(self):
                self.dialog = Dialog()
                self.dialog.show()
                
            def on_selection_change(self)->None:
                self.current_choice = self.combo.currentText()
                
            def add_value(self):
                for key,value in self.stuff.items():
                    if self.current_choice == value:   
                        self.check+=key
                self.cost = str(self.check)
                self.label3.setText(self.cost)
                
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            app.exec()
