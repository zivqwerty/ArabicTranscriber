

arabic_to_hebrew = {
    "ا": "א",
    "أ": "א",
    "إ": "א",
    "آ": "א",
    "ٱ": "א",
    "ب": "ב",
    "ت": "ת",
    "ث": "ת'",
    "ج": "ג'",
    "ح": "ח",
    "خ": "ח'",
    "د": "ד",
    "ذ": "ד'",
    "ر": "ר",
    "ز": "ז",
    "س": "ס",
    "ش": "ש",
    "ص": "צ",
    "ض": "צ'",
    "ط": "ט",
    "ظ": "ט'",
    "ع": "ע",
    "غ": "ע'",
    "ف": "פ",
    "ق": "ק",
    "ك": "כ",
    "ل": "ל",
    "م": "מ",
    "ن": "נ",
    "ه": "ה",
    "ة": "ה",
    "و": "ו",
    "ؤ": "או",
    "ي": "י",
    "ئ": "אי",
    "ى": "ת",
    "ء": "א'",

    "١": "1",
    "٢": "2",
    "٣": "3",
    "٤": "4",
    "٥": "5",
    "٦": "6",
    "٧": "7",
    "٨": "8",
    "٩": "9",
    "٠": "0",

    "؟": "?",
    "،": ",",
    ".": ".",

    str(chr(0x64E)): "◌ַ",
    str(chr(0x650)): "◌ִ",
    str(chr(0x64F)): "◌ֻ",
    str(chr(0x652)): "◌ְ",
    str(chr(0x651)): "◌ּ",

    str(chr(0x64B)): "◌ַן",
    str(chr(0x64D)): "◌ִן",
    str(chr(0x64C)): "◌ֻן",

}

vowels = {
    str(chr(0x64E)): "◌ַ",
    str(chr(0x650)): "◌ִ",
    str(chr(0x64F)): "◌ֻ",
    str(chr(0x652)): "◌ְ",
    str(chr(0x651)): "◌ּ",

    str(chr(0x64B)): "◌ַן",
    str(chr(0x64D)): "◌ִן",
    str(chr(0x64C)): "◌ֻן",
}


ending_letters = {
    "م": "ם",
    "ن": "ן",
    "ف": "ף",
    "ص": "ץ",
    "ض": "ץ'",
}

arabic_string = input("Enter Arabic string: ")
hebrew_string = ""
counter = 0
skip = 0

for character in arabic_string:

    # print(hex(ord(character)))

    if skip > 0:
        skip -= 1

    else:

        if character == "ة":
            if counter < len(arabic_string) - 4:
                if arabic_string[counter+1:counter+4] == " ال" or arabic_string[counter+1] in vowels:
                    hebrew_string += "ת"
            elif counter < len(arabic_string) - 1:
                if arabic_string[counter+1] in vowels:
                    hebrew_string += "ת"

        elif character == "ﹸ":
            if counter < len(arabic_string)-2:
                if arabic_string[counter + 1] == "و" and not arabic_string[counter + 2] in vowels:
                    hebrew_string += "וּ"
                    skip += 1
            elif counter == len(arabic_string)-2 and arabic_string[counter + 1] == "و":
                hebrew_string += "וּ"
                skip += 1
            else:
                hebrew_string += arabic_to_hebrew[character]

        else:
            if counter == len(arabic_string)-1:
                if character in ending_letters:
                    hebrew_string += ending_letters[character]
                elif character in arabic_to_hebrew:
                    hebrew_string += arabic_to_hebrew[character]
                else:
                    hebrew_string += character
            else:
                if arabic_string[counter + 1] == " " and character in ending_letters:
                    hebrew_string += ending_letters[character]
                elif character in arabic_to_hebrew:
                    hebrew_string += arabic_to_hebrew[character]
                else:
                    hebrew_string += character

    counter += 1

print("Hebrew tarnscription: " + hebrew_string)
