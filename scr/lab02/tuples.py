def format_record(record):
    if type(record) != tuple:
        raise TypeError("Input must be a tuple")
    if len(record) != 3:
        raise ValueError("Tuple must have exactly 3 elements")
    full_name, group, gpa = record
    if type(full_name) != str:
        raise TypeError("ФИО must be a string")
    if type(group) != str:
        raise TypeError("Group must be a string")
    if type(gpa) not in (int, float):
        raise TypeError("GPA must be a number")
    full_name = full_name.strip()
    if not full_name:
        raise ValueError("ФИО cannot be empty")
    group = group.strip()
    if not group:
        raise ValueError("Group cannot be empty")
    if gpa < 0:
        raise ValueError("GPA cannot be negative")
    name_parts = [part.strip() for part in full_name.split() if part.strip()]
    if len(name_parts) < 2:
        raise ValueError("ФИО must contain at least last name and first name")
    last_name = name_parts[0]
    first_names = name_parts[1:]
    initials = '.'.join(name[0].upper() for name in first_names) + '.'
    formatted_gpa = f"{gpa:.2f}"
    formatted_result = f"{last_name} {initials}, гр. {group}, GPA {formatted_gpa}"
    return formatted_result
print("=== format_record ===")   
print(format_record(("Иванов Иван Иванович", "БИВТ-25", 4.6)))  
print(format_record(("Петров Пётр", "IKB0-12", 5.0)))  
print(format_record(("Петров Пётр Петрович", "IKB0-12", 5.0)))
print(format_record(("Сидорова анна аергеевна", "АВВ-01", 3.999)))
    
 