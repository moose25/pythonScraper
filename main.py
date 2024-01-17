from scraper import get_bbc_headlines
from analyzer import analyze_headlines_for_words, analyze_headlines_for_ngrams
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data, title, ylabel):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=[val[1] for val in data], y=[str(val[0]) for val in data])
    plt.title(title)
    plt.xlabel('Frequency')
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def main():
    url = 'https://www.bbc.com/'
    headlines = get_bbc_headlines(url)

    if headlines:
        # Analyze for individual words (excluding common stop words)
        word_analysis = analyze_headlines_for_words(headlines)
        print("Top 10 Keywords in BBC Headlines:")
        # Visualize Top Keywords
        top_keywords = word_analysis.most_common(10)
        visualize_data(top_keywords, "Top 10 Keywords in BBC Headlines", "Keywords")
        for word, count in word_analysis.most_common(10):
            print(f"{word}: {count}")

        # Analyze for n-grams (3 to 5 word phrases)
        ngram_analysis = analyze_headlines_for_ngrams(headlines)
        print("\nTop 10 N-grams in BBC Headlines:")
         # Visualize Top N-grams
        top_ngrams = ngram_analysis
        visualize_data(top_ngrams, "Top 10 N-grams in BBC Headlines", "N-grams")
        for ngram, count in ngram_analysis:
            print(f"{' '.join(ngram)}: {count}")

if __name__ == "__main__":
    main()
