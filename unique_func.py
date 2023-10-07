import configparser
import math
import os
import re
from time import time

import pymorphy3
from PyQt5.QtCore import QThread, pyqtSignal


class DifferentWordsFunc(QThread):
    progressBar_signal = pyqtSignal(int)
    lcdNumber_signal = pyqtSignal(int)
    label_signal = pyqtSignal(str)
    unique_words_signal = pyqtSignal(set)
    label_time_signal = pyqtSignal(str)
    pushButton_enabled_signal = pyqtSignal(bool)
    pushButton_safe_enabled_signal = pyqtSignal(bool)

    def __init__(self, mainwindow):
        super(DifferentWordsFunc, self).__init__()
        self.mainwindow = mainwindow
        self.unique_words = set()
        self.progressBar = self.mainwindow.progressBar

    def run(self):
        start_time = time()
        if self.mainwindow.checkBox_rus.isChecked():
            pattern = self.mainwindow.pattern_ru
        else:
            pattern = self.mainwindow.pattern
        self.unique_words.clear()
        string_text = self.mainwindow.file_reader(self.mainwindow.file_path)
        string_text = self.mainwindow.pattern_punctuation.sub(' ', string_text)
        list_words = string_text.split()
        max_count = len(list_words)
        for count, word in enumerate(list_words):
            self.progressBar_signal.emit(math.ceil(100 * count / max_count))
            self.label_signal.emit('Счетчик уникальных слов: фильтруем')
            filtered_word = pattern.search(word)[0] if pattern.search(word) else False
            if filtered_word and len(filtered_word) >= self.mainwindow.min_symbols:
                if self.mainwindow.flag_normal_form:
                    filtered_word = self.mainwindow.morph.parse(filtered_word)[0].normal_form
                self.label_signal.emit('Счетчик уникальных слов: считаем')
                self.unique_words.add(filtered_word)

        self.lcdNumber_signal.emit(len(self.unique_words))
        self.unique_words_signal.emit(self.unique_words)
        self.label_time_signal.emit(f'{self.mainwindow.file_path}: {round(time() - start_time, 2)} сек')
        self.progressBar_signal.emit(100)
        self.pushButton_enabled_signal.emit(True)
        self.pushButton_safe_enabled_signal.emit(True)

class CounterUniqueWords:
    def __init__(self, main_window):
        super().__init__()
        self.morph : pymorphy3 = pymorphy3.MorphAnalyzer(path='pymorphy3_dicts_ru')
        self.main_window = main_window
        self.config: configparser = configparser.ConfigParser()
        self.config.read('config.ini', encoding="utf-8")
        self.pattern_punctuation = re.compile(self.config.get('default', 'pattern_punctuation'))
        self.pattern = re.compile(self.config.get('default', 'pattern'))
        self.pattern_ru = re.compile(self.config.get('default', 'pattern_ru'))
        self.progressBar = main_window.progressBar
        self.label = main_window.label
        self.checkBox_rus = main_window.checkBox_rus
        self.lcdNumber = main_window.lcdNumber
        self.pushButton = main_window.pushButton
        self.pushButton_safe = main_window.pushButton_safe
        self.unique_words = set()
        self.different_words_func_obj = DifferentWordsFunc(mainwindow=self)
        self.different_words_func_obj.progressBar_signal.connect(self.progressBar.setValue)
        self.different_words_func_obj.lcdNumber_signal.connect(self.lcdNumber.display)
        self.different_words_func_obj.label_signal.connect(self.label.setText)
        self.different_words_func_obj.unique_words_signal.connect(self.res_unique_words)
        self.different_words_func_obj.label_time_signal.connect(self.label.setText)
        self.different_words_func_obj.pushButton_enabled_signal.connect(self.pushButton.setEnabled)
        self.different_words_func_obj.pushButton_safe_enabled_signal.connect(self.pushButton_safe.setEnabled)

    def file_reader(self, path: str) -> str:
        path : str = os.path.normpath(path)
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
        self.different_words_func_obj.start()

    def res_unique_words(self, result_set):
        self.unique_words = result_set