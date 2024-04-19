def lz77Compress(input, bufferSize):
    if (bufferSize == -1):
        r = 0
        while (r < len(input)):
            t = ""
            t = input[r]
            pos = 0
            length = 0
            ind = 0
            z = r
            while (1):
                flag = False
                y = z - len(t)
                for i in range(0, y + 1):
                    if (input[i:len(t) + i] == t):
                        flag = True
                        pos = i
                if (flag):
                    r += 1
                    if (r >= len(input)):
                        length = len(t)
                        ind = r - length - pos
                        break;
                    t += input[r]
                else:
                    length = len(t) - 1
                    if (len(t) == 1):
                        ind = 0
                    else:
                        ind = r - length - pos
                    break;
            print("<" + str(ind) + "," + str(length) + ",", end="")
            if (r >= len(input)):
                print("\"" + "Null" + "\"" + ">")
            else:
                print("\"" + input[r] + "\"" + ">")
                r += 1


    else:
        r = 0;
        while (r < len(input)):
            t = ""
            t = input[r]
            pos = 0
            y = 0
            f = r
            if (r >= bufferSize):
                y = r - bufferSize
            while (1):
                flag = False
                z = f - len(t)
                for i in range(y, z + 1):
                    if (input[i:len(t) + i] == t):
                        flag = True
                        pos = i
                if (flag):
                    r += 1
                    if (r >= len(input)):
                        length = len(t)
                        ind = r - length - pos
                        break
                    t += input[r]
                else:
                    length = len(t) - 1
                    if (len(t) == 1):
                        ind = 0
                    else:
                        ind = r - length - pos
                    break

            print("<" + str(ind) + "," + str(length) + ",")
            if (r >= len(input)):
                print("\"" + "Null" + "\"" + ">")
            else:
                print("\"" + input[r] + "\"" + ">")
                r += 1


s = input("Enter TEXT : ")
# n = int(input("enter search size \(if unlimited enter -1) : "))#"ABAABABAABBBBBBBBBBBBA"
lz77Compress(s, -1)