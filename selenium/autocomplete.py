  
    
import sys
from PyQt5.QtWidgets import *
 
 
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
 
        names = ["네이버", "삼성", "쿠팡", "토스", "카카오","현대","포스텍","넥슨","넷마블"]
        completer = QCompleter(names)
 
        self.line_edit = QLineEdit()
        self.line_edit.setCompleter(completer)
 
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        self.setLayout(layout)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
