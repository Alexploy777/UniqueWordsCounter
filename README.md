# UniqueWordsCounter - счетчик уникальных слов в текстовом файле.
Программа подсчитывает уникальные слова в текстовом файле.
1.	Можно задать минимальное количество букв в слове, если в слове число букв, менее заданных, то такое слово не учитывается.
2.	Если поставить галочку "формы слова - одно слово", то запускается более сложная обработка, где разные формы слова приводятся к одной форме и засчитываются за одно и тоже слово (используется библиотека "pymorphy3_dicts_ru"), 
3.	Если стоит галочка – «only rus», то «не русские» слова будут пропускаться.
4.	Можно сохранить множество неповторяющихся слов в виде текстового файла. При сохранении изначальный порядок слов не учитывается.
  	- При использовании "формы слова - одно слово" будет сохранено множество из "нормализованных слов".

