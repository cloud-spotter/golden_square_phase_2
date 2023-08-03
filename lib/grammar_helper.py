# Less complex scenario in exercise demonstration solution. 
# Solution also returns just T/F depending on whether correctly punctuated.

def grammar_helper(text_string):
    transformed_string = text_string.strip().capitalize()
    # Added .strip() to trim any leading/trailing whitespaces

    if text_string == "":
        raise Exception("Cannot punctuate an empty string")
    elif transformed_string[-1] in ".!?":
        return transformed_string
    elif transformed_string[-1] in ":;,":
        return transformed_string[:-1] + "."
    else: 
        return transformed_string + "."