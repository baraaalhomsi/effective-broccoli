print("your name is: ")
name = str(input())


def first_letters(names):
    nnn = name.split()
    the_basic_part = [n[0] for n in nnn if n]
    return ".".join(the_basic_part)


length = len(name.replace(" ", ""))
print("short name:", first_letters(name))
print("length(symbols):", length)
