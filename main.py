import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow #Импортирование классов QApplication, QWidget и
# QMainWindow из модуля QtWidgets библиотеки PyQt5. Эти классы используются для создания графических приложений с помощью PyQt5.
from ui_main import Ui_MainWindow # мпортирование класса Ui_MainWindow из модуля uimain.
# этот класс содержит описание пользовательского интерфейса (UI) для главного окна приложения.

class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self): #инициализация объекта
        super().__init__() #Вызов метода инициализации родительского класса (в данном случае, инициализация класса QMainWindow).
        self.setupUi(self) #Вызов метода setupUi, который, устанавливает пользовательский интерфейс,
        # описанный в классе Ui_MainWindow
        self.pushButton.clicked.connect(self.push_button_for_reverse_names)

    def push_button_for_reverse_names(self): #функция, которая задает действие кнопке ОК
        #1. Получает текст из полей lineEdit_last_name и lineEdit_first_name.
        #2. Переворачивает текст в каждом из полей, используя срезы [::-1].
        #3. Устанавливает перевернутый текст обратно в поля lineEdit_first_name и lineEdit_last_name.
        last_name = self.lineEdit_last_name.text()[::-1]
        first_name = self.lineEdit_first_name.text()[::-1]
        self.lineEdit_first_name.setText(first_name)
        self.lineEdit_last_name.setText(last_name)


app = QApplication(sys.argv) #Создание объекта приложения QApplication с передачей аргументов командной строки sys.argv
ex = MyWidget() # Создание экземпляра класса MyWidget
ex.show() #его отображение
sys.exit(app.exec_()) #Запуск основного цикла обработки событий приложения с помощью метода exec_()
# объекта приложения app, и завершение программы с кодом возврата после завершения работы приложения.