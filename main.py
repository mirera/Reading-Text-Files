# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#from sympy import content


def read_file_content(filename): 
    with open('story.txt', 'r') as opened_file:
        read_file = opened_file.read()
    return read_file
    


def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()
    word_dict = {}
    
    for word in split_text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict 

print (count_words())

    

