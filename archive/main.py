"""
Student:
    name: str
    marks: list[int]

Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""

# ==================================================
# Simulated storage
# ==================================================
students = {
    1: {
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    2: {
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football",
    },
}

LAST_ID_CONTEXT = 2


def represent_students():
    for id_, student in students.items():
        print(f"[{id_}] {student['name']}, marks: {student['marks']}")


# ==================================================
# CRUD (Create Read Update Delete)
# ==================================================
def add_marks(id_: int, marks_list: list):
    students[id_]['marks'].extend(marks_list)
    return marks_list

def add_student(student: dict) -> dict | None:
    global LAST_ID_CONTEXT

    if len(student) != 2:
        return None
    elif not student.get("name") or not student.get("marks"):
        return None
    else:
        LAST_ID_CONTEXT += 1
        students[LAST_ID_CONTEXT] = student

    return student


def search_student(id_: int) -> dict | None:
    return students.get(id_)


def delete_student(id_: int):
    if search_student(id_):
        del students[id_]
        print(f"Student with id '{id_}' is deleted")
    else:
        print(f"There is student '{id_}' in the storage")


def update_student(id_: int, payload: dict) -> dict:
    updated_name, updated_marks = payload.values()
    if updated_name:
        students[id_]['name'] = updated_name

    if updated_marks:
        students[id_]['marks'] = updated_marks
    return payload


def student_details(student: dict) -> None:
    print(f"Detailed info: [{student['name']}]...")


# ==================================================
# Handle user input
# ==================================================
def parse(data: str, change_mode: bool) -> tuple[str, list[int]]:
    """Return student name and marks.

    user input template:
    'John Doe;4,5,4,5,4,5'


    def foo(*args, **kwargs):
        pass

    """

    template = "John Doe;4,5,4,5,4,5"

    items = data.split(";")

    if len(items) != 2:
        raise Exception(f"Incorrect data. Template: {template}")

    # items == ["John Doe", "4,5...."]
    name, raw_marks = items

    marks = []
    if raw_marks or not change_mode:
        try:
            marks = [int(item) for item in raw_marks.split(",")]
        except ValueError as error:
            print(error)
            raise Exception(f"Marks are incorrect. Template: {template}") from error

    return name, marks

def ask_student_marks():
    """
    Input template:
        '4,5,4,5,4,5'

    Expected:
        4,5,4,5,4,5:    list[int]
    """
    prompt = "Enter student's marks using next template:\n'4,5,4,5,4,5': "
    raw_marks = input(prompt)
    try:
        marks = [int(item) for item in raw_marks.split(",")]
    except ValueError as error:
        print(error)
        raise Exception("Marks are incorrect. Template: '4,5,4,5,4,5'") from error

    return marks

def ask_student_payload(change_mode: bool = False):
    """
    Input template:
        'John Doe;4,5,4,5,4,5'

    Expected:
        John Doe:       str | None
        4,5,4,5,4,5:    list[int] | None
    """

    prompt = "Enter student's payload using next template:\n'John Doe;4,5,4,5,4,5': "

    if not (payload := parse(input(prompt), change_mode)):
        return None
    else:
        name, marks = payload

    return {"name": name, "marks": marks}


def handle_management_command(command: str):
    if command == "show":
        represent_students()

    elif command == "retrieve":
        search_id = input("Enter student's id to retrieve: ")

        try:
            id_ = int(search_id)
        except ValueError as error:
            raise Exception(f"ID '{search_id}' is not correct value") from error
        else:
            if student := search_student(id_):
                student_details(student)
            else:
                print(f"There is not student with id: '{id_}'")

    elif command == "remove":
        delete_id = input("Enter student's id to remove: ")

        try:
            id_ = int(delete_id)
        except ValueError as error:
            raise Exception(f"ID '{delete_id}' is not correct value") from error
        else:
            delete_student(id_)

    elif command == "change":
        update_id = input("Enter student's id you wanna change: ")

        try:
            id_ = int(update_id)
        except ValueError as error:
            raise Exception(f"ID '{update_id}' is not correct value") from error
        else:
            if data := ask_student_payload(change_mode=True):
                update_student(id_, data)
                print(f"✅ Student is updated")
                if student := search_student(id_):
                    student_details(student)
                else:
                    print(f"❌ Can not change user with data {data}")

    elif command == "add":
        data = ask_student_payload()
        if data is None:
            return None
        else:
            if not (student := add_student(data)):
                print(f"❌ Can't create user with data: {data}")
            else:
                print(f"✅ New student '{student['name']}' is created")
    elif command == "add marks":
        student_id = input("Enter student's id you wanna add marks: ")

        try:
            id_ = int(student_id)
        except ValueError as error:
            raise Exception(f"ID '{student_id}' is not correct value") from error
        else:
            if marks := ask_student_marks():
                if student := search_student(id_):
                    add_marks(id_, marks)
                    print(f"✅ Marks successfully added to student")
                    student_details(student)
                else:
                    print(f"❌ Can not add marks to user with data {marks}")

    else:
        raise SystemExit(f"Unrecognized command: '{command}'")


def handle_user_input():
    """This is an application entrypoint."""

    SYSTEM_COMMANDS = ("quit", "help")
    MANAGEMENT_COMMANDS = ("show", "add", "retrieve", "remove", "change", "add marks")
    AVAILABLE_COMMANDS = SYSTEM_COMMANDS + MANAGEMENT_COMMANDS

    help_message = (
        "Welcome to the Journal application. Use the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )

    print(help_message)

    while True:
        command = input("Enter the command: ")

        if command == "quit":
            print(f"\nThanks for using Journal application. Bye!")
            break
        elif command == "help":
            print(help_message)
        elif command in MANAGEMENT_COMMANDS:
            handle_management_command(command=command)
        else:
            print(f"Unrecognized command '{command}'")


handle_user_input()
