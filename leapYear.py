
def isLeapYear(year):
    # Hier müssen Sie erweitern ...
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("Welches Jahr soll überprüft werden? "))
    if isLeapYear(year):
        print( year, "ist ein Schaltjahr" )
    else:
        print( year, "ist KEIN Schaltjahr" )
if __name__ == "__main__":
    main()
