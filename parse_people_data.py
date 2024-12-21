import re

def parse_person(line):
    # Regex patterns for basic validation
    name_pattern = r"^[A-Za-z\s]+$"
    age_pattern = r"^\d+$"
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    line = line.strip()
    fields = line.split(",")
    
    # Ensure there are exactly 3 fields
    if len(fields) != 3:
        raise ValueError(f"Invalid format: {line}")

    name, age, email = fields[0].strip(), fields[1].strip(), fields[2].strip()

    # Validate Name
    if not re.match(name_pattern, name):
        raise ValueError(f"Invalid Name: {name}")

    # Validate Age
    if not re.match(age_pattern, age) or not (0 <= int(age) <= 150):
        raise ValueError(f"Invalid Age: {age}")

    # Validate Email
    if not re.match(email_pattern, email):
        raise ValueError(f"Invalid Email: {email}")

    return {
        "Name": name,
        "Age": int(age),
        "Email": email
    }

def parse_file(file_content: list[str]):
    people = []
    for line in file_content:
        try:
            person = parse_person(line)
            people.append(person)
        except ValueError as e:
            print(f"Error: {e}")
    
    return people