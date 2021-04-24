# Backpack values for NLChoc program.

def ValText(TextValue):

    IsValid = True
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
    if TextValue == "":
        print("Invalid input - value cannot be blank.")
        IsValid = False
    elif not set(TextValue).issubset(allowed_char):
        print("Invalid input - entry contains invalid character.")
        IsValid = False

    return IsValid

def ValFloatNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = float(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid

def ValIntNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = int(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid

def StrAndPad(DollarValue):
    DollarValueStr = "${:,.2f}".format(DollarValue)
    DollarValuePad = "{:>10}".format(DollarValueStr)

    return DollarValuePad

def ValRentOwn(TextValue):

    IsValid = True
    allowed_char = set("OoRr")
    if TextValue == "":
        print("Invalid input - value cannot be blank.")
        IsValid = False
    elif not set(TextValue).issubset(allowed_char):
        print("Invalid input - entry contains invalid character.")
        IsValid = False

    return IsValid

def ValDate(TextValue):

    IsValid = True
    allowed_char = set("1234567890/")
    if TextValue == "":
        print("Invalid input - value cannot be blank.")
        IsValid = False
    elif not TextValue.subset(allowed_char):
        print("Invalid input - entry contains invalid character.")
        IsValid = False
    elif str(TextValue[2]) != "/" + str(TextValue[5]) != "/":
        print("Invalid input - not in the format DD/MM/YYYY")
        IsValid = False
    elif not str(TextValue[0]).isdigit() + str(TextValue[1]).isdigit() + str(TextValue[3]).isdigit() + str(TextValue[4]).isdigit() + str(TextValue[6]).isdigit() + str(TextValue[7]).isdigit() + str(TextValue[8]).isdigit() + str(TextValue[9]).isdigit():
        print("Invalid input - not in the format DD/MM/YYYY")
        IsValid = False

    return IsValid
