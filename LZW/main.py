def encode(text):

    dict_size = 128
    dictionary = {}

    for i in range(0, dict_size):
        x = chr(i)
        dictionary[x] = i

    s = ""
    result = []
    i = 0
    while i < len(text):
        ms = s + text[i]
        if ms in dictionary:
            s = ms
        else:
            result.append(dictionary[s])
            dictionary[ms] = dict_size
            dict_size += 1
            s = ""
            i -= 1
        i += 1
    if len(s) > 0:
        result.append(dictionary[s])
    return result



# "ABAABABBAABAABAAAABABBBBBBBB"
e = input("Enter Text : ")
r=encode(e)
print(r)

#xyxyxyxyxyxyzzzzzzzz