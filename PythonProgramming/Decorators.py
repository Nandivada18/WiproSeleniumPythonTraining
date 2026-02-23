#decorator - wrapper function around the functions

#decorator method
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def vanilacake():
    print("I am the venila cake")

@make_pretty
def straberrycake():
    print("I am the straberry cake")

vanilacake()
straberrycake()