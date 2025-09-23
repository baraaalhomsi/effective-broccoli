print("your name is: ")
name=str(input())
length=len(name)
def first_letters(names):
    nnn=names.split()
    the_basic_part= [n[0] for n in nnn if n]
    return '.'.join(the_basic_part)
print("short name:",first_letters(name))
print("length(symbols):",length)