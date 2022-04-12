def get_word_space_rest(string):
    word, space = [], []
    i = 1
    while i < len(string):
        if string[i] == ' ':
            word



def reverseWordsInString(string):
    word, space, rest = get_word_space_rest(string)
    if space == None:
        return word
    else:
        return reverseWordsInString(rest) + space + word


string = "AlgoExpert is the best!"
print(reverseWordsInString(string))