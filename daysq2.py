def valid(D):
    year=int(D[6:])
    month=int(D[3:5])
    day=int(D[0:2])
    f=0;c=0
    if (year%4==0):
        c=1
    if month>=1 and month<=12:
        if month==2:
            if c==1:
                if day>=1 and day<=29:
                    f=1
            else:
                if day>=1 and day<=28:
                    f=1
        elif month in [1,3,5,7,8,10,12]:
            if day>=1 and day<=31:
                f=1
        else:
            if day>=1 and day<=30:
                f=1
    return f
date=input("enter date: ")
if valid(date)==1:
    print("valid date")
else:
    print("invalid date")
d=int(input("enter no of days : "))
year=int(date[6:])
month=int(date[3:5])
day=int(date[0:2])
d=d+day
day1=0
while (d>0):
    if year%4==0:
        months={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        day1=d
        month1=month
        d=d-months[month]
        month+=1
        if month>12:
            month=1
            year+=1
    else:
        months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        day1=d
        month1=month
        d=d-months[month]
        month+=1
        if month>12:
            month=1
            year+=1
mon=['01','02','03','04','05','06','07','08','09','10','11','12']
if day1>=1 and day1<=9:
    day1='0'+str(day1)
else:
    day1=str(day1)           
new_date=day1+"/"+mon[month1-1]+"/"+str(year)
if valid(new_date)==1:
    print("new date is valid date and\nIt is",new_date)
else:
    print("new date is invalid date")                  