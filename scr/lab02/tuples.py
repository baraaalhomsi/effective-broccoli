def format_record(fio: str,group: str,gpa: float) -> str:
    if not fio or not group:
        raise ValueError("you have to enter the name")
    if not isinstance(gpa, (float, int)):
        raise TypeError("type GPA shoud not be str")
    sfio=fio.split()
    sfio_len=len(sfio)
    f=sfio[0].capitalize()+" " if sfio_len >= 1 else ""
    i=sfio[1][0].capitalize()+"." if sfio_len >= 2 else ""
    o=sfio[2][0].capitalize()+"." if sfio_len >= 3 else ""
    x=f+i+o
    y=f"gr. {group}"
    z=f"GPA {gpa:.2f}"
    s= x + " " + y + " " + z
    return s
print(format_record("Иванов Иван Иванович", "BIVT-25", 4.6))
print(format_record("Петров Пётр", "IKBO-12", 5.0))
print(format_record("Петров Пётр Петрович", "IKBO-12", 5.0))
print(format_record("  сидорова  анна   сергеевна ", "ABB-01", 3.999))