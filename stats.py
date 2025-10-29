from collections import Counter

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(filepath):
    book_content = get_book_text(filepath)
    word_count = book_content.split()
    return len(word_count)

def get_letter_count(filepath):
    book_content = get_book_text(filepath)
    letter_count_dict = {}
    
    for l in book_content:
        lowered_letter = l.lower()
        if lowered_letter in letter_count_dict:
            letter_count_dict[lowered_letter] += 1
        else:
            letter_count_dict[lowered_letter] = 1
    return letter_count_dict

def character_sorted_list(filepath):
    unsorted_list = get_letter_count(filepath)
    sorted_list = sorted(unsorted_list.items(), key=lambda item: item[1], reverse=True)
    return sorted_list