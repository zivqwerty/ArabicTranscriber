

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
}

ending_letters = {
    "م": "ם",
    "ن": "ן",
    "ف": "ף",
    "ص": "ץ",
    "ض": "ץ'",
}

input = input("Enter Arabic string: ")
output = ""
counter = 0

for letter in input:

    if counter == len(input)-1:
        if letter in ending_letters:
            output += ending_letters[letter]
        elif letter in arabic_to_hebrew:
            output += arabic_to_hebrew[letter]
        else:
            output += letter
    elif input[counter+1] == " " and letter in ending_letters:
        output += ending_letters[letter]
    elif letter in arabic_to_hebrew:
        output += arabic_to_hebrew[letter]
    else:
        output += letter

    counter += 1

print("Hebrew tarnscription: " + output)
