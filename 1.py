from random import randint as rnd

#print(f'{rnd(0, 24):0>2}')

low_p = rnd(2, 7)/100
hi_p = 1-low_p
number = rnd(300, 700)
low_hours = [0,1,2,3,4,5,6,22,23]
hi_hours = range(7,22)


print('low_p ', low_p)
print('hi_p ', hi_p)
print('number ', number)

def main():
    hours = get_hours()
    minutes = get_minutes()
    seconds = get_minutes()
    print('hours ', hours)
    print()
    print('minutes ', minutes)
    print()
    print('seconds ', seconds)


def get_hours():
    hours = []

    for i in range(int(number*low_p)):
        hours.append(low_hours[rnd(0,len(low_hours)-1)])

    for i in range(int(number*hi_p)):
        hours.append(hi_hours[rnd(0,len(hi_hours)-1)])

    hours.sort()
    return hours

def get_minutes():
    minutes = []

    for i in range(int(number*low_p)):
        minutes.append(rnd(0,59))

    for i in range(int(number*hi_p)):
        minutes.append(rnd(0,59))

    return minutes

main()

