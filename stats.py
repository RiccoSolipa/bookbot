def get_num_words(text):
    num_words = len(text.split())
    return num_words

def appeareance_count(text):
    letter_count = {}
    text = text.lower()
    for t in text:
        if t not in letter_count:
            letter_count[t] = 1
        else:
            letter_count[t] +=1      
    return letter_count

def sort_on(d):
    return d["num"]

def sort_dicts(letter_count):
    sorted_list = []
    for letter in letter_count:
        sorted_list.append({"char": letter, "num": letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
