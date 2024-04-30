def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        words_count = len(file_contents.split())
        letters_dict = count_letters(file_contents)
        letters_dict_list = get_list_from_dict(letters_dict)
        letters_dict_list.sort(reverse=True, key=sort_on)
        

        print(f"Frankestein book has {words_count} words!")
        
        for letter in letters_dict:
            print(f"The '{letter}' character was found {letters_dict[letter]} times")

        # print the sorted list
        print(letters_dict_list)

def count_letters(string):
    alphabet = {
        'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True, 'h': True, 'i': True, 'j': True,
        'k': True, 'l': True, 'm': True, 'n': True, 'o': True, 'p': True, 'q': True, 'r': True, 's': True, 't': True,
        'u': True, 'v': True, 'w': True, 'x': True, 'y': True, 'z': True
    }
    letters = {}

    for ch in string.lower():
        if ch in alphabet:
            if not (ch in letters):
                letters[ch] = 1
            else:
                letters[ch] += 1

    return letters

def sort_on(dict):
    return dict["count"]

def get_list_from_dict(dict):
    list = []
    for letter in dict:
        list.append({"letter": letter, "count": dict[letter]})
       
    return list



main()