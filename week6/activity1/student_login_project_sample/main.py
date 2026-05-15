from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():

    # Debugging note: this entry point calls each user action in order
    # so we can verify the decorator output around every function call.

    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__":
    main()
