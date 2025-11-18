import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt
# Завантаження необхідних ресурсів NLTK
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
#Завантаження тексту Chesterton "Thursday"
text = gutenberg.raw('chesterton-thursday.txt')
#Токенізація
tokens = nltk.word_tokenize(text)
#неочищений текст
print("Кількість слів у тексті:", len(tokens))
# Частотний розподіл
fdist = FreqDist(tokens)
# 10 найчастіших слів
top10 = fdist.most_common(10)
print("\n10 найбільш уживаних слів (без очищення):")
print(top10)
# Побудова діаграми
words, counts = zip(*top10)
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title("Топ-10 найчастіших слів (без очищення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
#очищений текст
stop_words = set(stopwords.words('english'))
# Очищення: тільки слова, без пунктуації та стоп-слів
clean_tokens = [
    word.lower()
    for word in tokens
    if word.isalpha() and word.lower() not in stop_words
]
fdist_clean = FreqDist(clean_tokens)
top10_clean = fdist_clean.most_common(10)
print("\n10 найбільш уживаних слів (після очищення):")
print(top10_clean)
# Діаграма очищених даних
words_clean, counts_clean = zip(*top10_clean)
plt.figure(figsize=(10, 5))
plt.bar(words_clean, counts_clean)
plt.title("Топ-10 найчастіших очищених слів")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
