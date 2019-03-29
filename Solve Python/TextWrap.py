def wrap(string, max_width):
    res = ''

    for i in range(len(string)):
        if i>0 and i%max_width==0:
            res += '\n'
        res += string[i]
    return res
