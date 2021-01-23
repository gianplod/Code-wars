def to_nato(words):

    nato_words = []
    nato_dict = {

        "A"	:	"Alfa"	,
        "B"	:	"Bravo"	,
        "C"	:	"Charlie"	,
        "D"	:	"Delta"	,
        "E"	:	"Echo"	,
        "F"	:	"Foxtrot"	,
        "G"	:	"Golf"	,
        "H"	:	"Hotel"	,
        "I"	:	"India"	,
        "J"	:	"Juliett"	,
        "K"	:	"Kilo"	,
        "L"	:	"Lima"	,
        "M"	:	"Mike"	,
        "N"	:	"November"	,
        "O"	:	"Oscar"	,
        "P"	:	"Papa"	,
        "Q"	:	"Quebec"	,
        "R"	:	"Romeo"	,
        "S"	:	"Sierra"	,
        "T"	:	"Tango"	,
        "U"	:	"Uniform"	,
        "V"	:	"Victor"	,
        "W"	:	"Whiskey"	,
        "X"	:	"X-ray"	,
        "Y"	:	"Yankee"	,
        "Z"	:	"Zulu"	,
        "0"	:	"Zero"	,
        "1"	:	"One"	,
        "2"	:	"Two"	,
        "3"	:	"Three"	,
        "4"	:	"Four"	,
        "5"	:	"Five"	,
        "6"	:	"Six"	,
        "7"	:	"Seven"	,
        "8"	:	"Eight"	,
        "9"	:	"Nine",
    }

    letters = nato_dict.keys()

    for char in words:

        if char != ' ':

            if char.upper() in letters:

                nato_words.append(nato_dict.get(char.upper()))
            else:
                nato_words.append(char)

    return " ".join(nato_words)
