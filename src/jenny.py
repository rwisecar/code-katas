"""Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him differently.
She added a special case to her function, but she made a mistake."""


def greet(name):
    """Return special hello for Johnny, normal greeting for everyone else."""
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {}!".format(name)
