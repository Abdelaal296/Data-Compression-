s = input("Enter data :")
n = input("Enter number of letters :")
d = {}
print("Enter letter and his code: ")
for i in range (int(n)) :
     b = input()
     l = input()
     d[str(l)] = b

t = ""
res = ""
for i in s:
    t += i
    if str(t) in d:
        res += d[t]
        t = ""



print(res)

# ('C', '0'), ('B', '100'), ('D', '101'), ('A', '11')]

# 1000111110110110100110110110