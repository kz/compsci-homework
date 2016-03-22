# Task 1
# Author: Kelvin Zhang
# Date Created: 2016-03-22
# This program takes in a word and makes it uppercase (e.g., "computing" -> "COMPUTING". It then takes in a keyword.
# An encrypted message is generated by adding the alphabet value of the message to the value of the keyword.
# If the word is longer than the keyword, the keyword repeats (e.g., "GCSE" -> "GCSEGCSEG" for "COMPUTING").


def convert_character_to_alphabet_value(char):
    return ord(char) - ASCII_A + 1  # Incremented by one as the alphabet does not use zero-based numbering


def convert_alphabet_value_to_character(val):
    return chr(ASCII_A + val - 1)


# This function takes a position of a message (starting from position zero [zero-based numbering])
# and returns the equivalent keyword letter for this position.
# E.g., if message is "COMPUTING", keyword is "GCSE" and we are taking the position five ("T"),
# the equivalent keyword letter would be "GCSE"[5 % 4] = "GCSE"[1] = "C"
def get_keyword_letter_for_position(keyword, pos):
    return keyword[pos % len(keyword)]


# ASCII value for the letter A
ASCII_A = 65

# Prompt for input
rawMessage = input("Enter your message: ")
keyword = input("Enter your keyword: ")

# Initialise empty string for the encrypted message
encryptedMessage = ""

# Loop through the raw message, generating the encrypted message
for i in range(0, len(rawMessage)):
    # Get the letter of the keyword as an alphabet value
    keywordLetter = get_keyword_letter_for_position(keyword, i)
    keywordValue = convert_character_to_alphabet_value(keywordLetter)

    # Get the alphabet value for the letter of the message
    messageValue = convert_character_to_alphabet_value(rawMessage[i])

    # Obtain the encrypted letter
    encryptedValue = (keywordValue + messageValue) % 26  # Modulo 26 is used to bring overflow values back to the start
    encryptedLetter = convert_alphabet_value_to_character(encryptedValue)

    # Append the letter to the message
    encryptedMessage += encryptedLetter

# Output to user
print(encryptedMessage)