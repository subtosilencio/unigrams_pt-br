#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""npl_word_segment.py:

Word segmentation to create unigrams in Portuguese (pt-br).
"""

import unicodedata
import re
import os

# import nltk


def main():
    """Main function."""
    print("Reading folder with corpus files...")
    list_of_files = os.listdir('corpus/')

    for file_name in list_of_files:
        unigrams = {}
        list_unigrams = []
        filepath = os.path.join('corpus/', file_name)

        print(f'Getting data from file: "{file_name}"...')
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as filetxt:
            for line in filetxt:
                line = clean_text(line)
                if line != '':
                    unigrams_dict = create_unigrams(line)
                    for key, value in unigrams_dict.items():
                        numbers = sum(c.isdigit() for c in key)  # Count numbers in string
                        # limite 4 numbers
                        if numbers < 4:
                            unigrams[key] = unigrams.get(key, 0) + value

        print("Sorting data...")
        list_unigrams = sorted(unigrams.items(), key=lambda x: x[1], reverse=True)

        print(f'Save data to file "unigrams_{file_name}"')
        with open(f'unigrams/onegram_{file_name}', 'w+', encoding="utf-8") as filetxt:
            for key, value in list_unigrams:
                filetxt.write(f"{key}\t{value}\n")
        print(f'File "unigrams_{file_name}" created!')
        print()


def create_unigrams(text):
    """Create a dictionary with the frequency of each word."""
    unigrams = {}
    # tokenize words
    # tokenized_words = nltk.word_tokenize(text)
    tokenized_words = text.split()
    # filter empty words
    tokenized_words = list(filter(None, tokenized_words))
    # create dictionary
    for word in tokenized_words:
        unigrams[word] = unigrams.get(word, 0) + 1

    return unigrams


def convert_accents_regex(text: str) -> str:
    """Convert accents from a string using regex."""
    regex = re.compile(r'[\u0300-\u036F]', flags=re.DOTALL)
    normalized = unicodedata.normalize('NFKD', text)
    return regex.sub('', normalized)


def clean_text(text):
    """Clean text converting and removing junk."""
    regex_url = r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
    text = text.strip()
    # Convert Accents
    text = convert_accents_regex(text)
    # Remove URLs
    text = re.sub(regex_url, '', text)
    # Remove HTML Tags
    text = re.sub('<[^<]+?>', '', text)
    # Lowercase all text
    text = text.lower()
    # Remove punctuation
    text = re.sub('[^A-Za-z0-9 ]+', '', text)

    return text


if __name__ == '__main__':
    main()
