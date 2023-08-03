def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char not in " .!,?": # Added to get rid of bug caused by whitespace/punctuation
            # print(f"char: {char}") # This prints ok
            counter[char] = counter.get(char, 0) + 1
    # sorted_counter = sorted(counter.items()) # Breaking down what's going on in the code!
    # print("a", f"printing sorted_counter: {sorted_counter}")  #This prints ok
    # print("z", f"the first element of sorted_counter is :{sorted_counter[0]}") # This prints ok 
    # letter_key = sorted(counter.items(), key=lambda item: item[1])[0][1] #old letter variable (bug)
    # print("b", f"sorted(counter.items) by value instead: {sorted(counter.items(), key=lambda item: item[1])}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # print("c", f"returning most common letter: {letter}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

# Start small!:
# print(get_most_common_letter("the roof"))
# print(get_most_common_letter("the roof, the roof, the roof is on fire!"))