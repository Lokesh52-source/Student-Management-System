def get_valid_roll_no(message):

    while True:
        try:
            roll_no = int(input(message))

            if roll_no > 0:
                return roll_no

            print("Roll Number must be greater than 0.")

        except ValueError:
            print("Please enter numbers only.")


def get_valid_name(message):

    while True:

        name = input(message).strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            return name


def get_valid_age(message):

    while True:
        try:
            age = int(input(message))

            if 5 <= age <= 100:
                return age

            print("Age must be between 5 and 100.")

        except ValueError:
            print("Please enter numbers only.")


def get_valid_course(message):

    while True:

        course = input(message).strip()

        if course == "":
            print("Course cannot be empty.")
        else:
            return course


def get_valid_marks(message):

    while True:
        try:
            marks = float(input(message))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")