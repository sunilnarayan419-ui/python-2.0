# PyQt5 introduction 

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QLabel, QVBoxLayout, QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MaiWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY COOL FIRST GUI")
        self.setGeometry(700,300, 500,500)
        self.setWindowIcon(QIcon("profile_pic.jpg"))    
          
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial",30))    
        label.setGeometry(0,0,300,500)
        label.setStyleSheet("color : #292929;" 
                            "background_color : 6fdc7;"
                            "font-Weight: bold;"
                           "font-style : italic;"
                           "text-decoration: underline;")
        
    #label.setAlignment(Qt.AlignTop) # VERTICALLY TOP 
    #label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM 
    #label.setAlignment(Qt.AlignCenter) # VERTICALLY CENTER 
    
    #label.setAlignment(Qt.AlignRight) # VERTICALLY RIGHT  
    #label.setAlignment(Qt.AlignLeft) # VERTICALLY LEFT  
        
def main():
    app = QApplication(sys.argv) 
    window = MaiWindow()
    window.show()
    sys.exit(app.exec_())    

if __name__ == " __main__":
    main()