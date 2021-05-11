import sys
from PyQt5.QtWidgets import *

class Mywindow(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.setGeometry(100, 200, 300, 400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon(""))
        btn = QPushButton("버튼1", self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_clicked)
    def btn_clicked(self):
        print("버튼 클릭")
    
        btn2 = QPushButton("버튼2", self)
        btn2.move(40,10)
        btn2.clicked.connect(self.btn_clicked2)
    def btn.clicked2(self):
        print("집에가자")

app = QApplication(sys.argv)
window =  Mywindow()
window.show()
app.exec_()

