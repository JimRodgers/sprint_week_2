# Sprint Week 2 - NL Chocolate Company Travel Claim System Team 7 Jim Rodgers & Erin Slaney

import datetime as dt
import backpack as bp
import matplotlib.pyplot as plt

CurDate = dt.date.today()

# /OPTION 1/ Open default file & read values into variables. Prompt user for claim info. Calculate length of trip, number of KM if own vehicle, mileage, HST, & claim totals. Append claim file & update claim number. Prompt user to repeat or end process.
def EmpTravClaim():
    f = open('TCDef.dat', 'r')
    ClaimNum = int(f.readline())
    HSTRate = float(f.readline())
    LowPerDiem = float(f.readline())
    HighPerDiem = float(f.readline())
    KMRate = float(f.readline())
    RentalRate = float(f.readline())
    f.close()

    while True:
        EmpName = input("Employee name: ")
        IsValid = bp.ValText(EmpName)
        if IsValid:
            EmpName = EmpName.title()
            break
    while True:
        TripLocation = input("Enter the trip location: ")
        IsValid = bp.ValText(TripLocation)
        if IsValid:
            TripLocation = TripLocation.title()
            break
    while True:
        StartDate_str = input("Enter Start Date (DD/MM/YYYY): ")
        IsValid = bp.ValDate(StartDate_str)
        if IsValid:
            StartDate_str = str(StartDate_str)
            break
    while True:
        EndDate_str = input("Enter End Date (DD/MM/YYYY): ")
        IsValid = bp.ValDate(EndDate_str)
        if IsValid:
            EndDate_str = str(EndDate_str)
            break

    StartDate = dt.datetime.strptime(StartDate_str, "%d/%m/%Y")
    EndDate = dt.datetime.strptime(EndDate_str, "%d/%m/%Y")
    NumDays = (EndDate - StartDate).days

    if NumDays <= 3:
        PerDiem = LowPerDiem
    else:
        PerDiem = HighPerDiem

    while True:
        CarType = input("Rental or Own Vehicle (R or O): ")
        IsValid = bp.ValRentOwn(CarType)
        if IsValid:
            CarType = CarType.title()
            break

    if CarType == "O":
        while True:
            NumKM = input("Enter Number of Kilometres: ")
            IsValid = bp.ValIntNumber(NumKM, 1, 10000)
            if IsValid:
                NumKM = int(NumKM)
                break
        Mileage = NumKM * KMRate
    else:
        Mileage = NumDays * RentalRate

    HST = Mileage * HSTRate
    ClaimTotal = Mileage + PerDiem + HST

    cf = open("Claims.dat", "a")
    cf.write("{}, ".format(ClaimNum))
    cf.write("{}, ".format(EmpName))
    cf.write("{}, ".format(TripLocation))
    cf.write("{}, ".format(StartDate.strftime("%d/%m/%y")))
    cf.write("{}, ".format(EndDate.strftime("%d/%m/%y")))
    cf.write("{}, ".format(str(NumDays)))
    cf.write("{}, ".format(str(Mileage)))
    cf.write("{}, ".format(str(PerDiem)))
    cf.write("{}, ".format(str(HST)))
    cf.write("{}\n".format(str(ClaimTotal)))
    cf.close()

    print("Claim data successfully saved to file")
    ClaimNum += 1
    Cont = input("Process another claim? (Y/N): ")
    if Cont.upper() != "N":
        EmpTravClaim()
    else:
        f = open('TCDef.dat', 'w')
        f.write("{}\n".format(str(ClaimNum)))
        f.write("{}\n".format(str(HSTRate)))
        f.write("{}\n".format(str(LowPerDiem)))
        f.write("{}\n".format(str(HighPerDiem)))
        f.write("{}\n".format(str(KMRate)))
        f.write("{}\n".format(str(RentalRate)))
        f.close()

    return main()

# /OPTION 2/ Open default file & read values into variables. Prompt user to either enter a new value or keep the current value for each variable. Calculate & write new values to default file. Inform user of update.
def EditDefVal():
    f = open('TCDef.dat', 'r')
    ClaimNum = int(f.readline())
    HSTRate = float(f.readline())
    LowPerDiem = float(f.readline())
    HighPerDiem = float(f.readline())
    KMRate = float(f.readline())
    RentalRate = float(f.readline())
    f.close()

    print("Claims Processing System")
    print("Edit Default Values")
    print()
    print("For each value, enter an updated value, ")
    print("or press Enter to keep the existing value.")
    print("Current value is shown in ().")
    print()

    NewClaimNum = input("Enter the claim number (" + str(ClaimNum) + "): ")
    if NewClaimNum == "":
        NewClaimNum = ClaimNum
    NewHSTRate = input("Enter the HST rate (" + str(HSTRate) + "): ")
    if NewHSTRate == "":
        NewHSTRate = HSTRate
    NewLowPerDiem = input("Enter the low per diem (" + str(LowPerDiem) + "): ")
    if NewLowPerDiem == "":
        NewLowPerDiem = LowPerDiem
    NewHighPerDiem = input("Enter the high per diem (" + str(HighPerDiem) + "): ")
    if NewHighPerDiem == "":
        NewHighPerDiem = HighPerDiem
    NewKMRate = input("Enter the KM rate (" + str(KMRate) + "): ")
    if NewKMRate == "":
        NewKMRate = KMRate
    NewRentalRate = input("Enter the rental rate (" + str(RentalRate) + "): ")
    if NewRentalRate == "":
        NewRentalRate = RentalRate

    f = open('TCDef.dat', 'w')
    f.write("{}\n".format(str(NewClaimNum)))
    f.write("{}\n".format(str(NewHSTRate)))
    f.write("{}\n".format(str(NewLowPerDiem)))
    f.write("{}\n".format(str(NewHighPerDiem)))
    f.write("{}\n".format(str(NewKMRate)))
    f.write("{}\n".format(str(NewRentalRate)))
    f.close()

    print()
    print("Default values successfully updated")
    print()
    return main()

# /OPTION 3/ Display report header. Initialize counter and accumulators. Open claims file & list values in appropriate indeces. Display formatted claim values.  Process counter & accumulator values. Display formatted accumulator values with report footer.
def PrintClaimRep():
    print()
    print(
        " " * 9 + "1" + " " * 9 + "2" + " " * 9 + "3" + " " * 9 + "4" + " " * 9 + "5" + " " * 9 + "6" + " " * 9 + "7" + " " * 9 + "8")
    print("1234567890" * 8)
    print()
    print(" " * 26 + "SMACKERS CHOCOLATE COMPANY")
    print()
    print(" " * 19 + "TRAVEL CLAIMS LISTING AS OF " + (CurDate.strftime("%m/%d/%Y")))
    print()
    print("CLAIM" + " " * 4 + "CLAIM" + " " * 7 + "SALESPERSON" + " " * 5 + "CLAIM" + " " * 6 + "PER DIEM" + " " * 3 + "MILEAGE" + " " * 3 + "CLAIM")
    print("NUMBER" + " " * 3 + "DATE" + " " * 11 + "NAME" + " " + " " * 8 + "LOCATION" + " " * 3 + "AMOUNT" + " " * 5 + "AMOUNT" + " " * 4 + "AMOUNT")
    print("=" * 81)

    ClaimCtr = 0
    PerDiemAmtAcc = 0
    MileageAmtAcc = 0
    ClaimAmtAcc = 0

    f = open('Claims.dat', 'r')
    for claims in f:
        ClaimList = claims.split(",")
        ClaimNum = ClaimList[0]
        ClaimDate = ClaimList[3]
        VendName = ClaimList[1].strip()
        ClaimLoc = ClaimList[2].strip()
        PerDiemAmt = float(ClaimList[7])
        MileageAmt = float(ClaimList[8])
        ClaimAmt = float(ClaimList[9])

        print(" {}  {}   {}        {} {} {} {}".format(ClaimNum, ClaimDate, VendName, ClaimLoc, bp.StrAndPad(PerDiemAmt), bp.StrAndPad(MileageAmt), bp.StrAndPad(ClaimAmt)))
        ClaimCtr += 1
        PerDiemAmtAcc += PerDiemAmt
        MileageAmtAcc += MileageAmt
        ClaimAmtAcc += ClaimAmt
    f.close()
    print("=" * 81)
    print("TOTAL" + " " * 43 + "PER DIEM" + " " * 3 + "MILEAGE" + " " * 3 + "CLAIM AMT")
    print("CLAIMS" + " " * 42 + "TOTAL" + " " * 6 + "TOTAL" + " " + " " * 4 + "TOTAL")
    print(" {}                                          {} {} {}".format(ClaimCtr, bp.StrAndPad(PerDiemAmtAcc), bp.StrAndPad(MileageAmtAcc), bp.StrAndPad(ClaimAmtAcc)))
    print()
    print("End of listing")
    return main()

# /OPTION 4/ Initialize monthly claim totals. Open claims file and read values into variables. Assign totals to each month. List months as x-axis & totals as y-axis. Plot a line graph using these values.
def GraphTotals():
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0

    f = open("Claims.dat", "r")
    for Claims in f:
        ClaimList = Claims.split(",")
        ClaimDate = ClaimList[3].strip()
        ClaimAmt = ClaimList[9].strip()
        ClaimDate = dt.datetime.strptime(ClaimDate, "%d/%m/%y")
        ClaimAmt = float(ClaimAmt)
        ClaimMonth = ClaimDate.month
        if ClaimMonth == 1:
            Jan += ClaimAmt
        elif ClaimMonth == 2:
            Feb += ClaimAmt
        elif ClaimMonth == 3:
            Mar += ClaimAmt
        elif ClaimMonth == 4:
            Apr += ClaimAmt
        elif ClaimMonth == 5:
            May += ClaimAmt
        elif ClaimMonth == 6:
            Jun += ClaimAmt
        elif ClaimMonth == 7:
            Jul += ClaimAmt
        elif ClaimMonth == 8:
            Aug += ClaimAmt
        elif ClaimMonth == 9:
            Sep += ClaimAmt
        elif ClaimMonth == 10:
            Oct += ClaimAmt
        elif ClaimMonth == 11:
            Nov += ClaimAmt
        elif ClaimMonth == 12:
            Dec += ClaimAmt
    f.close()

    x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y_axis = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    plt.title("Claim totals over 1 year")
    plt.plot(x_axis, y_axis, color='darkblue', label="item 1")
    plt.xlabel("Time (months)")
    plt.ylabel("Total (dollars)")
    plt.grid(True)
    plt.legend()
    plt.show()
    return main()

# /MAIN MENU/ Display menu for the user offering a choice between 1 & 5. Each choice calls the corresponding function defined above allowing the user to run a menu option or exit the program.
def main():
    while True:
        print()
        print("NL Chocolate Company")
        print("Travel claims processing system")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Edit System Default Values.")
        print("3. Print the Travel Claim Report.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit")
        print()
        while True:
            Choice = input("Enter choice: (1-5): ")
            IsValid = bp.ValIntNumber(Choice, 1, 5)
            if IsValid:
                Choice = int(Choice)
                break
        if Choice == 1:
            EmpTravClaim()
        elif Choice == 2:
            EditDefVal()
        elif Choice == 3:
            PrintClaimRep()
        elif Choice == 4:
            GraphTotals()
        else:
            print("Thank-you for using the NL Chocolate Co. claims processing system & have a great day!")
            exit(0)


if __name__ == "__main__":
    main()

