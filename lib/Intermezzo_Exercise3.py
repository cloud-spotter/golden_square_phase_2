# Now debug with Discovery Debugging

def encode(text, key): # text = 'abc'
    cipher = make_cipher(key)
    # print(f"cipher = {cipher}")
    ciphertext_chars = []
    for i in text:
        # print(f"i in text ({text}) here is {i}")
        # print(f"cipher index {cipher.index(i)}")
        ciphered_char = chr(65 + cipher.index(i)) # Adds text index num to chr(65) i.e. unicode 'A', saves in variable
        # print(ciphered_char)
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        # print(f"letter i is {i}")
        # print(f"letter (65 - ord(i)) is {65 - ord(i)}") # Suspicious: minus numbers result!
        # print(f"letter (ord(i) - 65) is {ord(i) - 65}") # Corrected: no minus numbers now 
        # plain_char = cipher[65 - ord(i)] # bug No. 2! (Calculation to undo cipher was wrong way round.)
        plain_char = cipher[ord(i) - 65]
        # The ord() function returns the number representing the unicode code of a specified character.
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    # DISCOVERY DEBUGGING - step 1: understanding how the cipher output is constructed

    #alphabet = [print(f"adding {i} to unicode char 98 gives {chr(i + 98)}") for i in range(1, 26)]
    # alphabet = [print(f"adding {i} to unicode char 97 gives {chr(i + 97)}") for i in range(1, 26)] 
    # alphabet = [chr(i + 98) for i in range(1, 26)] -> original, with bug
    alphabet = [chr(i + 97) for i in range(0, 26)] # issue with this line? only alpha c-z and { included (not full alphabet)
    # The chr() function returns the character that represents the specified unicode.
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)
# ***This bug was sorted by fixing alphabet variable list comprehension***

#Commenting this out to deal just with the first example initially
print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")  

# make_cipher('ant')
# print(encode('ac', 'ant'))
# print(f"""
#   Running: encode('abc', 'ant')
#   Expected: ?
#   Actual:  {encode('abc', 'ant')}""")