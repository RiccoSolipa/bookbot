import sys
from stats import get_num_words, appeareance_count, sort_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count = appeareance_count(text)
    sorted_chars = sort_dicts(count)
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")
    
main()
