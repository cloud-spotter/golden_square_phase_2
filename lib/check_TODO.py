def check_TODO(text):
    """Check whether the string #TODO is in a text.

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "Here is my #TODO list for Monday")

    Returns: (state the return value and its type)
        a boolean, T/F depending on whether #TODO features in the argument passed to it (e.g. True)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    if text == "":
        raise Exception("Text is empty!")
    else:
        return "#TODO" in text or "#todo" in text