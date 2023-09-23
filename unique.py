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
        self.pushButton.clicked.connect(self.start)
        self.pushButton_clear.clicked.connect(self.lcd_clear)
        self.pushButton_safe.clicked.connect(self.safe_dict)
        self._ = CounterUniqueWords(self)
        self.counter_obj = CounterUniqueWords(self)

    def lcd_clear(self):
        self.lcdNumber.display(0)
        self.progressBar.setValue(0)
        self.label.setText('Счетчик уникальных слов:')

    def safe_dict(self):
        path_for_safe = QFileDialog.getSaveFileName(self, "Сохраняем словарь", filter="текстовый файл (*.txt)")[0]
        self.counter_obj.safe_unique_words(path_for_safe)

    def start(self):
        self.lcd_clear()
        self.pushButton_clear.setDisabled(True)
        self.pushButton_safe.setDisabled(True)
        file_path = \
            QFileDialog.getOpenFileName(self, "Выбери текстовый файл", "/home/",
                                        filter="текстовый файл (*.txt)")[0]

        if self.checkBox.isChecked():
            flag_normal_form = True
        else:
            flag_normal_form = False
        min_symbols = self.spinBox.value()
        start_time = time()
        if file_path:
            unique_words_num = self.counter_obj.different_words_func(file_path, flag_normal_form, min_symbols)
            self.lcdNumber.display(unique_words_num)
            self.label.setText(f'Счетчик уникальных слов: посчитали за {round(time() - start_time, 2)} сек')
            self.progressBar.setValue(100)
            self.pushButton_safe.setEnabled(True)
            self.pushButton_clear.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UniqueWords()
    w.show()
    sys.exit(app.exec_())
