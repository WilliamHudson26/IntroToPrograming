def smashmouth():
    print("Somebody once told me the world was gona roll me! I aint the sharpest tool in the shed!")

def pingas():
    print("Snooping as usual i see!")

def leonidas():
    print("THIS IS SPARTA!!!!")

def add(a: int,b: int):
    return (a+b)

function = input("what function would you like to run?\n->")
if function == "smashmouth":
    smashmouth()
if function == "pingas":
    pingas()
if function == "leonidas":
    leonidas()
if function == "calculator":
    a: int = input("variable a\n->")
    b: int = input("variable b\n->")
    function = input("how will you calculate?\n->")
    if function == "add":
        result = add(a,b)
    print(result)