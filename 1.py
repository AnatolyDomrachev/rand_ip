from random import randint as rnd

days = ['31.07','01.08' ,'02.08','07.08', '08.08','09.08','14.08','15.08' ,'16.08','21.08', '22.08' ,'23.08','28.08', '29.08' ,'30.08']
print(days)
year = '2020'
#print(f'{rnd(0, 24):0>2}')

low_p = rnd(2, 7)/100
hi_p = 1-low_p
number = rnd(300, 700)
low_number = int(number*low_p)
low_hours = [0,1,2,3,4,5,6,22,23]
hi_hours = range(7,22)



def main():
    hours = get_hours()
    minutes = get_minutes()
    seconds = get_minutes()
    ips = get_ips()
    for day in days:
        fout = open(day+'.csv', 'w')
        for i in range(number):
            print(day+'.'+year , end = ' ', file = fout)
            print(f'{str(hours[i]):0>2}', end = ':', file = fout)
            print(f'{str(minutes[i]):0>2}', end = ';', file = fout)
            print(ips[i], file = fout)
'''
    print('low_p ', low_p)
    print('hi_p ', hi_p)
    print('number ', number)
    print('hours ', hours)
    print()
    print('minutes ', minutes)
    print()
    print('seconds ', seconds)
    print()
    print('ips ', ips)
'''

def get_hours():
    hours = []

    for i in range(low_number):
        hours.append(low_hours[rnd(0,len(low_hours)-1)])

    for i in range(number - low_number):
        hours.append(hi_hours[rnd(0,len(hi_hours)-1)])

    hours.sort()
    return hours

def get_minutes():
    minutes = []

    for i in range(number):
        minutes.append(rnd(0,59))

    return minutes

def get_ips():
    ips = []

    for i in range(number):
        ips.append(str(rnd(11,250)) + '.' + str(rnd(11,250)) + '.' +str(rnd(11,250)) + '.' +str(rnd(11,250)))

    return ips


main()

