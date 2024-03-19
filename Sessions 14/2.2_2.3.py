#============================================2.2
def find_anagrams(file_path):
    with open(file_path, 'r') as file:
        word_dict = {}
        for word in file:
            word = word.strip().lower()
            key = ''.join(sorted(word))
            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

    # Filter out the entries with only one word, as they dont have anagrams
    anagrams = [words for words in word_dict.values() if len(words) > 1]
    for words in anagrams:
        print(words)

find_anagrams('words.txt')

#============================================2.3
def find_and_sort_anagrams(file_path):
    with open(file_path, 'r') as file:
        word_dict = {}
        for word in file:
            word = word.strip().lower()
            key = ''.join(sorted(word))
            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

    anagrams = [words for words in word_dict.values() if len(words) > 1]

    # Sort the anagrams list by the length of its sublists in descending order
    anagrams_sorted = sorted(anagrams, key=len, reverse=True)
    for words in anagrams_sorted:
        print(words)

find_and_sort_anagrams('words.txt')
