"""
File:         hw4_part2.py
Author:       Vu Nguyen
Date:         9/30/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Using Caesar Salad Cipher method, user can in put in
              any phrase or word with the number of offset and the
              programs with encrypted that phrase.

"""

if __name__ == "__main__":
    encrypt_string = input("What is the string to encrypt? (or stop) ").strip()

    upperCase_list = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    lowerCase_list = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']

    while encrypt_string != 'stop':
        offset_value = int(input("What is the offset? ").strip())
        encrypt_char_list = []
        newEncrypt_char_list = []
        non_letter_list = []

        for character in encrypt_string:
            encrypt_char_list.append(character)

        # Check for characters that is not letter
        for special_char in encrypt_char_list:
            if (ord(special_char) < 65) and (ord(special_char) > 32):
                non_letter_list.append(special_char)
            elif (ord(special_char) > 90) and (ord(special_char) < 97):
                non_letter_list.append(special_char)
            elif (ord(special_char) > 122) or (ord(special_char) < 32):
                non_letter_list.append(special_char)

        # If there is nothing in the non_letter_list then execute this statement.
        if not non_letter_list:
            place_holder_string = ''
            for letter_index in range(len(encrypt_char_list)):

                # Check for lower case
                if (ord(encrypt_char_list[letter_index]) >= 97) and (ord(encrypt_char_list[letter_index]) <= 122):
                    lower_index = (ord(encrypt_char_list[letter_index]) + offset_value + (letter_index**2)) % 26
                    place_holder_string += lowerCase_list[lower_index]

                # Check for upper case
                elif (ord(encrypt_char_list[letter_index]) >= 65) and (ord(encrypt_char_list[letter_index]) <= 90):
                    upper_index = (ord(encrypt_char_list[letter_index]) + offset_value + (letter_index**2)) % 26
                    place_holder_string += upperCase_list[upper_index]

                # Check for space
                elif ord(encrypt_char_list[letter_index]) == 32:
                    place_holder_string += encrypt_char_list[letter_index]

            # Empty out this list for the next cycle
            encrypt_char_list = []
            print("The new encrypted string is:", place_holder_string)
            encrypt_string = input("What is the string to encrypt? (or stop) ").strip()
        else:
            print("The encrypted string should only contain letter, no special character or number!")
            encrypt_string = input("What is the string to encrypt? (or stop) ").strip()








