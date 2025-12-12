from stats import get_num_words, appeareance_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text


def main():
   text = get_book_text("books/frankenstein.txt")
   get_num_words(text)
   count = appeareance_count(text)
   print(count)
   
main()
