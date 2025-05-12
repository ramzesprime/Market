from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
import sys
import main


if __name__ == "__main__":

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Market menegment helper")
            self.setWindowIcon(QIcon("1.png"))
            btn1 = QPushButton("Push me!")
            btn1.clicked.connect(self.btn_clicked)
            self.setFixedSize(QSize(400, 300))
            self.setCentralWidget(btn1)
        
        def btn_clicked(self):
            msg = QMessageBox()
            msg.setWindowTitle("FUCKFUCKFUCK")
            msg.setText("Are you stupid?")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            
    app =  QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()
