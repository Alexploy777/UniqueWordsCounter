import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication

from gui import Ui_MainWindow
from unique_func import CounterUniqueWords


class UniqueWords(QMainWindow, Ui_MainWindow, QFileDialog):
    def __init__(self):
        super(UniqueWords, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Alex words counter')
        self.setWindowIcon(QIcon('al.ico'))
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_count.clicked.connect(self.start)
        self.pushButton_safe.clicked.connect(self.safe_dict)

        self.counter_obj = CounterUniqueWords(self)
        self.file_path = ''

    def lcd_clear(self):
        self.lcdNumber.display(0)

    def safe_dict(self):
        path_for_safe = QFileDialog.getSaveFileName(self, "Сохраняем словарь", filter="текстовый файл (*.txt)")[0]
        self.counter_obj.safe_unique_words(path_for_safe)

    def open_file(self):
        path = QFileDialog.getOpenFileName(self, "Выбери текстовый файл", "/home/", filter="текстовый файл (*.txt)")[0]
        if path:
            self.file_path = path
            self.label.setText(f'Файл: {self.file_path}')
            self.pushButton_safe.setDisabled(True)
            self.lcd_clear()

    def start(self):
        self.lcd_clear()
        if self.checkBox.isChecked():
            flag_normal_form = True
        else:
            flag_normal_form = False
        min_symbols = self.spinBox.value()
        if self.file_path:
            self.pushButton.setDisabled(True)  # Делает не активной кнопку выбора файла
            self.counter_obj.different_words_func(self.file_path, flag_normal_form, min_symbols)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UniqueWords()
    w.show()
    sys.exit(app.exec_())
