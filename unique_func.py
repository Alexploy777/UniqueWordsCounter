import math
import os
import re
import pymorphy3


class CounterUniqueWords:
    def __init__(self, main_window):
        self.morph = pymorphy3.MorphAnalyzer(path='pymorphy3_dicts_ru')
        self.main_window = main_window
        self.pattern = re.compile(r'[а-яёa-z]+')
        self.progressBar = main_window.progressBar
        self.label = main_window.label
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
        self.unique_words.clear()
        string_text = self.file_reader(file_path)
        list_words = string_text.split()
        max_count = len(list_words)
        for count, word in enumerate(list_words):
            # x = 100 * count / max_count
            self.progressBar.setValue(math.ceil(100 * count / max_count))
            filtered_word = self.pattern.search(word)
            self.label.setText('Счетчик уникальных слов: фильтруем')
            word = filtered_word[0] if filtered_word else ''
            if word and len(word) >= min_symbols:
                if flag_normal_form:
                    word = self.morph.parse(word)[0].normal_form
                self.unique_words.add(word)
                self.label.setText('Счетчик уникальных слов: считаем')

        l = len(self.unique_words)
        print(l)
        print(count)
        return len(self.unique_words)
