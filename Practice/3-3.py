#text = input("->")
#print(text.upper())
#print(text.strip())
#print(text.replace("bad", "good"))
#print(text.endswith("."))

i = 0
text = input("->")
c = "null"
while c != "|":
    c = text[i]
    if c == "|":
        break
    else:
        print(c)
        i += 1
