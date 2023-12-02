from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generator)

    def generator(self):
        print(1)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()