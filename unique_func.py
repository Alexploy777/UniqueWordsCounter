import math
import os
import re
import pymorphy3
import configparser


class CounterUniqueWords:
    def __init__(self, main_window):
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
        self.unique_words = set()

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
        if self.checkBox_rus.isChecked():
            pattern = self.pattern_ru
        else:
            pattern = self.pattern
        self.unique_words.clear()
        string_text = self.file_reader(file_path)
        string_text = self.pattern_punctuation.sub(' ', string_text)
        list_words = string_text.split()
        max_count = len(list_words)
        for count, word in enumerate(list_words):
            self.progressBar.setValue(math.ceil(100 * count / max_count))
            self.label.setText('Счетчик уникальных слов: фильтруем')
            filtered_word = pattern.search(word)[0] if pattern.search(word) else False
            if filtered_word and len(filtered_word) >= min_symbols:
                if flag_normal_form:
                    filtered_word = self.morph.parse(filtered_word)[0].normal_form
                self.label.setText('Счетчик уникальных слов: считаем')
                self.unique_words.add(filtered_word)
        return len(self.unique_words)
