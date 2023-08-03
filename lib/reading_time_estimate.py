def reading_time_estimate(text_size):
    time_in_min = round(text_size / 200)
    if text_size == 0:
        return "No text to be read here"
    elif 0 < text_size < 200:
        return "This text will take less than 2 minutes to read"
    else:
        return f"This text will take {time_in_min} minutes to read"