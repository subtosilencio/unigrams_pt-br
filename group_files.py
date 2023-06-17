#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""group_files.py:

Put together all files created indidually.
"""

import os


def main():
    """Main function."""
    print("Reading files...")
    list_of_files = os.listdir('unigrams/')
    unigrams = {}

    for file_name in list_of_files:
        filepath = os.path.join('unigrams/', file_name)

        print(f'Colecting data from: "{file_name}"...')
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as filetxt:
            for line in filetxt:
                key, value = line.split()
                unigrams[key] = unigrams.get(key, 0) + int(value)

    print('Creating "big_unigrams.txt"...')
    with open('unigrams/big_unigrams.txt', 'w+', encoding="utf-8") as filetxt:
        for key, value in sorted(unigrams.items(), key=lambda x: x[1], reverse=True):
            if value > 100:
                filetxt.write(f"{key}\t{value}\n")
    print('File "big_unigrams.txt" created!')
    print()


if __name__ == '__main__':
    main()
