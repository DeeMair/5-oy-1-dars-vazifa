import random
from ranglar import colors

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QPushButton, QWidget, QHBoxLayout, QVBoxLayout,
                             QListWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        vertical = QVBoxLayout()
        self.birinchi_bosilgan = None

        self.buttons = {}

        nums = list(range(1, 13))
        nums += nums
        random.shuffle(nums)

        print(nums)
        nums_index = 0
        for i in range(6):
            horizontal = QHBoxLayout()
            for j in range(4):
                btn = QPushButton("X")
                print(btn)

                btn.clicked.connect(self.almashtir)


                horizontal.addWidget(btn)

                self.buttons.update({btn: nums[nums_index]})
                nums_index+=1

            vertical.addLayout(horizontal)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)


    def almashtir(self):
        btn = self.sender()
        raqam = self.buttons.get(btn, -1)
        if raqam == -1:
            print("Xatolik bor!")

        if self.birinchi_bosilgan is None:
            self.birinchi_bosilgan = btn
            btn.setText(str(raqam))
        else:
            birinchi_raqam = self.buttons.get(self.birinchi_bosilgan)
            if birinchi_raqam != raqam:
                self.birinchi_bosilgan.setText("X")
                self.birinchi_bosilgan = None
                return
            btn.setText(str(raqam))
            color = colors.pop()
            if color is None:
                color = 'red'

            btn.setStyleSheet(f"background-color: {color}")
            self.birinchi_bosilgan.setStyleSheet(f"background-color: {color}")
            self.birinchi_bosilgan = None

app = QApplication([])

main_window = MainWindow()
main_window.show()

app.exec_()
