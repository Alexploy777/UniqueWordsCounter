import sys
from time import time
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
        # self.progressBar.setValue(0)
        # self.label.setText('Счетчик уникальных слов:')

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

        self.pushButton_safe.setDisabled(True)
        if self.checkBox.isChecked():
            flag_normal_form = True
        else:
            flag_normal_form = False
        min_symbols = self.spinBox.value()
        start_time = time()
        if self.file_path:
            self.pushButton.setDisabled(True)
            unique_words_num = self.counter_obj.different_words_func(self.file_path, flag_normal_form, min_symbols)
            self.lcdNumber.display(unique_words_num)
            self.label.setText(f'{self.file_path}: {round(time() - start_time, 2)} сек')
            self.progressBar.setValue(100)
            self.pushButton_safe.setEnabled(True)
            self.pushButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UniqueWords()
    w.show()
    sys.exit(app.exec_())
