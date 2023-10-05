import math
import os
import re
import pymorphy3
import configparser

from PyQt5.QtCore import QThread, pyqtSignal


class DifferentWordsFunc(QThread):
    # update_signal = pyqtSignal(str)
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.unique_words = set()

        # self.different_words_func_qth()

    def different_words_func_qth(self):
        if self.main_window.checkBox_rus.isChecked():
            pattern = self.main_window.pattern_ru
        else:
            pattern = self.main_window.pattern
        self.unique_words.clear()
        string_text = self.main_window.file_reader(self.main_window.file_path)
        string_text = self.main_window.pattern_punctuation.sub(' ', string_text)
        list_words = string_text.split()
        max_count = len(list_words)
        for count, word in enumerate(list_words):
            self.main_window.progressBar.setValue(math.ceil(100 * count / max_count))
            self.main_window.label.setText('Счетчик уникальных слов: фильтруем')
            filtered_word = pattern.search(word)[0] if pattern.search(word) else False
            if filtered_word and len(filtered_word) >= self.main_window.min_symbols:
                if self.main_window.flag_normal_form:
                    filtered_word = self.main_window.morph.parse(filtered_word)[0].normal_form
                self.main_window.label.setText('Счетчик уникальных слов: считаем')
                self.unique_words.add(filtered_word)

        res = self.unique_words
        self.main_window.lcdNumber.display(len(res))
        return res



class CounterUniqueWords(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.morph = pymorphy3.MorphAnalyzer(path='pymorphy3_dicts_ru')
        self.main_window = main_window
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding="utf-8")
        self.pattern_punctuation = re.compile(self.config.get('default', 'pattern_punctuation'))
        self.pattern = re.compile(self.config.get('default', 'pattern'))
        self.pattern_ru = re.compile(self.config.get('default', 'pattern_ru'))
        self.progressBar = main_window.progressBar
        self.label = main_window.label
        self.checkBox_rus = main_window.checkBox_rus
        self.lcdNumber = main_window.lcdNumber







    def file_reader(self, path):
        path = os.path.normpath(path)
        with open(path, 'r', encoding='utf-8') as f:
            self.label.setText('Счетчик уникальных слов: читаем файл..')
            return f.read().lower()

    def safe_unique_words(self, path_for_safe):
        if path_for_safe:
            path = os.path.normpath(path_for_safe)
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.unique_words))

    def different_words_func(self, file_path, flag_normal_form, min_symbols):
        self.file_path = file_path
        self.flag_normal_form = flag_normal_form
        self.min_symbols = min_symbols

        self.different_words_func_obj = DifferentWordsFunc(self)

        # self.thread = QThread()
        # self.thread.start(self.different_words_func_obj.different_words_func_qth())


        self.unique_words = self.different_words_func_obj.different_words_func_qth()

