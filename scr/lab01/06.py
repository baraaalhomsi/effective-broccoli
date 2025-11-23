n = int(input())
ochno = 0
zaochno = 0
for _ in range(n):
    surname, name, age, form = input().split()
    if form == "True":
        ochno += 1
    else:
        zaochno += 1
print(ochno, zaochno)
