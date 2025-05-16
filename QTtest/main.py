from PyQt6.QtWidgets import QTableWidgetItem,QTableWidget, QTextEdit,QDialog, QMessageBox, QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation
from PyQt6.QtGui import QIcon, QFont,QPixmap
import sys


DISCOUNT = 0

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

class DialogDISCOUNT(QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("DialogDISCOUNT")
            
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


class DialogERROR(QMainWindow):
    def __init__(self):
            super().__init__()
            
            self.setWindowTitle("DialogDISCOUNT")
            
            self.label1 = QLabel("INVALID VALUE",self)
            self.label1.setGeometry(62,10,100,20) 
            self.btnOK = QPushButton("OK",self)
            self.btnOK.setGeometry(50,50,100,20) 
            self.btnOK.clicked.connect(self.close2)    
            
    def close2(self):
        self.close()
        
class DialogBUFFER(QMainWindow):
    def __init__(self):
            super().__init__()
            
            self.setWindowTitle("buffer")
            
            self.label1 = QLabel("There is nothing in buffer",self)
            self.label1.setGeometry(30,10,200,20) 
            self.btnOK = QPushButton("OK",self)
            self.btnOK.setGeometry(50,50,100,20) 
            self.btnOK.clicked.connect(self.close2)    
            
    def close2(self):
        
        self.close()
         
class WorkTable(QMainWindow):
        def __init__(self):
            super().__init__()
            
            self.main_window = None 
            
            self.buffer_check = []
            self.NUM_CLIENT = 0
            self.rows = 0
            self.value = 0
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
            self.label2.setGeometry(366, 0, 220, 23)
            
            self.label4 = QLabel("History",self)
            self.label4.setGeometry(386, 120, 100, 40) 
        
            self.BTN_apply2 = QPushButton("SAVE",self)
            self.BTN_apply2.setGeometry(354, 90, 40, 33)
            self.BTN_apply2.clicked.connect(self.save_value)
            
            self.BTN_apply3 = QPushButton("BACK",self)
            self.BTN_apply3.setGeometry(416, 90, 40, 33)
            self.BTN_apply3.clicked.connect(self.undo)
            
            self.BTN_exit = QPushButton("EXIT",self)
            self.BTN_exit.setGeometry(10, 460, 40, 33)
            self.BTN_exit.clicked.connect(self.exit_from)
            
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
            
            self.table = QTableWidget(self.rows, 1, self)  # 5 строк, 3 колонки
            self.table.setHorizontalHeaderLabels(["Sum cost"])
            self.table.setGeometry(356, 150, 100, 300) 
            
            self.label3 = QTextEdit(self.cost,self)
            font = QFont("Arial",8, QFont.Weight.Black)
            self.label3.setReadOnly(True)
            self.label3.setFont(font)
            self.label3.setGeometry(356, 50, 100, 33)

        def exit_from(self):
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        
        def undo(self):
            if self.buffer_check:
                VALUE = self.buffer_check[-1]
                self.check -= VALUE
                self.buffer_check.pop(-1) # Обновляем buffer_check
                self.label3.setText(str(self.check))  # Показываем актуальную сумму
            else:
                self.dialog2 = DialogBUFFER()
                self.dialog2.show()

        
        def save_value(self):
            if self.check!= 0:
                VALUE = self.check
                self.rows += 1
                self.table.setRowCount(self.rows)
                self.table.setItem(self.rows - 1,0,QTableWidgetItem(str(VALUE)))
                self.label3.setText('')
                self.NUM_CLIENT+=1
            if self.check == 0:
                self.error()
            self.check = 0
        
        def add_disc(self):
            self.dialog = DialogDISCOUNT()
            self.dialog.show()
            
        def error(self):
            self.dialog2 = DialogERROR()
            self.dialog2.show()
            
        def on_selection_change(self)->None:
            self.current_choice = self.combo.currentText()
            
        def add_value(self):
            for key,value in self.stuff.items():
                if self.current_choice == value:   
                    self.buffer_check.append(key)
                    self.check+=key
            self.cost = str(self.check)
            self.label3.setText(self.cost)
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()