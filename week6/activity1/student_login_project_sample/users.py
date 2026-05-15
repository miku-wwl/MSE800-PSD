from decorators import log_activity


@log_activity
def student_login(username):
    # Debugging note: this function represents a simple login action.
    # The decorator should print logs before and after this message.
    print(f"{username} logged into the system.")


@log_activity
def submit_assignment(username, assignment):
    # Debugging note: this function simulates a submission workflow.
    # The wrapper should still preserve the original function arguments.
    print(f"{username} submitted {assignment}.")


@log_activity
def view_grades(username):
    # Debugging note: this function is the third test case for the decorator.
    # It confirms the same logging behavior works for another function.
    print(f"{username} is viewing grades.")
