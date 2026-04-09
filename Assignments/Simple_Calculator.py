X = input("Please type in your variables\n-X->")
X = int(X)
Y = input("-Y->")
Y = int(Y)
opperator = input("Please type in the opperator\n->")

def Add():
    return X+Y
def Subtract():
    return X-Y
def Multiply():
    return X*Y
def Devide():
    return X/Y
def Exponent():
    return X**Y

if (opperator == "add"):
    result = Add()
if (opperator == "subtract"):
    result = Subtract()
if (opperator == "multiply"):
    result = Multiply()
if (opperator == "devide"):
    result = Devide()
if (opperator == "exponent"):
    result = Exponent()

print(result)