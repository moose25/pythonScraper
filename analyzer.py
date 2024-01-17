import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk import bigrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk import ngrams

# Download NLTK stopwords
nltk.download('stopwords')

def clean_text(text):
    return re.sub(r'\W+', ' ', text.lower())

def analyze_headlines_for_words(headlines):
    stop_words = set(stopwords.words('english'))
    word_count = Counter()

    for headline in headlines:
        cleaned = clean_text(headline['title'])
        words = [word for word in cleaned.split() if word not in stop_words]
        word_count.update(words)

    return word_count

def analyze_headlines_for_ngrams(headlines, n=3):
    stop_words = set(stopwords.words('english'))
    all_words = []

    for headline in headlines:
        cleaned = clean_text(headline['title'])
        words = [word for word in cleaned.split() if word not in stop_words]
        all_words.extend(words)

    ngram_freq = Counter()
    for i in range(3, 6):  # Adjust range for trigrams to five-grams
        for ngram in ngrams(all_words, i):
            if all(word not in stop_words for word in ngram):  # Check if all words in the n-gram are not stop words
                ngram_freq[ngram] += 1

    return ngram_freq.most_common(10)

