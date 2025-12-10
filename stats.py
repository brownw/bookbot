def count_words(s):
    totalWords = 0
    words = s.split()
    for word in words:
        totalWords += 1
    return totalWords

def count_characters(s):
    char_count = {}
    for c in s:
        lower_c = c.lower()
        if lower_c not in char_count:
            char_count[lower_c] = 1
        else:
            char_count[lower_c] += 1
    return char_count

def sort_on(char_dict):
    return char_dict["num"]

def sort_characters(char_count):
    sorted = []
    for char in char_count:
        if char.isalpha():
            char_dict =  {"char": char, "num": char_count[char]}
            sorted.append(char_dict)
    sorted.sort(reverse=True, key=sort_on)
    return sorted
        
