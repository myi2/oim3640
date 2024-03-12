import random
import string
import sys
from unicodedata import category

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith("*** START OF THE PROJECT"):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency
    excluding_stopwords: boolean, whether to exclude common stopwords

    returns: list of (frequency, word) pairs
    """
    if excluding_stopwords:
        stopwords = set(line.strip() for line in open('stopwords.txt'))
        hist = {word: freq for word, freq in hist.items() if word not in stopwords}
    
    return sorted(hist.items(), key=lambda x: x[1], reverse=True)

def print_most_common(hist, num=10):
    """Prints the most commons words in a histogram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print(f"The {num} most common words are:")
    for word, freq in t[:num]:
        print(f"{word}\t{freq}")

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    return {key: d1[key] for key in d1 if key not in d2}

def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    words, cum_dist = [], []
    total_freq = sum(hist.values())
    cumulative = 0
    for word, freq in hist.items():
        cumulative += freq
        words.append(word)
        cum_dist.append(cumulative / total_freq)

    r = random.random()
    for word, cum_val in zip(words, cum_dist):
        if r < cum_val:
            return word

def main():
    hist = process_file("Sessions 15\Pride and Prejudice.txt", skip_header=True)

    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for word, freq in t[:20]:
        print(word, '\t', freq)
    print("\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == "__main__":
    main()
