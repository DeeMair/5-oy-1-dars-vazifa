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

