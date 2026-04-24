import re

def get_value(pair):   # функция для сортировки
  return pair[1]
#===============Литературный текст=============
class LiteraryText:
  """ тип КнижныйТекст"""
  def __init__(self, title, author, text):
    self._title = title
    self._author = author
    self._text = text

  def word_count(self): #считать слова
    if not self._text:
      return 0
    words = self._text.split()
    return len(words)

  def char_count(self): #считать символы
    return len(self._text)

  def unique_words(self): #считать уникальные слова
    if not self._text:
        return 0
    words = self._text.split()
    unique_words_set = set(words)
    return len(unique_words_set)

  def __str__(self):
    word_count = self.word_count()
    return f"'{self._title}' - {self._author} ({word_count} слов)"

  def __repr__(self):
    return f"LiteraryText(title='{self._title}', author='{self._author}')"

  def get_author(self):
    return self._author

  def get_title(self):
    return self._title

  def get_text(self):
    return self._text

#==================== поэма ==========

class Poem(LiteraryText):
  def __init__(self, title, author, text,lines):
     super().__init__(title, author, text)
     self.__lines = lines

  def get_lines_count(self):
    return len(self.__lines)

  def __str__(self):
    base_str = super().__str__()
    return f"{base_str} (стихотворение, {len(self.__lines)} строк)"
#===============- проза -===========

class Prose(LiteraryText):
  def __init__(self, title, author, text, chapters):
     super().__init__(title, author, text)
     self.__chapters = chapters

  def get_chapter_count(self):
    return self.__chapters

  def __str__(self):
    base_str = super().__str__()
    return f"{base_str} (проза, {self.__chapters} глав)"

#===============- задание -=============
#===============- форматный миксин -===============

class FormatMixin:

 def format(self, style="html"):
  text = self.get_text()
  if style == "html":
    return f"<p>{text}</p>"
  elif style == "markdown":
    return f"*{text}*"
  else:
    return text

#=================- Аналайз миксин -===============

class AnalyzeMixin:

  def avg_word_length(self):
    text = self.get_text()
    if not text:
      return 0
    text_by_word = re.sub(r'[^\w\s]', '', text.lower())
    words = text_by_word.split()
    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)

  def most_common_word(self):
    text = self.get_text()
    if not text:
      return None

    text_by_word = re.sub(r'[^\w\s]', '', text.lower())
    words = text_by_word.split()
    if not words:
        return 0

    word_counts={}
    for word in words:
      word_counts[word] = word_counts.get(word, 0) + 1 # get безопасый способ проверить если значение в дикте и к нему +1 если он будет

    word_counts_sort= sorted(word_counts.items(), key=get_value , reverse=True)
    return word_counts_sort[0]


#=================- СОЗДАНИЕ комбинирующих -========
class FormattedPoem(Poem, FormatMixin):
    pass

class FormattedProse(Prose, FormatMixin):
    pass

class AnalyzedPoem(Poem, AnalyzeMixin):
    pass

class AnalyzedProse(Prose, AnalyzeMixin):
    pass

class ProcessedPoem(Poem, FormatMixin, AnalyzeMixin):
    pass

class ProcessedProse(Prose, FormatMixin, AnalyzeMixin):
    pass

#===================- Создание функции -==========
def process_text(text_obj):
  print(f'Информация об {text_obj}')
  print(f"Тип: {type(text_obj).__name__} ")

  if hasattr(text_obj, 'format'):# Если у объекта есть метод format(), вызываем его для обоих стилей
    print(f"Форматирование (HTML): {text_obj.format('html')}")
    print(f"Форматирование (Markdown): {text_obj.format('markdown')}")

  if hasattr(text_obj, 'most_common_word'): # Если у объекта есть метод most_common_word(), вызываем его
    common_word = text_obj.most_common_word()
    if common_word:
        print(f"Самое частое слово: '{common_word[0]}' (встречается {common_word[1]} раз)")
    else:
        print("\nСамое частое слово: не определено")

  if hasattr(text_obj, 'avg_word_length'): # Если у объекта есть метод avg_word_length(), вызываем его
    avg_len = text_obj.avg_word_length()
    print(f"Средняя длина слова: {avg_len:.2f} символов")

  if hasattr(text_obj, 'get_lines_count'): # Если у объекта есть метод get_lines_count(), выводим количество строк
    print(f"Количество строк: {text_obj.get_lines_count()}")

  if hasattr(text_obj, 'get_chapter_count'): # Если у объекта есть метод get_chapter_count(), выводим количество глав
    print(f"Количество глав: {text_obj.get_chapter_count()}")

#==========- демонстрация -==========

# Данные для тестирования
poem_text = "В синем море звезды блещут в синем море волны хлещут"
prose_text = "В некотором царстве в некотором государстве жил был царь"

# Создание объектов
objects = [
    LiteraryText("Война и мир", "Толстой", prose_text),
    Poem("Бородино", "Лермонтов", poem_text, ["строка1", "строка2", "строка3"]),
    Prose("Морозко", "Народная", prose_text, 5),
    FormattedPoem("Узник", "Пушкин", poem_text, ["строка1", "строка2"]),
    FormattedProse("Дубровский", "Пушкин", prose_text, 4),
    AnalyzedPoem("Анчар", "Пушкин", poem_text, ["строка1", "строка2"]),
    AnalyzedProse("Мцыри", "Лермонтов", prose_text, 3),
    ProcessedPoem("Пророк", "Пушкин", poem_text, ["строка1"]),
    ProcessedProse("Пиковая дама", "Пушкин", prose_text, 3)
]

# Вывод результатов
print("\n" + "=" * 55)
print("ОБРАБОТКА ТЕКСТОВЫХ ОБЪЕКТОВ")
print("=" * 55)

for obj in objects:
    print(f"\n▶ {obj}")
    print(f"   Тип: {type(obj).__name__}")

    if hasattr(obj, 'format'):
        print(f"   HTML: {obj.format('html')}")
        print(f"   Markdown: {obj.format('markdown')}")

    if hasattr(obj, 'most_common_word'):
        word, count = obj.most_common_word()
        print(f"   Частое слово: '{word}' ({count})")

    if hasattr(obj, 'avg_word_length'):
        print(f"   Средняя длина слова: {obj.avg_word_length():.1f}")

    if hasattr(obj, 'get_lines_count'):
        print(f"   Строк: {obj.get_lines_count()}")

    if hasattr(obj, 'get_chapter_count'):
        print(f"   Глав: {obj.get_chapter_count()}")

print("\n" + "=" * 55)