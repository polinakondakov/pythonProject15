import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow #Импортирование классов QApplication, QWidget и
# QMainWindow из модуля QtWidgets библиотеки PyQt5. Эти классы используются для создания графических приложений с помощью PyQt5.
from ui_widgets import Ui_Form # мпортирование класса Ui_Form из модуля ui_widgets.
# этот класс содержит описание пользовательского интерфейса (UI) для главного окна приложения.

class MyWidget(QWidget, Ui_Form):

       def __init__(self): #инициализация объекта
           super().__init__() #Вызов метода инициализации родительского класса (в данном случае, инициализация класса QMainWindow).
           self.setupUi(self) #Вызов метода setupUi, который, устанавливает пользовательский интерфейс,
           # описанный в классе Ui_MainWindow
           self.pushButton.clicked.connect(self.push_ok)

       def push_ok(self):
           answer = []
           if self.radioButton_1_red.isChecked():
               answer.append("Красный")
           elif self.radioButton_1_blue.isChecked():
               answer.append("Синий")
           elif self.radioButton_1_green.isChecked():
               answer.append("Зеленый")

           if self.radioButton_2_red.isChecked():
               answer.append("Красный")
           elif self.radioButton_2_blue.isChecked():
               answer.append("Синий")
           elif self.radioButton_2_green.isChecked():
               answer.append("Зеленый")

           if self.radioButton_3_red.isChecked():
               answer.append("Красный")
           elif self.radioButton_3_blue.isChecked():
               answer.append("Синий")
           elif self.radioButton_3_green.isChecked():
               answer.append("Зеленый")

           self.label_answer.setText(", ".join(answer))

app = QApplication(sys.argv) #Создание объекта приложения QApplication с передачей аргументов командной строки sys.argv
ex = MyWidget() # Создание экземпляра класса MyWidget
ex.show() #его отображение
sys.exit(app.exec_()) #Запуск основного цикла обработки событий приложения с помощью метода exec_()
# объекта приложения app, и завершение программы с кодом возврата после завершения работы приложения.