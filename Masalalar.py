# from PyQt5.QtWidgets import QApplication, QLayout, QWidget, QWidgetItem, QLabel
#
# app = QApplication([])
# myWindow_style = """
#         QLabel{
#             font-size: 50px;
#             color: purple;
#         }
# """
#
#
# window = QWidget()
# window.setWindowTitle("MyWindow")
# window.setGeometry(700, 400, 300, 100)
#
# label = QLabel("Salom dunyo", parent=window)
# label.setStyleSheet(myWindow_style)
#
# window.show()
# app.exec_()

# from PyQt5.QtWidgets import QLabel, QApplication, QWidget
#
# app = QApplication([])
#
# myWindow_style = """
#         QLabel{
#             font-size: 100px;
#             color: red;
#         }
# """
#
# window = QWidget()
# window.setWindowTitle("MyWindow")
# window.setGeometry(700, 400, 400, 200)
#
# label = QLabel("Soxibjon", parent=window)
#
# label.setStyleSheet(myWindow_style)
# window.show()
# app.exec_()


"""Masalalar"""

"""1.Masala"""

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         vertical = QVBoxLayout()
#
#         label1 = QLabel("Nomi:Sherlock Holmes")
#         label2 = QLabel("Janri: Detective")
#         label3 = QLabel("Avtor: Arthur Konandoil")
#
#         vertical.addWidget(label1)
#         vertical.addWidget(label2)
#         vertical.addWidget(label3)
#
#         window = QWidget()
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
# window = MyWindow()
# window.show()
# app.exec_()

"""2.Masala"""

# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         label1 = QLabel("Nomi: Osh")
#         label2 = QLabel("Tarkibi: guruch, sabzi, piyoz, yog', go'sht, suv ")
#         label3 = QLabel("Retspeti: Avval Yog' quyamiz keyin go'sht solamiz keyin piyoz sabzi, undan keyin suv undan keyin guruch va osh tayyor")
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(label1)
#         vertical.addWidget(label2)
#         vertical.addWidget(label3)
#
#         window = QWidget()
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
# window = MyWindow()
# window.show()
# app.exec_()

"""3.Masala"""

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow
#
# app = QApplication([])
#
# class Mywindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         label1 = QLabel("Sevimli sport turim: Shaxmat")
#         label2 = QLabel("sevimli sportchim: CR7")
#         label3 = QLabel("Sevimli sportchimni sport turi: konkida uchish")
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(label1)
#         vertical.addWidget(label2)
#         vertical.addWidget(label3)
#
#         window = QWidget()
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
# window = Mywindow()
# window.show()
# app.exec_()

# """4.Masala"""


# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         label1 = QLabel("Videodarsliklar")
#         label2 = QLabel("Bolalarga masofadan ta'lim berish")
#         label3 = QLabel("Ertaga")
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(label1)
#         vertical.addWidget(label2)
#         vertical.addWidget(label3)
#
#         window = QWidget()
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
# window = MyWindow()
# window.show()
# app.exec_()

"""5.Masala"""

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLabel, QPushButton
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("********")
#         btn1 = QPushButton("Hayvon")
#         btn1.clicked.connect(self.get_hayvon)
#
#         btn2 = QPushButton("Rang")
#         btn2.clicked.connect(self.get_rang)
#
#         btn3 = QPushButton("Tug'ilgan shahar")
#         btn3.clicked.connect(self.get_shahar)
#
#         verticalca = QVBoxLayout()
#         verticalca.addWidget(self.label)
#         verticalca.addWidget(btn1)
#         verticalca.addWidget(btn2)
#         verticalca.addWidget(btn3)
#
#
#         window = QWidget()
#         window.setLayout(verticalca)
#         self.setCentralWidget(window)
#
#     def get_hayvon(self):
#         self.label.setText("Baliq")
#
#     def get_rang(self):
#         self.label.setText("qora")
#
#     def get_shahar(self):
#         self.label.setText("Farg'ona")
#
# window = MyWindow()
# window.show()
# app.exec_()


"""6.Masala"""

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel("************")
#
#         btn1 = QPushButton("Meva")
#         btn1.clicked.connect(self.get_meva)
#
#         btn2 = QPushButton("Film")
#         btn2.clicked.connect(self.get_film)
#
#         btn3 = QPushButton("Qo'shiqchi")
#         btn3.clicked.connect(self.get_artist)
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(self.label)
#         vertical.addWidget(btn1)
#         vertical.addWidget(btn2)
#         vertical.addWidget(btn3)
#
#         window = QWidget()
#         window.setWindowTitle("MyWindow")
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
#     def get_meva(self):
#         self.label.setText("shaftoli")
#
#     def get_film(self):
#         self.label.setText("Avengars")
#
#     def get_artist(self):
#         self.label.setText("Kosta")
#
# window = MyWindow()
# window.show()
# app.exec_()

"""7.Masalana"""

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
#
# app = QApplication([])
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel("********")
#
#         btn1 = QPushButton("Data - time")
#         btn1.clicked.connect(self.get_data)
#
#         btn2 = QPushButton("Food")
#         btn2.clicked.connect(self.get_food)
#
#         btn3 = QPushButton("Place")
#         btn3.clicked.connect(self.get_place)
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(self.label)
#         vertical.addWidget(btn1)
#         vertical.addWidget(btn2)
#         vertical.addWidget(btn3)
#
#         window = QWidget()
#         window.setWindowTitle("MyWindow")
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#
#     def get_data(self):
#         self.label.setText("22:08  22/08/2024")
#
#     def get_food(self):
#         self.label.setText("Shashlik")
#
#     def get_place(self):
#         self.label.setText("Farg'ona")
#
# window = MyWindow()
# window.show()
# app.exec_()

"""8.MAsala"""

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
#
# app = QApplication([])

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.label = QLabel("********")
#
#         btn1 = QPushButton("Kitob")
#         btn1.clicked.connect(self.get_book)
#
#         btn2 = QPushButton("Qo'shiq")
#         btn2.clicked.connect(self.get_song)
#
#         btn3 = QPushButton("Sport")
#         btn3.clicked.connect(self.get_sport)
#
#         vertical = QVBoxLayout()
#         vertical.addWidget(self.label)
#         vertical.addWidget(btn1)
#         vertical.addWidget(btn2)
#         vertical.addWidget(btn3)
#
#         window = QWidget()
#         window.setLayout(vertical)
#         self.setCentralWidget(window)
#         self.setWindowTitle("MyWindow")
#
#     def get_book(self):
#         self.label.setText("Alchemist")
#
#     def get_song(self):
#         self.label.setText("Bohemian Rhapsody")
#
#     def get_sport(self):
#         self.label.setText("Shaxmat")
#
# window = MyWindow()
# window.show()
# app.exec_()

"""9.masala"""

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.line_edit = QLineEdit(self)
#         self.label = QLabel('Natija:', self)
#
#         self.button_length = QPushButton('Matn uzunligi', self)
#         self.button_upper = QPushButton('Katta harflar', self)
#         self.button_lower = QPushButton('Kichik harflar', self)
#         self.button_reverse = QPushButton('Orqaga ogirish', self)
#         self.button_remove_spaces = QPushButton('Bosh joylarni olib tashlash', self)
#         self.button_modify = QPushButton('Matnni ozgartirish', self)
#
#         self.button_length.clicked.connect(self.show_length)
#         self.button_upper.clicked.connect(self.convert_to_upper)
#         self.button_lower.clicked.connect(self.convert_to_lower)
#         self.button_reverse.clicked.connect(self.reverse_text)
#         self.button_remove_spaces.clicked.connect(self.remove_spaces)
#         self.button_modify.clicked.connect(self.modify_text)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.line_edit)
#         layout.addWidget(self.label)
#         layout.addWidget(self.button_length)
#         layout.addWidget(self.button_upper)
#         layout.addWidget(self.button_lower)
#         layout.addWidget(self.button_reverse)
#         layout.addWidget(self.button_remove_spaces)
#         layout.addWidget(self.button_modify)
#
#         self.setLayout(layout)
#
#     def show_length(self):
#         text = self.line_edit.text()
#         self.label.setText(f'Matn uzunligi: {len(text)}')
#
#     def convert_to_upper(self):
#         text = self.line_edit.text()
#         self.label.setText(f'Katta harflar: {text.upper()}')
#
#     def convert_to_lower(self):
#         text = self.line_edit.text()
#         self.label.setText(f'Kichik harflar: {text.lower()}')
#
#     def reverse_text(self):
#         text = self.line_edit.text()
#         self.label.setText(f'Orqaga ogirilgan matn: {text[::-1]}')
#
#     def remove_spaces(self):
#         text = self.line_edit.text()
#         self.label.setText(f'Bosh joylarsiz matn: {text.replace(" ", "")}')
#
#     def modify_text(self):
#         self.label.setText('Matn ozgartirildi!')
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec_())


"""10.Masala""" """Manashu 9 va 10 da GPT dan yorda so'radim sababi o'zim chiqarishni bilmadim tog'ri ishlame qoldi"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import QDate

class SanaIlovasi(QWidget):
    def __init__(self):
        super().__init__()
        self.kiritish = QLineEdit(self)
        self.natija = QLabel('Natija:', self)

        self.kun_btn = QPushButton('Sana kuni', self)
        self.qush_10_kun_btn = QPushButton('10 kun keyin', self)
        self.qush_oy_btn = QPushButton('1 oy keyin', self)
        self.qush_yil_btn = QPushButton('1 yil keyin', self)
        self.ayir_2_kun_btn = QPushButton('2 kun oldin', self)
        self.ayir_oy_btn = QPushButton('1 oy oldin', self)

        self.kun_btn.clicked.connect(self.sana_kuni)
        self.qush_10_kun_btn.clicked.connect(self.qush_10_kun)
        self.qush_oy_btn.clicked.connect(self.qush_oy)
        self.qush_yil_btn.clicked.connect(self.qush_yil)
        self.ayir_2_kun_btn.clicked.connect(self.ayir_2_kun)
        self.ayir_oy_btn.clicked.connect(self.ayir_oy)

        layout = QVBoxLayout()
        layout.addWidget(self.kiritish)
        layout.addWidget(self.natija)
        layout.addWidget(self.kun_btn)
        layout.addWidget(self.qush_10_kun_btn)
        layout.addWidget(self.qush_oy_btn)
        layout.addWidget(self.qush_yil_btn)
        layout.addWidget(self.ayir_2_kun_btn)
        layout.addWidget(self.ayir_oy_btn)

        self.setLayout(layout)
    def ol_sana(self):
        sana_matn = self.kiritish.text()
        return QDate.fromString(sana_matn, 'yyyy-MM-dd')

    def sana_kuni(self):
        sana = self.ol_sana()
        self.natija.setText(f'Kun: {sana.day()}')

    def qush_10_kun(self):
        sana = self.ol_sana().addDays(10)
        self.natija.setText(f'10 kun keyin: {sana.toString("yyyy-MM-dd")}')

    def qush_oy(self):
        sana = self.ol_sana().addMonths(1)
        self.natija.setText(f'1 oy keyin: {sana.toString("yyyy-MM-dd")}')

    def qush_yil(self):
        sana = self.ol_sana().addYears(1)
        self.natija.setText(f'1 yil keyin: {sana.toString("yyyy-MM-dd")}')

    def ayir_2_kun(self):
        sana = self.ol_sana().addDays(-2)
        self.natija.setText(f'2 kun oldin: {sana.toString("yyyy-MM-dd")}')

    def ayir_oy(self):
        sana = self.ol_sana().addMonths(-1)
        self.natija.setText(f'1 oy oldin: {sana.toString("yyyy-MM-dd")}')

app = QApplication(sys.argv)
window = SanaIlovasi()
window.show()
sys.exit(app.exec_())

