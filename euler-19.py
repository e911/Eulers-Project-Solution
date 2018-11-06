months_length = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leapyear(year):
    if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
        return True
    return False

def get_sundays(year2, year1=1900):
    sundays = 0
    day = 2 #given 1900, 1st Jan was sunday: so sunday the first day of week as 1 

    for year in range(year1, year2+1):
        for each_month in months_length:

            if day%7 == 1:
                sundays+=1 
            
            if is_leapyear(year) and each_month==2:
                day+=1
            
            day = day + each_month

    return sundays

if __name__ == "__main__":
    from_1900_1901 = get_sundays(1900)
    from_1900_2000 = get_sundays(2000)
    print(from_1900_2000 - from_1900_1901)

