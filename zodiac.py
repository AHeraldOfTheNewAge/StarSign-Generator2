import csv
import re
import sys

def main():
    if len(sys.argv) != 2: # CHECK FOR THE COMMAND LINE ARGUMENT
        sys.exit("Usage: zodiac.py date")

    list = read_csv("./horoscopes.csv") # READ THE CSV FILE

    if check_format(sys.argv[1]) == False:#CHECK FOR THE VALIDITY OF THE COMMAND LINE ARGUMENT
        sys.exit("Format MM/DD")

    month, day = sys.argv[1].split("/")

    month = int(month)
    day = int(day)

    if check_date_validity(month, day) == False:
        sys.exit("Format MM/DD")

    # GET THE ZODIAC SIGN
    zodiac = get_zodiac(month, day)
    sign = generate_sign(zodiac, list)

    # PRINT THE ZODIAC SIGN
    print(f"{zodiac} - {sign}")


def read_csv(x):
    # OPEN THE CSV FILE AND CREATE A NEW LIST THAT CONTAINS A DICT WITH THE ZODIAC NAME AND SIGN AS KEY-VALUE PAIR
    with open(x) as csvfile:
        reader = csv.DictReader(csvfile)
        list = []
        for row in reader:
            list.append({row["Horoscope"]:row["Sign"]})
        return list


def check_format(x):
    # CHECK THE VALIDITY OF THE INPUT BASED ON THE REGEX FORMULA
    date = re.search(r"^([0-1]*[0-9]+)\/([0-3]+[0-9]+)$", x)
    if date == None:
        return False


def check_date_validity(month, day):
    # CHECK THE VALIDITY OF THE MONTH AND DATE PROVIDED BY THE USER
    if month not in range(1,13):
        return False

    if day not in range(1,32):
        return False

    return True

def get_zodiac(x, y):
    # GET THE ZODIAC NAME ACCORDING TO THE DATES OF EACH ZODIAC SIGN
    if (x == 3 and y in range(21,32)) or (x == 4 and y in range(1,20)):
        return f"Aries"
    elif (x == 4 and y in range(20,31)) or (x == 5 and y in range(1,21)):
        return f"Taurus"
    elif (x == 5 and y in range(21,32)) or (x == 6 and y in range(1,21)):
        return f"Gemini"
    elif (x == 6 and y in range(21,31)) or (x == 7 and y in range(1,23)):
        return f"Cancer"
    elif (x == 7 and y in range(23,32)) or (x == 8 and y in range(1,23)):
        return f"Leo"
    elif (x == 8 and y in range(23,32)) or (x == 9 and y in range(1,23)):
        return f"Virgo"
    elif (x == 9 and y in range(23,31)) or (x == 10 and y in range(1,23)):
        return f"Libra"
    elif (x == 10 and y in range(23,32)) or (x == 11 and y in range(1,22)):
        return f"Scorpio"
    elif (x == 11 and y in range(22,31)) or (x == 12 and y in range(1,22)):
        return f"Sagittarius"
    elif (x == 12 and y in range(22,32)) or (x == 1 and y in range(1,20)):
        return f"Capricorn"
    elif (x == 1 and y in range(20,32)) or (x == 2 and y in range(1,19)):
        return f"Aquarius"
    elif (x == 2 and y in range(19,31)) or (x == 3 and y in range(1,21)):
        return f"Pisces"


def generate_sign(x, y):
    # GENERATE THE ZODIAC SIGN FROM THE LIST ALREADY CREATED BEFORE
    for i in range(0,12):
        if (y[i].get(x)) != None:
            return (y[i].get(x))


if __name__ == "__main__":
    main()
