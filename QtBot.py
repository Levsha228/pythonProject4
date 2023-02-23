from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5973256978:AAEy_YK5UHXGg0Vrq7UGjy7WJBWyp75vjYA'
offset: int = -2
timeout: int = 0
updates: dict
chat_id_me = 538393324
chat_id_group = -798451609
chat_id_ilya = 979056570
chat_id_dasha = 534198136

types_message = ['Отправить текст','Отправить изображение']
#req = requests.get(f'https://api.telegram.org/bot5973256978:AAEy_YK5UHXGg0Vrq7UGjy7WJBWyp75vjYA/sendMessage?chat_id={chat_id_me}&text={message}')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Telegram bot from GET request") # Типа название окна
        self.button = QPushButton("GET запрос") # Текст на кнопке
        self.button.setCheckable(True)
        self.button.clicked.connect(self.GET_after_click) # Сигнал кнопки

        self.label = QLabel() # Текст в окне
        self.input = QLineEdit() # ВВод строки в окне

        self.picture = QPixmap('fun.jpg') # Инициализация картинки
        self.label_picture = QLabel()  # Вывод картинки (не получился)
        self.label_picture.setPixmap(self.picture)
         # (Типа изменения размера картинки в окне)

        self.combo_box = QComboBox()
        self.combo_box.addItems(types_message)
        self.combo_box.currentIndexChanged.connect(self.index_changed)
        self.combo_box.textActivated.connect(self.text_changed)

        self.setFixedSize(QSize(640, 480)) # размер окна
        self.label.setText('Введите текст или выберите тип сообщения')

        layout = QVBoxLayout()                          # !!!!НУЖНО СДЕЛАТЬ РАЗНЫЕ layout ДЛЯ КАЖДОГО ВИДЖЕТА В ОКНЕ!!!!
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        layout.addWidget(self.combo_box)
        layout.addWidget(self.button)
        layout.addWidget(self.label_picture)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    def GET_after_click(self):
        message = self.input.text()
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id_dasha}&text={message}')
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id_group}&text={message}')
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id_ilya}&text={message}')

    def index_changed(self, i):
        print(i)

    def text_changed(self, str):
        self.label.setText(str)
        print(str)
app = QApplication([])
# Создаем виджет Qt - окно

window = MainWindow()
window.show() # Окно по умолчанию скрыто

# Запускаем цикл событий
app.exec()

