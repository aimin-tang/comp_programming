def get_curr_end(string, start, is_space):
    curr_ptr = start
    while curr_ptr < len(string):
        if is_space:
            if string[curr_ptr] == ' ':
                curr_ptr += 1
            else:
                return curr_ptr
        else:
            if string[curr_ptr] != ' ':
                curr_ptr += 1
            else:
                return curr_ptr
    return len(string)

def reverseWordsInString(string):
    curr_start = 0
    result_l = []
    while curr_start < len(string):
        if string[curr_start] == ' ':
            curr_end = get_curr_end(string, curr_start+1, is_space=True)
        else:
            curr_end = get_curr_end(string, curr_start+1, is_space=False)
        result_l.append(string[curr_start:curr_end])
        curr_start = curr_end

    return ''.join(reversed(result_l))



string = "AlgoExpert is the best!"
print("-{}=".format(reverseWordsInString(string)))