def decode(op):
    dict_size = 128
    dictionary = {}
    for i in range(0, dict_size):
        x = chr(i)
        dictionary[i] = x
    result = ""
    cur = op[0]
    old = dictionary[cur]
    result += old
    op.pop(0)
    for k in op:
        if k in dictionary:
            cur = dictionary[k]
        else:
            cur = old + old[0]
        result += cur
        dictionary[dict_size] = old + cur[0]
        dict_size += 1
        old = cur

    return result

# res = [65, 66, 65, 128, 128, 129, 131, 134, 130, 129, 66, 138, 139, 138]
# n=input("Enter number of tags : ")
# print("Enter list")
res=[]
# for i in range(int(n)):
#     x=input()
#     res.append(int(x))
i = 0


s = input("Enter list")

s = s.replace("[", "")
s = s.replace("]", "")
s = s.replace(" ", "")
s.split(',')

while i < len(s):

    res.append(int(s[i]))
    i += 1

d = decode(res)
print(d)