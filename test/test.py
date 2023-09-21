import re
import string

string_text = '''
   <p>В китайском языке_здесь -играслов то-же: «протон» и «софон» звучат почти одинаково: «чжицзи». — <emphasis>Прим. К. Л.</emphasis></p>
  </section>
  <section id="n67">
   <title>
    <p>67</p>
   </title>
   <p>Напомним, «софия» по-гречески «мудрость». — <emphasis>Прим. перев.</emphasis></p>
  </section>
  <section id="n68">
   <title>
    <p>68</p>
   </title>
   <p>Напомним на всякий случай, что это явление называется квантовой запутанностью. — <emphasis>Прим. перев.</emphasis></p>
  </section>
  <section id="n69">
   <title>
    <p>69</p>
   </title>
   <p>Здесь нет ошибки и нет противоречия с главой 30, в которой утверждается, что трисоляриане прекратили общение с землянами еще четыре года назад. Имеется в виду, что они прекратили радиопередачи. Трисоляриане общались с адвентистами с помощью софонов, проецируя сообщения непосредственно на сетчатку их глаз. А теперь они перестали делать и это. — <emphasis>Прим. перев.</emphasis></p>
  </section>
 </body>
 <binary id="cover.jpg" content-type="image/jpeg">/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgMCAgMDAgMDAwMDBAcFBAQEBAkGBwUHCgkL
CwoJCgoMDREODAwQDAoKDhQPEBESExMTCw4UFhQSFhESExL/2wBDAQMDAwQEBAgFBQgSDAoM
EhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhL/wgAR
CANNAjoDAREAAhEBAxEB/8QAHQAAAQUBAQEBAAAAAAAAAAAAAwABAgQFBgcICf/EABsBAAMB
AQEBAQAAAAAAAAAAAAABAgMEBQYH/9oADAMBAAIQAxAAAAH53x3sDCmwODAgkEQQTFBqZQyU
SgQIHGxSB0ONDdNFMxyWEzlgYURISBhJiQgQIaaYUikhAgQJhSknFjotDCEAccykNEuJhDBC
YHBwgCBAgQEAYODgybgwOCTZpCTaQmMJAgQnGgQSmmY8tFSTi5ZpnLNMTESBAgYSA4RAQJiA
qYmnTQIECYdsZSQhTTiCBxlHAbAhGAAmEhpBQGCBmmBAgQIHRIpgQkqdUgZynLA4MCJQIbpp
jCQ3RKdDmgSIuY1DNIEKIkJwi0yHBNsk42aQIEDA45JsJBKqcaBIdCBA45DOOuDCOA0QGQIA
'''

pattern_punctuation = re.compile(r'[^\w\s\-]')

pattern = re.compile(r'\b[а-яa-zё_]*(?:-[а-яa-zё_]+[а-яa-zё_]*)*\b')
pattern_ru = re.compile(r'\b[а-яё_]*(?:-[а-яё_]+[а-яё_]*)*\b')

string_text = string_text.lower()
string_text = pattern_punctuation.sub(' ', string_text)


w_list = string_text.split()


deleted_word_list = []

# filtered_word_list = [pattern.search(w)[0] for w in w_list if pattern.search(w) and pattern.search(w)[0]]
filtered_word_list = [pattern.search(w)[0] for w in w_list if pattern.search(w) and pattern.search(w)[0]]

# filtered_word_list = []
# for word in w_list:
#     filtered_word = pattern.search(word) # re только буквы
#     if filtered_word:
#         if filtered_word[0]:
#             filtered_word_list.append(filtered_word[0])
#     else:
#         deleted_word_list.append(word)


print(filtered_word_list, len(filtered_word_list))
print('==================================')
print(deleted_word_list)