from PyQt6.QtWidgets import QTableWidgetItem,QTableWidget, QTextEdit,QDialog, QMessageBox, QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation
from PyQt6.QtGui import QIcon, QFont,QPixmap
import sys
import sqlite3
from PyQt6.QtCore import QTimer

DISCOUNT = 0
VALUES = []

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("SELECT name, price FROM items")
data = cursor.fetchall()

CURRENT_ACORTY = [row[0] for row in data]
CURRENT_ACORTY_COST = [row[1] for row in data]

conn.close()

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
        
        self.btn2 = QPushButton("Make a new value",self)
        self.btn2.setGeometry(50, 60, 200, 23) 
        self.btn2.clicked.connect(self.btn2_handler)
        
        self.btn3 = QPushButton("Exit",self)
        self.btn3.setGeometry(50, 100, 200, 23) 
        self.btn3.clicked.connect(self.exit_from)

        self.label2 = QLabel(self)
        self.label2.setFont(font)
        self.label2.setGeometry(80, 300, 2002, 200)
        
        self.pixmap = QPixmap(r"C:/Users/rulko/Desktop/14-148130_minion-imagenes-de-100x100-pixeles.jpg")
        self.label2.setPixmap(self.pixmap)
        
        self.ThirdWin = None
        self.SecWin  = None

    def exit_from(self):
            self.main_window = MainWindow()
            self.close()
    
    def btn1_handler(self):

        if self.SecWin is None: 
            self.SecWin = WorkTable()
        self.close()
        self.SecWin.show()
        
    def btn2_handler(self):
        if self.ThirdWin is None: 
            self.ThirdWin = Statistics()
        self.close()
        self.ThirdWin.show()
        

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


class DialogSUCCES(QMainWindow):
    def __init__(self,flag:int):
            super().__init__()
            
            self.setWindowTitle("DialogDISCOUNT")
            if flag == 1:
                self.label1 = QLabel("Succesfly added new value",self)
            elif flag == 2:
                self.label1 = QLabel("Succesfly clean all table",self)
            self.label1.setGeometry(32,10,140,20) 
            self.btnOK = QPushButton("OK",self)
            self.btnOK.setGeometry(50,50,100,20) 
            self.btnOK.clicked.connect(self.close2)    
            
    def close2(self):
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

VALUES = []

class WorkTable(QMainWindow):
        def __init__(self):
            super().__init__()

            self.my_init()
            
            self.main_window = None 
            
            self.buffer_check = []
            self.NUM_CLIENT = 0
            self.rows = 0
            self.value = 0
            self.check = 0
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
        
        def my_init(self):
            self.stuff = {}
            step = 0
            while step != len(CURRENT_ACORTY):
                self.stuff[CURRENT_ACORTY_COST[step]] = CURRENT_ACORTY[step]
                step +=1
            print(self.stuff)
            self.current_choice = self.stuff.get(100)
        
        def exit_from(self):
            print(VALUES)
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        
        def undo(self):
            if self.buffer_check:
                VALUE = self.buffer_check[-1]
                self.check -= VALUE
                self.buffer_check.pop(-1) 
                self.label3.setText(str(self.check))  
            else:
                self.dialog2 = DialogBUFFER()
                self.dialog2.show()

        def save_stats(self,VALUE):
            try:
                conn2 = sqlite3.connect("stats.db")
                cursor2 = conn2.cursor()

                cursor2.execute("SELECT amount FROM stats WHERE name = ?", (VALUE,))
                result = cursor2.fetchone()

                if result:  
                    cursor2.execute("UPDATE stats SET amount = amount + 1 WHERE name = ?", (VALUE,))
                    VALUES.append(VALUE)
                else:
                    cursor2.execute("INSERT INTO stats (name, amount) VALUES (?, ?)", (VALUE, 1))

                conn2.commit()
                conn2.close()

                print("Статистика обновлена")
            except Exception as e:
                print(f"Ошибка SQL: {e}")

        
        def save_value(self):
            if self.check!= 0:
                VALUE = self.check
                self.save_stats(VALUE)
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


class Statistics(QMainWindow):
        def __init__(self):
            super().__init__()
            
            self.text1:str
            self.text2:int
            
            self.main_window = None 
            self.setWindowTitle("statistics window!")
            self.setFixedSize(500,500)
            
            self.BTN_exit = QPushButton("EXIT",self)
            self.BTN_exit.setGeometry(10, 460, 40, 33)
            self.BTN_exit.clicked.connect(self.exit_from)
            
            self.MainTitle = QLabel("There is statistics",self)
            font = QFont("Arial",8, QFont.Weight.Black)
            self.MainTitle.setFont(font)
            self.MainTitle.setGeometry(200,20,110,33)
            
            self.input = QLineEdit(self)
            self.input.setPlaceholderText("Enter value")
            self.text1 = self.input.text() 
            self.input.setGeometry(10,50,100,30)
            
            self.input2 = QLineEdit(self)
            self.input2.setPlaceholderText("Enter price")
            self.text2 = self.input2.text() 
            self.input2.setGeometry(10,90,100,30)
            
            self.btn_SAVE = QPushButton("save",self)
            self.btn_SAVE.setGeometry(10,140,100,40)
            self.btn_SAVE.clicked.connect(self.save)
            
            self.btn_SAVE = QPushButton("clean all table",self)
            self.btn_SAVE.setGeometry(10,190,100,40)
            self.btn_SAVE.clicked.connect(self.clean)
        
        def clean(self):
            try:
                conn = sqlite3.connect("store.db") 
                cursor = conn.cursor()
                
                cursor.execute("DELETE FROM items")
                conn.commit()
                
                self.succes = DialogSUCCES(2)
                self.succes.show()

                conn.close()
            except Exception as e:
                print("erro with SQL")
        def save(self):
            try:

                conn = sqlite3.connect("store.db") 
                cursor = conn.cursor()

                new_name = self.input.text()
                new_price = self.input2.text()
                
                if not new_name or not new_price.isdigit():
                    self.error = DialogERROR()
                    self.error.show()
                    return

                new_price = int(new_price)

                cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (new_name, new_price))
                conn.commit()

                self.succes = DialogSUCCES(1)
                self.succes.show()

                cursor.execute("SELECT * FROM items WHERE name = ?", (new_name,))
                print(cursor.fetchone())
                self.input.clear()
                self.input2.clear()
                conn.close()
            except Exception as e:
                print(f"Ошибка SQL-запроса: {e}")
        def exit_from(self):
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

