from stats import get_word_count
from stats import get_letter_count
from stats import character_sorted_list
from collections import Counter
import sys

def main():
    
    book_path = ""
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    

    word_length = get_word_count(book_path)
    letter_count = get_letter_count(book_path)
    sorted_list = character_sorted_list(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_length} total words")
    print("--------- Character Count -------")
    for key, value in sorted_list:
        print(f"{key}: {value}")
    print("============= END ===============")
    
    


main()