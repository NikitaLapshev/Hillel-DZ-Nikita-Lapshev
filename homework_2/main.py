"""
DRY: do not repeat yourself


Student:
    name: str
    marks: list[int]


Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""

COMMANDS = ("quit", "show", "retrieve", "add")

# Simulated database
students = [
    {
        "id": 1,
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    {
        "id": 2,
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football",
    },
]


def find_student(id: int) -> dict | None:
    for student in students:
        if student["id"] == id:
            return student

    return None


def show_students() -> None:
    print("=" * 20)
    print("The list of students:\n")
    for student in students:
        print(f"№{student['id']}.{student['name']}. Marks: {student['marks']}")

    print("=" * 20)


def show_student(id: int) -> None:
    student: dict | None = find_student(id)

    if not student:
        print(f"There is no student {id}")
        return

    print("Detailed about student:\n")
    print(
        f"№{student['id']}.{student['name']}. Marks: {student['marks']}\n"
        f"Details: {student['info']}\n"
    )


def add_student(name: str, details: str | None):
    identifier = 1
    if students is not []:
        identifier = students[-1]["id"] + 1
    instance = {"id": identifier, "name": name, "marks": [], "info": details}
    students.append(instance)

    return instance


def main():
    print(f"Welcome to the Digital journal!\nAvailable commands: {COMMANDS}")
    while True:
        user_input = input("Enter the command: ")

        if user_input not in COMMANDS:
            print(f"Command {user_input} is not available.\n")
            continue

        if user_input == "quit":
            print("See you next time.")
            break

        try:
            if user_input == "show":
                show_students()
            elif user_input == "retrieve":
                student_id = input("Enter student id you are looking for: ")
                if student_id.isdigit():
                    show_student(int(student_id))
                else:
                    print("ID should be a valid integer")
            elif user_input == "add":
                name = input("Enter student's name: ")
                details = input("Enter student's details: ")
                add_student(name, details)

        except NotImplementedError as error:
            print(f"Feature '{error}' is not ready for live.")
        except Exception as error:
            print(error)


main()
