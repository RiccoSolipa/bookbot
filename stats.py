def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def appeareance_count(text):
    letter_count = {}
    text = text.lower()
    for t in text:
        if t not in letter_count:
            letter_count[t] = 1
        else:
            letter_count[t] +=1
       
    return letter_count