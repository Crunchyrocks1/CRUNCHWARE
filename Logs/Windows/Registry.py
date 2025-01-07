import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class TransparentTextWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Running Text')
        self.setGeometry(100, 100, 200, 50)  
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground) 
        self.setFixedSize(200, 50)  # Fix the size of the window

        self.label = QLabel('Running', self)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop) 
        self.label.setStyleSheet('color: white; font-size: 16px;')  

    def mousePressEvent(self, event):
        self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TransparentTextWindow()
    window.show()

    sys.exit(app.exec_())
